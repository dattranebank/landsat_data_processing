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

    # Đường dẫn tới Band 3, Band 4, Band 5 và Band 10
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
    # Xử lý band 2
    ## Hiển thị band 2
    show_remote_sensing_image(band2_dn, "Band 2")
    ## Tính Surface Reflectance
    band2_surface_reflectance = calculate_surface_reflectance(band2_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    ## Xuất Surface Reflectance
    export_surface_reflectance(band2_surface_reflectance, band2_transform, "Band2_TOA_Reflectance_Python.TIF")

    # Xử lý band 3
    ## Hiển thị band 3
    show_remote_sensing_image(band3_dn, "Band 3")
    ## Tính Surface Reflectance
    band3_surface_reflectance = calculate_surface_reflectance(band3_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    ## Xuất Surface Reflectance
    export_surface_reflectance(band3_surface_reflectance, band3_transform, "Band3_TOA_Reflectance_Python.TIF")

    # Xử lý band 4
    ## Hiển thị band 4
    show_remote_sensing_image(band4_dn, "Band 4")
    ## Tính Surface Reflectance
    band4_surface_reflectance = calculate_surface_reflectance(band4_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    ## Xuất Surface Reflectance
    export_surface_reflectance(band4_surface_reflectance, band4_transform, "Band4_TOA_Reflectance_Python.TIF")

    # Xử lý band 5
    ## Hiển thị band 5
    show_remote_sensing_image(band5_dn, "Band 5")
    ## Tính Surface Reflectance
    band5_surface_reflectance = calculate_surface_reflectance(band5_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    ## Xuất Surface Reflectance
    export_surface_reflectance(band5_surface_reflectance, band5_transform, "Band5_TOA_Reflectance_Python.TIF")

    # Xử lý band 10
    ## Hiển thị band 10
    show_remote_sensing_image(band10_dn, "Band 10")
    ## Tính TOA Radiance
    band10_toa_radiance = calculate_toa_radiance(band10_dn, radiance_mult_band_1_to_11_lst[9],
                                                 radiance_add_band_1_to_11_lst[9])

    ## Xuất TOA Radiance
    export_toa_radiance(band10_toa_radiance, band10_transform, "Band10_TOA_Radiance_Python.TIF")

    # # Tính BT
    # # Tính E
    # # Tính LST
    #
    # # Tính NDVI, NDWI, LST
    # ndvi = calculate_ndvi(band4_surface_reflectance, band5_surface_reflectance)
    # ndwi = calculate_ndwi(band3_surface_reflectance, band5_surface_reflectance)
    # # Xuất NDVI, NDWI, LST
    # export_ndvi(ndvi, band3_transform, "NDVI_Python.TIF")
    # export_ndwi(ndwi, band3_transform, "NDWI_Python.TIF")


if __name__ == "__main__":
    main()
