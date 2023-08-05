#! /usr/bin/env python

"""Investigate spectra rescaling test failures when using in-flight filter throughput curves and zeropoints
"""

import astropy.units as u
import numpy as np

photmjsr = 0.202  # F322W2+CLEAR B mod, new value
pivot = 3.247
pixar = 9.34E-14 * u.sr
fnu = (photmjsr * u.MJy / u.sr * pixar.to(u.sr)).to(u.erg/u.second/u.cm/u.cm/u.Hz).value
flambda = 3.e18 * fnu / (pivot*1e4)**2
abzp = -2.5 * np.log10(fnu) - 48.599934378
stzp = -2.5 * np.log10(flambda) - 21.099934378
print(photmjsr, fnu, flambda, abzp, stzp)





import os
import numpy as np
import copy

from astropy.io import ascii
from astropy.table import Table
import astropy.units as u
from synphot import SourceSpectrum, Observation, units
from synphot.spectrum import SpectralElement
from synphot.models import Empirical1D
from synphot.models import BlackBodyNorm1D

from mirage.catalogs import spectra_from_catalog as spec
from mirage.catalogs import hdf5_catalog as hdf5
from mirage.utils.constants import FLAMBDA_CGS_UNITS, FNU_CGS_UNITS, MEAN_GAIN_VALUES
from mirage.utils.utils import get_filter_throughput_file, magnitude_to_countrate



primary_area = 25.326 * (u.m * u.m)
magnitude = 18.0

# Create spectrum: one source to be normalized
# and the other should not be
waves = np.arange(0.4, 5.6, 0.01) * u.micron
flux = np.repeat(1e-16, len(waves)) * u.pct
#spectra = {1: {"wavelengths": waves * u.micron,
#                "fluxes": flux * u.pct}}
#rescaled_spectra = copy.deepcopy(spectra)
inst, filt, pup, mod, det = 'nircam', 'F322W2', 'CLEAR', 'B', 'NRCB5'
magsys = 'abmag'
gain = 1.82
photfnu = 9.37562006925883e-31
photflam = 2.6678209425579067e-21
old_photfnu = 2.1263616854851517e-31
old_phtoflam = 6.0976465869679935e-22


# ----------------------BANDPASSES--------------------------
filter_thru_file = '/Users/hilbert/python_repos/mirage/mirage/config/F322W2_CLEAR_nircam_plus_ote_throughput_modb_sorted.txt'
old_filter_thru_file = '/Users/hilbert/python_repos/mirage/mirage/config/OLD_F322W2_CLEAR_nircam_plus_ote_modb_throghput.txt'

# Create bandpass for new throughput curve
filter_tp = ascii.read(filter_thru_file)
bp_waves = filter_tp['Wavelength_microns'].data * u.micron
bp_waves = bp_waves.to(u.Angstrom)
thru = filter_tp['Throughput'].data
bandpass = SpectralElement(Empirical1D, points=bp_waves.value, lookup_table=thru) / gain

# Create bandpass for old throughput curve
old_filter_tp = ascii.read(old_filter_thru_file)
old_bp_waves = old_filter_tp['Wavelength_microns'].data * u.micron
old_bp_waves = old_bp_waves.to(u.Angstrom)
old_thru = old_filter_tp['Throughput'].data
old_bandpass = SpectralElement(Empirical1D, points=old_bp_waves.value, lookup_table=old_thru) / gain
# ---------------------------------------------------------

#rescaled_spectra = spec.rescale_normalized_spectra(spectra, sub_catalog, magsys, filter_thru_file, gain)
# broken into pieces below
#waves = spectra[dataset]['wavelengths']
#flux = spectra[dataset]['fluxes']

# SourcSspectrum of input spectrum
fake_flux_units = units.FLAM
source_spectrum = SourceSpectrum(Empirical1D, points=waves, lookup_table=flux.value * fake_flux_units)

# Renormalize
renorm = source_spectrum.normalize(magnitude * u.ABmag, bandpass, vegaspec=None)
rescaled_flux = renorm(waves, flux_unit='flam')

old_renorm = source_spectrum.normalize(magnitude * u.ABmag, old_bandpass, vegaspec=None)
old_rescaled_flux = old_renorm(waves, flux_unit='flam')

# this is the end of the rescaling function

# SourceSpectrum of spectrum rescaled to the requested magnitude
rescaled_spectrum = SourceSpectrum(Empirical1D, points=waves, lookup_table=rescaled_flux)
old_rescaled_spectrum = SourceSpectrum(Empirical1D, points=waves, lookup_table=old_rescaled_flux)

# Compare the total area under the curve for the old vs new bandpass
rescaled_area = np.trapz(rescaled_flux, x=waves)
old_area = np.trapz(old_rescaled_flux, x=waves)
print('rescaled area: ', rescaled_area)
print('old area: ', old_area)
print('ratio: ', rescaled_area / old_area)


obs = Observation(rescaled_spectrum, bandpass, binset=bandpass.waveset)
renorm_counts = obs.countrate(area=primary_area)
print(renorm_counts)

old_obs = Observation(old_rescaled_spectrum, old_bandpass, binset=old_bandpass.waveset)
old_renorm_counts = old_obs.countrate(area=primary_area)
print('Counts: ', renorm_counts)
print('Old counts: ', old_renorm_counts)
print('ratio: ', renorm_counts / old_renorm_counts)


check_counts = magnitude_to_countrate(inst, filt, magsys, magnitude, photfnu=photfnu,
                                                          photflam=photflam)
old_check_counts = magnitude_to_countrate(inst, filt, magsys, magnitude, photfnu=old_photfnu,
                                                          photflam=old_photflam)

print('mags_to_countrate: ', check_counts)
print('old mags_to_countrate: ', old_check_counts)
print('ratio: ', check_counts / old_check_counts)
