import numpy as np


# Chuyển band_dn sang band_toa_radiance (DNs sang TOA Radiance)
def calculate_toa_radiance(band_dn, radiance_mult_band, radiance_add_band):
    band_toa_radiance = radiance_mult_band * band_dn + radiance_add_band
    return band_toa_radiance


# Chuyển band_dn sang band_toa_radiance (DNs sang TOA Radiance)
def calculate_toa_radiance_b10(band_dn, radiance_mult_band, radiance_add_band):
    band_toa_radiance_b10 = radiance_mult_band * band_dn + radiance_add_band - 0.29
    return band_toa_radiance_b10


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


# Tính NDWI (Gao) từ Band 5 và Band 6
def calculate_ndwi(band5, band6):
    ndwi = (band5 - band6) / (band5 + band6)
    return ndwi


# Tính TOA Brightness Temperature
def calculate_toa_brightness_temperature(band10_toa_radiance, k1, k2):
    band10_toa_bt = k2 / np.log(k1 / band10_toa_radiance + 1) - 273.15
    return band10_toa_bt


# Tính Land Surface Emissivity (LSE)
def calculate_lse(ndvi, band4_surface_reflectance):
    # Tính NDVI min và NDVI max
    ndvi_min = 0.2
    ndvi_max = 0.5

    # Tính Proportion of Vegetation (PV)
    pv = ((ndvi - ndvi_min) / (ndvi_max - ndvi_min)) ** 2

    # Tính LSE theo ngưỡng NDVI
    epsilon_v = 0.99
    epsilon_s = 0.97
    F = 0.55

    # dε chỉ áp dụng khi 0.2 <= NDVI <= 0.5
    de = (1 - epsilon_s) * (1 - pv) * F * epsilon_v
    de = np.where((ndvi >= ndvi_min) & (ndvi <= ndvi_max), de, 0)

    lse = np.where(
        ndvi < ndvi_min,
        band4_surface_reflectance if band4_surface_reflectance is not None else 0.97,
        np.where(
            ndvi > ndvi_max,
            epsilon_v,
            epsilon_v * pv + epsilon_s * (1 - pv) + de
        )
    )
    return pv, lse


# Tính Land Surface Temperature (LST)
def calculate_lst(band10_toa_bt, lse):
    # lse is e
    lst = band10_toa_bt / (1 + (10.895 * band10_toa_bt / 0.01438) * np.log(lse))
    return lst
