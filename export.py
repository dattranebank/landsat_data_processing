import numpy as np
import pandas as pd
import rasterio


# Xuất tham số ảnh Landsat 8-9
def export_landsat_metadata(landsat_product_id, output_format, data_type_band_1_to_11_lst, cloud_cover,
                            cloud_cover_land, sun_elevation, map_projection, datum, utm_zone,
                            grid_cell_size_panchromatic, grid_cell_size_reflective, grid_cell_size_thermal,
                            corner_ul_lat_product, corner_ul_lon_product, corner_ur_lat_product,
                            corner_ur_lon_product, corner_ll_lat_product, corner_ll_lon_product, corner_lr_lat_product,
                            corner_lr_lon_product, radiance_mult_band_1_to_11_lst, radiance_add_band_1_to_11_lst,
                            reflectance_mult_band, reflectance_add_band, k1_constant_band_10, k2_constant_band_10,
                            k1_constant_band_11, k2_constant_band_11, txt_path):
    # Mở file txt và ghi nội dung của các tham số
    with open(txt_path, 'w') as file:
        file.write(f"LANDSAT_PRODUCT_ID = {landsat_product_id}\n")
        file.write(f"OUTPUT_FORMAT = {output_format}\n")

        # Ghi từng giá trị trong data_type_band_1_to_11_lst
        for i, value in enumerate(data_type_band_1_to_11_lst, start=1):
            file.write(f"DATA_TYPE_BAND_{i} = {value}\n")

        file.write(f"CLOUD_COVER = {cloud_cover}\n")
        file.write(f"CLOUD_COVER_LAND = {cloud_cover_land}\n")
        file.write(f"SUN_ELEVATION = {sun_elevation}\n")
        file.write(f"MAP_PROJECTION = {map_projection}\n")
        file.write(f"DATUM = {datum}\n")
        file.write(f"UTM_ZONE = {utm_zone}\n")
        file.write(f"GRID_CELL_SIZE_PANCHROMATIC = {grid_cell_size_panchromatic}\n")
        file.write(f"GRID_CELL_SIZE_REFLECTIVE = {grid_cell_size_reflective}\n")
        file.write(f"GRID_CELL_SIZE_THERMAL = {grid_cell_size_thermal}\n")
        file.write(f"CORNER_UL_LAT_PRODUCT = {corner_ul_lat_product}\n")
        file.write(f"CORNER_UL_LON_PRODUCT = {corner_ul_lon_product}\n")
        file.write(f"CORNER_UL_LON_PRODUCT = {corner_ur_lat_product}\n")
        file.write(f"CORNER_UR_LON_PRODUCT = {corner_ur_lon_product}\n")
        file.write(f"CORNER_LL_LAT_PRODUCT = {corner_ll_lat_product}\n")
        file.write(f"CORNER_LL_LON_PRODUCT = {corner_ll_lon_product}\n")
        file.write(f"CORNER_LR_LAT_PRODUCT = {corner_lr_lat_product}\n")
        file.write(f"CORNER_LR_LON_PRODUCT = {corner_lr_lon_product}\n")

        # Ghi từng giá trị trong radiance_mult_band_1_to_11_lst
        for i, value in enumerate(radiance_mult_band_1_to_11_lst, start=1):
            file.write(f"RADIANCE_MULT_BAND_{i} = {value}\n")

        # Ghi từng giá trị trong radiance_add_band_1_to_11_lst
        for i, value in enumerate(radiance_add_band_1_to_11_lst, start=1):
            file.write(f"RADIANCE_ADD_BAND_{i} = {value}\n")
        file.write(f"REFLECTANCE_MULT_BAND = {reflectance_mult_band}\n")
        file.write(f"REFLECTANCE_ADD_BAND = {reflectance_add_band}\n")
        file.write(f"K1_CONSTANT_BAND_10 = {k1_constant_band_10}\n")
        file.write(f"K2_CONSTANT_BAND_10 = {k2_constant_band_10}\n")
        file.write(f"K1_CONSTANT_BAND_11 = {k1_constant_band_11}\n")
        file.write(f"K2_CONSTANT_BAND_11 = {k2_constant_band_11}\n")

    print(f'Các tham số đã được xuất thành công ra {txt_path}')


# Xuất tổ hợp B432
def export_b432(band2_reflectance, band3_reflectance, band4_reflectance, band_transform, band_name):
    output_path = "D:\\VQG_TramChim\\03_landsat_processed_data\\" + band_name
    with rasterio.open(
            output_path,
            'w',
            driver='GTiff',
            height=band4_reflectance.shape[0],
            width=band4_reflectance.shape[1],
            count=3,  # 3 băng: Red, Green, Blue
            dtype='uint16',
            crs='EPSG:32648',  # CRS (tọa độ địa lý)
            transform=band_transform
    ) as dst:
        dst.write(band4_reflectance, 1)
        dst.write(band3_reflectance, 2)
        dst.write(band2_reflectance, 3)
    print(f"Ảnh tổ hợp B432 đã được xuất tại: {output_path}")


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
    output_path = "D:\\VQG_TramChim\\03_landsat_processed_data\\1. TOA_Radiance\\" + band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=band_toa_radiance.shape[0],
                       width=band_toa_radiance.shape[1],
                       count=1, dtype='float32', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(band_toa_radiance, 1)


# Xuất ảnh đã tính Surface Reflectance
def export_surface_reflectance(band_surface_reflectance, band_transform, band_name):
    output_path = "D:\\VQG_TramChim\\03_landsat_processed_data\\2. TOA_Reflectance\\" + band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=band_surface_reflectance.shape[0],
                       width=band_surface_reflectance.shape[1],
                       count=1, dtype='float32', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(band_surface_reflectance, 1)


def export_ndvi(ndvi, band_transform, band_name):
    output_path = "D:\\ThuNghiem\\5. NDVI, NDWI, LST\\" + band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=ndvi.shape[0],
                       width=ndvi.shape[1],
                       count=1, dtype='float32', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(ndvi, 1)


def export_ndwi(ndwi, band_transform, band_name):
    output_path = "D:\\ThuNghiem\\5. NDVI, NDWI, LST\\" + band_name

    # Xuất ảnh
    with rasterio.open(output_path, 'w', driver='GTiff', height=ndwi.shape[0],
                       width=ndwi.shape[1],
                       count=1, dtype='float32', crs='EPSG:32648',
                       transform=band_transform) as dst:
        dst.write(ndwi, 1)
