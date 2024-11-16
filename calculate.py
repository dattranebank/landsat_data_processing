import numpy as np


# Chuyển band_dn sang band_toa_radiance (DNs sang TOA Radiance)
def calculate_toa_radiance(band_dn, radiance_mult_band, radiance_add_band):
    band_toa_radiance = radiance_mult_band * band_dn + radiance_add_band
    return band_toa_radiance


# Chuyển band_dn sang band_toa_reflectance (DNs sang TOA Reflectance) và chuyển toa_reflectance sang surface_reflectance
def calculate_surface_reflectance(band_dn, reflectance_mult_band, reflectance_add_band, sun_elevation):
    band_toa_reflectance = (reflectance_mult_band * band_dn + reflectance_add_band) / np.sin(np.radians(sun_elevation))
    # band_toa_reflectance = (reflectance_mult_band * band_dn - reflectance_add_band) / 0.8259399926
    band_surface_reflectance = band_toa_reflectance / 0.9
    return band_surface_reflectance


# Tính NDVI từ Band 4 và Band 5
def calculate_ndvi(band4, band5):
    ndvi = (band5 - band4) / (band5 + band4)
    return ndvi


# Tính NDWI từ Band 3 và Band 5
def calculate_ndwi(band3, band5):
    ndwi = (band3 - band5) / (band3 + band5)
    return ndwi
