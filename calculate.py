
import numpy as np


# Chuyển band_dn sang band_toa_radiance (DN sang TOA Radiance)
def calculate_toa_radiance(band_dn, mult_band, add_band, sun_elevation):
    band_toa_radiance = (mult_band * band_dn + add_band) / np.sin(np.radians(sun_elevation))
    return band_toa_radiance

# Chuyển band_dn sang band_toa_reflectance (DN sang TOA Reflectance)
def calculate_toa_reflectance(band_dn, mult_band, add_band, sun_elevation):
    band_toa_reflectance = (mult_band * band_dn + add_band) / np.sin(np.radians(sun_elevation))
    return band_toa_reflectance

