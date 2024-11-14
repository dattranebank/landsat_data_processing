import rasterio

import matplotlib.pyplot as plt
from calculate import *
from export import *

# # Đọc ảnh Band 4 (Red) và Band 5 (NIR)
# def read_band(file_path):
#     with rasterio.open(file_path) as src:
#         band_data = src.read(1)  # Đọc dữ liệu từ band đầu tiên
#     return band_data
#
#
# # Đường dẫn tới ảnh Band 4 và Band 5
# band4_path = "D:\\ThuNghiem\\LC09_L1TP_125053_20240226_20240226_02_T1_B4.TIF"
# band5_path = "D:\\ThuNghiem\\LC09_L1TP_125053_20240226_20240226_02_T1_B5.TIF"
#
# # Đọc dữ liệu từ Band 4 và Band 5
# band4 = read_band(band4_path)
# band5 = read_band(band5_path)
#
# # Tính NDVI
# ndvi = (band5 - band4) / (band5 + band4)
#
# # Hiển thị NDVI
# plt.imshow(ndvi, cmap='RdYlGn')  # Sử dụng cmap để tạo màu sắc đẹp cho NDVI
# plt.colorbar()
# plt.title('NDVI Image')
# plt.show()
#
# # Lưu NDVI dưới dạng ảnh
# output_path = "ndvi_output.TIF"
# with rasterio.open(output_path, 'w', driver='GTiff', height=ndvi.shape[0], width=ndvi.shape[1],
#                    count=1, dtype='float32', crs='+proj=latlong', transform=rasterio.open(band4_path).transform) as dst:
#     dst.write(ndvi, 1)

# Đọc MTL.txt file
def read_mtl(file_path):
    # Đọc nội dung từ file .txt
    with open('D:\\ThuNghiem\\LC09_L1TP_125053_20240226_20240226_02_T1_MTL.txt', 'r') as file:
        lines = file.readlines()

    landsat_product_id = ""
    output_format = ""
    data_type_band_1_to_11_lst = []
    cloud_cover = 0
    cloud_cover_land = 0
    sun_elevation = 0
    map_projection = ""
    datum = ""
    utm_zone = 0
    grid_cell_size_panchromatic = 0
    grid_cell_size_reflective = 0
    grid_cell_size_thermal = 0
    corner_ul_lat_product = 0
    corner_ul_lon_product = 0
    corner_ur_lat_product = 0
    corner_ur_lon_product = 0
    corner_ll_lat_product = 0
    corner_ll_lon_product = 0
    corner_lr_lat_product = 0
    corner_lr_lon_product = 0
    radiance_mult_band_1_to_11_lst = []
    radiance_add_band_1_to_11_lst = []
    reflectance_mult_band = 0
    reflectance_add_band = 0
    k1_constant_band_10 = 0
    k2_constant_band_10 = 0
    k1_constant_band_11 = 0
    k2_constant_band_11 = 0

    for line in lines:
        if "LANDSAT_PRODUCT_ID" in line:
            landsat_product_id = line.split('=')[1].strip().strip('"')  # Tách giá trị từ chuỗi
        if "OUTPUT_FORMAT" in line:
            output_format = line.split('=')[1].strip().strip('"')
        if "DATA_TYPE_BAND_1 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_2 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_3 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_4 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_5 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_6 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_7 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_8 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_9 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_10 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "DATA_TYPE_BAND_11 =" in line:
            data_type_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "CLOUD_COVER =" in line:
            cloud_cover = line.split('=')[1].strip()
        if "CLOUD_COVER_LAND =" in line:
            cloud_cover_land = line.split('=')[1].strip()
        if "SUN_ELEVATION" in line:
            sun_elevation = line.split('=')[1].strip()
        if "MAP_PROJECTION" in line:
            map_projection = line.split('=')[1].strip().strip('"')
        if "DATUM" in line:
            datum = line.split('=')[1].strip().strip('"')
        if "UTM_ZONE" in line:
            utm_zone = line.split('=')[1].strip()
        if "GRID_CELL_SIZE_PANCHROMATIC" in line:
            grid_cell_size_panchromatic = line.split('=')[1].strip()
        if "GRID_CELL_SIZE_REFLECTIVE" in line:
            grid_cell_size_reflective = line.split('=')[1].strip()
        if "GRID_CELL_SIZE_THERMAL" in line:
            grid_cell_size_thermal = line.split('=')[1].strip()
        if "CORNER_UL_LAT_PRODUCT" in line:
            corner_ul_lat_product = line.split('=')[1].strip()
        if "CORNER_UL_LON_PRODUCT" in line:
            corner_ul_lon_product = line.split('=')[1].strip()
        if "CORNER_UR_LAT_PRODUCT" in line:
            corner_ur_lat_product = line.split('=')[1].strip()
        if "CORNER_UR_LON_PRODUCT" in line:
            corner_ur_lon_product = line.split('=')[1].strip()
        if "CORNER_LL_LAT_PRODUCT" in line:
            corner_ll_lat_product = line.split('=')[1].strip()
        if "CORNER_LL_LON_PRODUCT" in line:
            corner_ll_lon_product = line.split('=')[1].strip()
        if "CORNER_LR_LAT_PRODUCT" in line:
            corner_lr_lat_product = line.split('=')[1].strip()
        if "CORNER_LR_LON_PRODUCT" in line:
            corner_lr_lon_product = line.split('=')[1].strip()
        if "RADIANCE_MULT_BAND_1 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_2 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_3 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_4 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_5 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_6 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_7 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_8 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_9 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_10 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_MULT_BAND_11 =" in line:
            radiance_mult_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_1 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_2 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_3 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_4 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_5 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_6 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_7 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_8 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_9 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_10 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "RADIANCE_ADD_BAND_11 =" in line:
            radiance_add_band_1_to_11_lst.append(line.split('=')[1].strip().strip('"'))
        if "REFLECTANCE_MULT_BAND_1 =" in line:
            reflectance_mult_band = line.split('=')[1].strip().strip('"')
        if "REFLECTANCE_ADD_BAND_1 =" in line:
            reflectance_add_band = line.split('=')[1].strip().strip('"')
        if "K1_CONSTANT_BAND_10" in line:
            k1_constant_band_10 = line.split('=')[1].strip().strip('"')
        if "K2_CONSTANT_BAND_10" in line:
            k2_constant_band_10 = line.split('=')[1].strip().strip('"')
        if "K1_CONSTANT_BAND_11" in line:
            k1_constant_band_11 = line.split('=')[1].strip().strip('"')
        if "K2_CONSTANT_BAND_11" in line:
            k2_constant_band_11 = line.split('=')[1].strip().strip('"')

    return (landsat_product_id, output_format, data_type_band_1_to_11_lst, cloud_cover, cloud_cover_land, sun_elevation,
            map_projection, datum, utm_zone, grid_cell_size_panchromatic, grid_cell_size_reflective,
            grid_cell_size_thermal, corner_ul_lat_product, corner_ul_lon_product, corner_ur_lat_product,
            corner_ur_lon_product, corner_ll_lat_product, corner_ll_lon_product, corner_lr_lat_product,
            corner_lr_lon_product, radiance_mult_band_1_to_11_lst, radiance_add_band_1_to_11_lst, reflectance_mult_band,
            reflectance_add_band, k1_constant_band_10, k2_constant_band_10, k1_constant_band_11, k2_constant_band_11)


# Đọc band
def read_band(file_path):
    with rasterio.open(file_path) as src:
        band_dn = src.read(1)  # Đọc dữ liệu band đầu tiên
        band_profile = src.profile  # Lấy thông tin metadata
    return band_dn, band_profile





# Hiển thị band
def show_band(file_path):
    # Hiển thị NDVI
    plt.figure(figsize=(10, 6))
    plt.imshow(file_path, cmap='Blues')  # Màu sắc NDVI
    plt.colorbar(label='NDVI')
    plt.title('NDVI from Landsat 8/9')
    plt.axis('off')  # Tắt trục
    plt.show()





def main():
    # Đọc số liệu từ MTL file
    mtl_path = "D:\\ThuNghiem\\LC09_L1TP_125053_20240226_20240226_02_T1_MTL.txt"

    (landsat_product_id, output_format, data_type_band_1_to_11_lst, cloud_cover, cloud_cover_land,
     sun_elevation, map_projection, datum, utm_zone, grid_cell_size_panchromatic, grid_cell_size_reflective,
     grid_cell_size_thermal, corner_ul_lat_product, corner_ul_lon_product, corner_ur_lat_product, corner_ur_lon_product,
     corner_ll_lat_product, corner_ll_lon_product, corner_lr_lat_product, corner_lr_lon_product,
     radiance_mult_band_1_to_11_lst, radiance_add_band_1_to_11_lst, reflectance_mult_band, reflectance_add_band,
     k1_constant_band_10, k2_constant_band_10, k1_constant_band_11, k2_constant_band_11) = read_mtl(mtl_path)

    print("LANDSAT_PRODUCT_ID:", landsat_product_id)
    print("OUTPUT_FORMAT:", output_format)

    for index, string in enumerate(data_type_band_1_to_11_lst, start=1):
        print(f"DATA_TYPE_BAND_{index}={string}")

    print("CLOUD_COVER=", cloud_cover)
    print("CLOUD_COVER_LAND=", cloud_cover_land)
    print("SUN_ELEVATION=", sun_elevation)
    print("MAP_PROJECTION=", map_projection)
    print("DATUM=", datum)
    print("UTM_ZONE=", utm_zone)
    print("GRID_CELL_SIZE_PANCHROMATIC=", grid_cell_size_panchromatic)
    print("GRID_CELL_SIZE_REFLECTIVE=", grid_cell_size_reflective)
    print("GRID_CELL_SIZE_THERMAL=", grid_cell_size_thermal)
    print("CORNER_UL_LAT_PRODUCT=", corner_ul_lat_product)
    print("CORNER_UL_LON_PRODUCT=", corner_ul_lon_product)
    print("CORNER_UR_LAT_PRODUCT=", corner_ur_lat_product)
    print("CORNER_UR_LON_PRODUCT=", corner_ur_lon_product)
    print("CORNER_LL_LAT_PRODUCT=", corner_ll_lat_product)
    print("CORNER_LL_LON_PRODUCT=", corner_ll_lon_product)
    print("CORNER_LR_LAT_PRODUCT=", corner_lr_lat_product)
    print("CORNER_LR_LON_PRODUCT=", corner_lr_lon_product)

    for index, number in enumerate(radiance_mult_band_1_to_11_lst, start=1):
        print(f"RADIANCE_MULT_BAND_{index}={number}")

    for index, number in enumerate(radiance_add_band_1_to_11_lst, start=1):
        print(f"RADIANCE_ADD_BAND_{index}={number}")

    print("REFLECTANCE_MULT_BAND=", reflectance_mult_band)
    print("REFLECTANCE_ADD_BAND=", reflectance_add_band)

    print("K1_CONSTANT_BAND_10=", k1_constant_band_10)
    print("K2_CONSTANT_BAND_10=", k2_constant_band_10)
    print("K1_CONSTANT_BAND_11=", k1_constant_band_11)
    print("K2_CONSTANT_BAND_11=", k2_constant_band_11)

    # Đường dẫn tới ảnh Band 4 và Band 5
    band4_path = "D:\\ThuNghiem\\LC09_L1TP_125053_20240226_20240226_02_T1_B4.TIF"
    band5_path = "D:\\ThuNghiem\\LC09_L1TP_125053_20240226_20240226_02_T1_B5.TIF"

    # Tính TOA Radiance
    band4_dn, band4_profile = read_band(band4_path)



    band4_reflectance_mult_band4 = 2.0000E-05
    band4_reflectance_add_band4 = -0.1
    sun_elevation = float(sun_elevation)
    band4_toa_reflectance = calculate_toa_reflectance(band4_dn, band4_reflectance_mult_band4,
                                                      band4_reflectance_add_band4, sun_elevation)
    export(band4_toa_radiance,band4_path)
    export(band4_toa_reflectance, band4_path)

    # band5_dn, band5_profile = read_band(band5_path)
    # print(band4_profile)
    # show_band(band5_dn)


if __name__ == "__main__":
    main()
