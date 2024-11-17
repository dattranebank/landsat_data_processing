import numpy as np
import pandas as pd
import rasterio


# Xuất ảnh viễn thám thành file csv
def export_remote_sensing_image_to_csv(band, band_name):
    # Chuyển mảng numpy thành DataFrame
    df = pd.DataFrame(band)

    # Xuất DataFrame thành file .csv
    df.to_csv(f"{band_name}.csv", index=False, header=False)


# Xuất cùng ảnh
def export_origin(band, band_transform, band_name):
    output_path = band_name
    with rasterio.open(output_path, 'w', driver='GTiff', height=band.shape[0],
                       width=band.shape[1],
                       count=1, dtype='uint16', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(band, 1)


# Xuất ảnh đã tính TOA Radiance
def export_toa_radiance(band_toa_radiance, band_transform, band_name):
    output_path = band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=band_toa_radiance.shape[0],
                       width=band_toa_radiance.shape[1],
                       count=1, dtype='uint16', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(band_toa_radiance, 1)


# Xuất ảnh đã tính Surface Reflectance
def export_surface_reflectance(band_surface_reflectance, band_transform, band_name):
    output_path = "D:\\ThuNghiem\\4. TOA_Reflectance\\" + band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=band_surface_reflectance.shape[0],
                       width=band_surface_reflectance.shape[1],
                       count=1, dtype='float32', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(band_surface_reflectance, 1)


def export_ndvi(ndvi, band_transform,band_name):
    output_path = "D:\\ThuNghiem\\5. NDVI, NDWI, LST\\" + band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=ndvi.shape[0],
                       width=ndvi.shape[1],
                       count=1, dtype='float32', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(ndvi, 1)


def export_ndwi(ndwi, band_transform,band_name):
    output_path = "D:\\ThuNghiem\\5. NDVI, NDWI, LST\\"+band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=ndwi.shape[0],
                       width=ndwi.shape[1],
                       count=1, dtype='float32', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(ndwi, 1)
