from resize import *
from read import *
from show import *
from calculate import *
from export import *


def main():
    # Đọc số liệu từ MTL file
    mtl_path = "D:\\VQG_TramChim\\02_landsat_raw_data\\MuaKho\\LC09_L1TP_125053_20240226_20240226_02_T1_MTL.txt"
    (landsat_product_id, output_format, data_type_band_1_to_11_lst, cloud_cover, cloud_cover_land,
     sun_elevation, map_projection, datum, utm_zone, grid_cell_size_panchromatic, grid_cell_size_reflective,
     grid_cell_size_thermal, corner_ul_lat_product, corner_ul_lon_product, corner_ur_lat_product, corner_ur_lon_product,
     corner_ll_lat_product, corner_ll_lon_product, corner_lr_lat_product, corner_lr_lon_product,
     radiance_mult_band_1_to_11_lst, radiance_add_band_1_to_11_lst, reflectance_mult_band, reflectance_add_band,
     k1_constant_band_10, k2_constant_band_10, k1_constant_band_11, k2_constant_band_11) = read_mtl(mtl_path)

    # Xuất thông số ảnh viễn thám Landsat
    landsat_metadata_path = 'D:\\VQG_TramChim\\02_landsat_raw_data\MuaKho\\TramChim_MuaKho_2024_MTL.txt'
    export_landsat_metadata(landsat_product_id, output_format, data_type_band_1_to_11_lst, cloud_cover,
                            cloud_cover_land, sun_elevation, map_projection, datum, utm_zone,
                            grid_cell_size_panchromatic, grid_cell_size_reflective, grid_cell_size_thermal,
                            corner_ul_lat_product, corner_ul_lon_product, corner_ur_lat_product,
                            corner_ur_lon_product, corner_ll_lat_product, corner_ll_lon_product, corner_lr_lat_product,
                            corner_lr_lon_product, radiance_mult_band_1_to_11_lst, radiance_add_band_1_to_11_lst,
                            reflectance_mult_band, reflectance_add_band, k1_constant_band_10, k2_constant_band_10,
                            k1_constant_band_11, k2_constant_band_11, landsat_metadata_path)

    # Đường dẫn tới Band 2, Band 3, Band 4, Band 5 và Band 10
    band2_path = "D:\\VQG_TramChim\\02_landsat_raw_data\MuaKho\\LC09_L1TP_125053_20240226_20240226_02_T1_B2.TIF"
    band3_path = "D:\\VQG_TramChim\\02_landsat_raw_data\MuaKho\\LC09_L1TP_125053_20240226_20240226_02_T1_B3.TIF"
    band4_path = "D:\\VQG_TramChim\\02_landsat_raw_data\MuaKho\\LC09_L1TP_125053_20240226_20240226_02_T1_B4.TIF"
    band5_path = "D:\\VQG_TramChim\\02_landsat_raw_data\MuaKho\\LC09_L1TP_125053_20240226_20240226_02_T1_B5.TIF"
    band10_path = "D:\\VQG_TramChim\\02_landsat_raw_data\MuaKho\\LC09_L1TP_125053_20240226_20240226_02_T1_B10.TIF"

    # Đọc từng band
    band2_dn, band2_transform = read_band(band2_path)
    band3_dn, band3_transform = read_band(band3_path)
    band4_dn, band4_transform = read_band(band4_path)
    band5_dn, band5_transform = read_band(band5_path)
    band10_dn, band10_transform = read_band(band10_path)

    # Cắt ảnh viễn thám
    band2_dn, band2_transform = resize_remote_sensing_image(band2_dn, band2_transform,
                                                            start_sample=1413, end_sample=2912,
                                                            start_line=966, end_line=2465)
    band3_dn, band3_transform = resize_remote_sensing_image(band3_dn, band3_transform,
                                                            start_sample=1413, end_sample=2912,
                                                            start_line=966, end_line=2465)
    band4_dn, band4_transform = resize_remote_sensing_image(band4_dn, band4_transform,
                                                            start_sample=1413, end_sample=2912,
                                                            start_line=966, end_line=2465)
    band5_dn, band5_transform = resize_remote_sensing_image(band5_dn, band5_transform,
                                                            start_sample=1413, end_sample=2912,
                                                            start_line=966, end_line=2465)
    band10_dn, band10_transform = resize_remote_sensing_image(band10_dn, band10_transform,
                                                              start_sample=1413, end_sample=2912,
                                                              start_line=966, end_line=2465)

    # Hiển thị band
    show_remote_sensing_image(band2_dn, "Band 2")
    show_remote_sensing_image(band3_dn, "Band 3")
    show_remote_sensing_image(band4_dn, "Band 4")
    show_remote_sensing_image(band5_dn, "Band 5")
    show_remote_sensing_image(band10_dn, "Band 10")

    # Tính TOA Radiance
    band10_toa_radiance = calculate_toa_radiance(band10_dn, radiance_mult_band_1_to_11_lst[9],
                                                 radiance_add_band_1_to_11_lst[9])
    # Tính Surface Reflectance
    band2_surface_reflectance = calculate_surface_reflectance(band2_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    band3_surface_reflectance = calculate_surface_reflectance(band3_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    band4_surface_reflectance = calculate_surface_reflectance(band4_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    band5_surface_reflectance = calculate_surface_reflectance(band5_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)

    # Tính NDVI, NDW
    ndvi = calculate_ndvi(band4_surface_reflectance, band5_surface_reflectance)
    ndwi = calculate_ndwi(band3_surface_reflectance, band5_surface_reflectance)

    # Tính TOA Brightness Temperature
    band10_toa_bt = calculate_toa_brightness_temperature(band10_toa_radiance, k1_constant_band_10, k2_constant_band_10)

    # Tính Land Surface Emissivity (LSE)
    lse = calculate_lse(ndvi)

    # Tính Land Surface Temperature (LST)
    lst = calculate_lst(band10_toa_bt, lse)

    # Hiển thị tổ hợp màu (B432)
    rgb_image = np.stack([band4_surface_reflectance, band3_surface_reflectance, band2_surface_reflectance], axis=-1)
    plt.imshow(rgb_image / rgb_image.max())  # Chuẩn hóa về 0-1
    plt.title("B432 Composite")
    plt.axis('off')
    plt.show()

    # Gọi hàm xuất ảnh
    show_remote_sensing_image(band10_dn, "Band 10")
    export_b432(band2_surface_reflectance, band3_surface_reflectance, band4_surface_reflectance,
                band2_transform, "B432_Python.TIF")

    ## Xuất TOA Radiance
    export_toa_radiance(band10_toa_radiance, band10_transform, "B10_TOA_Radiance_Python.TIF")

    # Xuất Surface Reflectance
    export_surface_reflectance(band2_surface_reflectance, band2_transform, "B2_Surface_Reflectance_Python.TIF")
    export_surface_reflectance(band3_surface_reflectance, band3_transform, "B3_Surface_Reflectance_Python.TIF")
    export_surface_reflectance(band4_surface_reflectance, band4_transform, "B4_Surface_Reflectance_Python.TIF")
    export_surface_reflectance(band5_surface_reflectance, band5_transform, "B5_Surface_Reflectance_Python.TIF")

    # Xuất NDVI, NDWI
    export_ndvi(ndvi, band3_transform, "NDVI_Python.TIF")
    export_ndwi(ndwi, band3_transform, "NDWI_Python.TIF")

    # Xuất LST
    export_lst(lst,band10_transform,"LST_Python.TIF")


if __name__ == "__main__":
    main()
