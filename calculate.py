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


# Tính TOA Brightness Temperature
def calculate_toa_brightness_temperature(band10_toa_radiance, k1, k2):
    band10_toa_bt = k2 / np.log(k1 / band10_toa_radiance + 1) - 272.15
    return band10_toa_bt


# Tính Land Surface Emissivity (LSE)
def calculate_lse(ndvi):
    # Tính NDVI min và NDVI max
    ndvi_min = np.min(ndvi)
    ndvi_max = np.max(ndvi)

    # Tính Proportion of Vegetation (PV)
    pv = ((ndvi - ndvi_min) / (ndvi_max + ndvi_min)) ** 2

    # Tính Land Surface Emissivity (LSE)
    lse = 0.004 * pv + 0.986
    return lse


# Tính Land Surface Temperature (LST)
def calculate_lst(band10_toa_bt, e):
    lst = (band10_toa_bt / 1) + 10.8 * (band10_toa_bt / 14380) * np.log(e)
    return lst
