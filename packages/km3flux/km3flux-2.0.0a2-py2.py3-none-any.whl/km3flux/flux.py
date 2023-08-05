"""Assorted Fluxes, in  (m^2 sec sr GeV)^-1"""

import gzip
import logging
import io
import re

import numpy as np
import numpy.lib.recfunctions as rfn

import scipy.interpolate
from scipy.integrate import romberg, simps
from scipy.interpolate import splrep, splev, RectBivariateSpline

from km3flux.data import basepath


logger = logging.getLogger(__name__)


class BaseFlux(object):
    """Base class for fluxes.

    Methods
    =======
    __call__(energy, zenith=None)
        Return the flux on energy, optionally on zenith.
    integrate(zenith=None, emin=1, emax=100, **integargs)
        Integrate the flux via romberg integration.
    integrate_samples(energy, zenith=None, emin=1, emax=100)
        Integrate the flux from given samples, via simpson integration.

    Example
    =======
    >>> zen = np.linspace(0, np.pi, 5)
    >>> ene = np.logspace(0, 2, 5)

    >>> from km3flux.flux import MyFlux
    >>> flux = MyFlux(flavor='nu_mu')

    >>> flux(ene)
    array([6.68440000e+01, 1.83370000e+01, 4.96390000e+00,
           1.61780000e+00, 5.05350000e-01,])
    >>> flux(ene, zen)
    array([2.29920000e-01, 2.34160000e-02, 2.99460000e-03,
           3.77690000e-04, 6.87310000e-05])
    """

    def __init__(self, **kwargs):
        pass

    def __call__(self, energy, zenith=None, interpolate=True):
        logger.debug("Interpolate? {}".format(interpolate))
        energy = np.atleast_1d(energy)
        logger.debug("Entering __call__...")
        if zenith is None:
            logger.debug("Zenith is none, using averaged table...")
            return self._averaged(energy, interpolate=interpolate)
        zenith = np.atleast_1d(zenith)
        if len(zenith) != len(energy):
            raise ValueError("Zenith and energy need to have the same length.")
        logger.debug("Zenith available, using angle-dependent table...")
        return self._with_zenith(energy=energy, zenith=zenith, interpolate=interpolate)

    def _averaged(self, energy, interpolate=True):
        logger.debug("Interpolate? {}".format(interpolate))
        raise NotImplementedError

    def _with_zenith(self, energy, zenith, interpolate=True):
        logger.debug("Interpolate? {}".format(interpolate))
        raise NotImplementedError

    def integrate(self, zenith=None, emin=1, emax=100, interpolate=True, **integargs):
        logger.debug("Interpolate? {}".format(interpolate))
        return romberg(self, emin, emax, vec_func=True, **integargs)

    def integrate_samples(
        self, energy, zenith=None, emin=1, emax=100, interpolate=True, **integargs
    ):
        logger.debug("Interpolate? {}".format(interpolate))
        energy = np.atleast_1d(energy)
        mask = (emin <= energy) & (energy <= emax)
        energy = energy[mask]
        if zenith:
            logger.debug("Zenith available, using angle-dependent table...")
            zenith = np.atleast_1d(zenith)
            zenith = zenith[mask]
        flux = self(energy, zenith=zenith, interpolate=interpolate)
        return simps(flux, energy, **integargs)


class PowerlawFlux(BaseFlux):
    """E^-gamma flux."""

    def __init__(self, gamma=2, scale=1e-4):
        self.gamma = gamma
        self.scale = scale

    def _averaged(self, energy, interpolate=True):
        return self.scale * np.power(energy, -1 * self.gamma)

    def integrate(self, zenith=None, emin=1, emax=100, **integargs):
        """Compute analytic integral instead of numeric one."""
        if np.around(self.gamma, decimals=1) == 1.0:
            return np.log(emax) - np.log(emin)
        num = np.power(emax, 1 - self.gamma) - np.power(emin, 1 - self.gamma)
        den = 1.0 - self.gamma
        return self.scale * (num / den)


class IsotropicFlux:
    def __init__(self, data, flavors):
        self._data = data
        self._flavors = flavors
        for flavor in flavors:
            flux = scipy.interpolate.InterpolatedUnivariateSpline(
                data.energy, data[flavor]
            )
            setattr(self, flavor, flux)

    def __getitem__(self, flavor):
        if flavor in self._flavors:
            return getattr(self, flavor)
        raise KeyError(
            f"Flavor '{flavor}' not present in data. "
            "Available flavors: {', '.join(self._flavors)}"
        )


class HondaFlux:
    """Base class for Honda fluxes

    Methods
    =======
    make_regular_grid(axes_keys, flavor)
        Create a n_dim grid based on data.
    interpolation_method(axes_keys, flavor)
        Select the interpolation method.
    parse_categories(f)
        Integrate the flux from given samples, via simpson integration.
    """

    def __init__(self, data, flavors):

        # Add cosz and phi_az bin center
        data = rfn.append_fields(
            data, "cosz_mean", (data.cosz_min + data.cosz_max) / 2.0, dtypes=float
        ).view(np.recarray)
        data = rfn.append_fields(
            data, "phi_az_mean", (data.phi_az_min + data.phi_az_max) / 2.0, dtypes=float
        ).view(np.recarray)

        self._flavors = flavors
        self._data = data
        self._axes = ["energy"]

        # Check number of input dimensions
        if len(np.unique(data.cosz_mean)) > 1:
            self._axes.append("cosz_mean")
        if len(np.unique(data.phi_az_mean)) > 1:
            self._axes.append("phi_az_mean")

        self._n_dim = len(self._axes)

        # Set the interpolation method accordingly
        for flavor in flavors:
            flux = self.interpolation_method(self._axes, flavor)
            setattr(self, flavor, flux)

    def make_regular_grid(self, axes_keys, flavor):
        """
        Create a n_dim grid based on data.

        Parameters
        ----------
        axes_keys : list of str
            axes to be used, define dimensions order
        flavor : str
            column to use to fill the grid
        """
        axes = []
        dim = []

        for key in axes_keys:
            r = np.sort(np.unique(self._data[key]))
            axes.append(r)
            dim.append(len(r))

        self._data.sort(order=axes_keys)
        grid = np.reshape(self._data[flavor], np.array(dim))
        return grid, axes

    def interpolation_method(self, axes_keys, flavor):
        """
        Select the interpolation method.

        For 1D interpolation:
        - InterpolatedUnivariateSpline
        For 2D interpolation:
        - RectBivariateSpline
        For >= 3D interpolation:
        - RegularGridInterpolator

        Parameters
        ----------
        axes_keys : list of str
            axes to be used, define dimensions order
        flavor : str
            column to use to fill the grid
        """
        if len(axes_keys) == 1:
            return scipy.interpolate.InterpolatedUnivariateSpline(
                self._data.energy, self._data[flavor]
            )

        elif len(axes_keys) == 2:
            grid, axes = self.make_regular_grid(axes_keys, flavor)
            return scipy.interpolate.RectBivariateSpline(*axes, grid).ev

        else:
            grid, axes = self.make_regular_grid(axes_keys, flavor)
            flux = scipy.interpolate.RegularGridInterpolator(
                axes, grid, bounds_error=False, fill_value=None
            )

            def columnar_interface(*args):
                return flux(np.stack(args).T)

            return columnar_interface

    def __getitem__(self, flavor):
        if flavor in self._flavors:
            return getattr(self, flavor)
        raise KeyError(
            f"Flavor '{flavor}' not present in data. "
            "Available flavors: {', '.join(self._flavors)}"
        )

    @classmethod
    def from_hondafile(cls, filepath):

        with gzip.open(filepath, "r") as fobj:
            flavors = ["numu", "anumu", "nue", "anue"]

            cats = cls.parse_categories(cls, fobj)

            data = []
            for header, content in cats:

                # Split the header to get cosZ and phi_Az ranges (4 numbers)
                header = " ".join(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", header))
                header_cols = ["cosz_min", "cosz_max", "phi_az_min", "phi_az_max"]

                # Create a dummy file object from sub range content +
                # additional columns for the cos Zenith and phi
                # Azimuth
                f = io.StringIO(header.join([""] + content))

                # Create a recarray from the file
                data_tmp = np.recfromcsv(
                    f,
                    names=header_cols + ["energy"] + flavors,
                    skip_header=2,
                    delimiter=" ",
                )
                data.append(data_tmp)

            # Merge invidual rec arrays to one
            data = rfn.stack_arrays(data, asrecarray=True, usemask=False)

            return cls(data, flavors)

    def parse_categories(self, f):
        """
        Select the interpolation method.

        Parameters
        ----------
        f : file object
            Honda file to be parsed
        """
        cats = []
        last_cat_start = -1
        last_cat_header = ""
        lines = []
        for i, line in enumerate(f):
            line = line.decode("ascii")
            if bool(line.count("average flux in")):
                if len(lines) != 0:
                    cats.append((last_cat_header, lines))
                    lines = []
                last_cat_header = line
            lines.append(line)
        cats.append((last_cat_header, lines))
        f.seek(0)
        return cats


class Honda:
    _experiments = {
        "Frejus": "frj",
        "Gran Sasso": "grn",
        "Homestake": "hms",
        "INO": "ino",
        "JUNO": "juno",
        "Kamioka": "kam",
        "Pythasalmi": "pyh",
        "Soudan Mine": "sdn",
        "South Pole": "spl",
        "Sudbury": "sno",
    }
    _datapath = basepath / "honda"

    #    def __init__(self):
    #        self._years = [p.name for p in self._datapath.glob("????") if p.is_dir()]

    def flux(
        self, year, experiment, solar="min", mountain=False, season=None, averaged=None
    ):
        """
        Return the flux for a given year and experiment.

        Parameters
        ----------
        year : int
            The year of the publication.
        experiment : str
            The experiment name, can be one of the following:
            "Kamioka", "Gran Sasso", "Sudbury", "Frejus", "INO", "South Pole",
            "Pythasalmi", "Homestake", "JUNO"
        solar : str (optional)
            The solar parameter, can be "min" or "max". Default is "min" for Solar
            minimum.
        mountain : bool (optional)
            With or without mountain over the detector. Default is "False" => without.
        season : None or (int, int) (optional)
            The season of interest. If `None`, the dataset for the full period is taken.
            If a tuple is provided, the first entry is the starting and the last the
            ending month. Notice that the corresponding dataset might not be available.
        averaged : None or str (optional)
            The type of averaging. Default is `None`. Also available are "all" for all
            direction averaging and "azimuth" for azimuth averaging only.
        """
        filepath = self._filepath_for(
            year, experiment, solar, mountain, season, averaged
        )
        if not filepath.exists():
            raise FileNotFoundError(
                f"The requested data file {filepath} could not be found in the archive. "
                "Try running `km3flux update` (see `km3flux -h` for more information) and "
                "also make sure the requested combination of parameters is available."
            )

        return HondaFlux.from_hondafile(filepath)

    def _filepath_for(self, year, experiment, solar, mountain, season, averaged):
        """Generate the filename and path according to the naming conventions of Honda

        Does some sanity checks too.
        """
        exp = self.experiment_abbr(experiment)
        filename = exp

        if year >= 2014:  # seasonal data was added in 2014
            if season is None:
                filename += "-ally"
            else:
                filename += f"-{season[0]:02d}{season[1]:02d}"

            if averaged is None:
                filename += "-20-12"
            elif averaged == "azimuth":
                filename += "-20-01"
            elif averaged == "all":
                filename += "-01-01"
            else:
                raise ValueError(
                    f"Unsupported averageing '{averaged}', "
                    "please use `None`, 'all', or 'azimuth'."
                )

            if mountain:
                filename += "-mtn"

        if solar in ("min", "max"):
            filename += f"-sol{solar}"
        else:
            raise ValueError(
                f"Unsupported solar parameter '{solar}' "
                "please use either 'min' or 'max'."
            )

        if year <= 2011:
            if season:
                raise ValueError(
                    "No seasonal tables available for year 2011 and earlier."
                )

            if mountain:
                if averaged == "all":
                    raise ValueError(
                        "No published mountain data for all directions averaged."
                    )
                filename += "-mountain"

            if averaged is None:
                filename += ""
            elif averaged == "azimuth":
                filename += "-aa"
            elif averaged == "all":
                filename += "-alldir"
            else:
                raise ValueError(
                    f"Unsupported averageing '{averaged}', "
                    "please use `None`, 'all', or 'azimuth'."
                )

        filename += ".d.gz"
        filepath = self._datapath / str(year) / filename
        return filepath

    @property
    def experiments(self):
        """Return a list of supported experiments."""
        return sorted(list(self._experiments.keys()))

    def experiment_abbr(self, experiment):
        """Return the abbreviation used in filenames for a given experiment."""
        try:
            return self._experiments[experiment]
        except KeyError:
            experiments = ", ".join(self.experiments)
            raise KeyError(
                f"The '{experiment}' is not in the list of available experiments: {experiments}"
            )
