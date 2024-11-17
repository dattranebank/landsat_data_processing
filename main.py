from resize import *
from read import *
from show import *
from calculate import *
from export import *


def main():
    # Đọc số liệu từ MTL file
    mtl_path = "D:\\ThuNghiem\\LC09_L1TP_125053_20240226_20240226_02_T1_MTL.txt"

    (landsat_product_id, output_format, data_type_band_1_to_11_lst, cloud_cover, cloud_cover_land,
     sun_elevation, map_projection, datum, utm_zone, grid_cell_size_panchromatic, grid_cell_size_reflective,
     grid_cell_size_thermal, corner_ul_lat_product, corner_ul_lon_product, corner_ur_lat_product, corner_ur_lon_product,
     corner_ll_lat_product, corner_ll_lon_product, corner_lr_lat_product, corner_lr_lon_product,
     radiance_mult_band_1_to_11_lst, radiance_add_band_1_to_11_lst, reflectance_mult_band, reflectance_add_band,
     k1_constant_band_10, k2_constant_band_10, k1_constant_band_11, k2_constant_band_11) = read_mtl(mtl_path)

    # Đường dẫn tới Band 3, Band 4 và Band 5
    band3_path = "D:\\ThuNghiem\\1. Origin\\LC09_L1TP_125053_20240226_20240226_02_T1_B3.TIF"
    band4_path = "D:\\ThuNghiem\\1. Origin\\LC09_L1TP_125053_20240226_20240226_02_T1_B4.TIF"
    band5_path = "D:\\ThuNghiem\\1. Origin\\LC09_L1TP_125053_20240226_20240226_02_T1_B5.TIF"

    # Đọc từng band
    band3_dn, band3_transform = read_band(band3_path)
    band4_dn, band4_transform = read_band(band4_path)
    band5_dn, band5_transform = read_band(band5_path)

    # Cắt ảnh viễn thám
    band3_dn, band3_transform = resize_remote_sensing_image(band3_dn, band3_transform,
                                                            start_sample=3000, end_sample=6000,
                                                            start_line=3000, end_line=6000)
    band4_dn, band4_transform = resize_remote_sensing_image(band4_dn, band4_transform,
                                                            start_sample=3000, end_sample=6000,
                                                            start_line=3000, end_line=6000)
    band5_dn, band5_transform = resize_remote_sensing_image(band5_dn, band5_transform,
                                                            start_sample=3000, end_sample=6000,
                                                            start_line=3000, end_line=6000)

    # Xử lý band 3
    ## Hiển thị band 3
    show_remote_sensing_image(band3_dn, "Band 3")
    ## Tính TOA Radiance
    band3_toa_radiance = calculate_toa_radiance(band3_dn, radiance_mult_band_1_to_11_lst[2],
                                                radiance_add_band_1_to_11_lst[2])
    ## Tính Surface Reflectance
    band3_surface_reflectance = calculate_surface_reflectance(band3_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    ## Xuất TOA Radiance
    # export_toa_radiance(band3_toa_radiance, band3_transform, "band5_TOA_Radiance_Python.TIF")
    ## Xuất Surface Reflectance
    export_surface_reflectance(band3_surface_reflectance, band3_transform, "band3_TOA_Reflectance_Python.TIF")

    # Xử lý band 4
    ## Hiển thị band 4
    show_remote_sensing_image(band4_dn, "Band 4")
    ## Tính TOA Radiance
    band4_toa_radiance = calculate_toa_radiance(band4_dn, radiance_mult_band_1_to_11_lst[3],
                                                radiance_add_band_1_to_11_lst[3])
    ## Tính Surface Reflectance
    band4_surface_reflectance = calculate_surface_reflectance(band4_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    ## Xuất TOA Reflectance
    export_toa_radiance(band4_toa_radiance, band4_transform, "band4_TOA_Radiance_Python.TIF")
    ## Xuất Surface Reflectance
    export_surface_reflectance(band4_surface_reflectance, band4_transform, "band4_TOA_Reflectance_Python.TIF")

    # Xử lý band 5
    ## Hiển thị band 5
    show_remote_sensing_image(band5_dn, "Band 5")
    ## Tính TOA Radiance
    band5_toa_radiance = calculate_toa_radiance(band5_dn, radiance_mult_band_1_to_11_lst[4],
                                                radiance_add_band_1_to_11_lst[4])
    ## Tính Surface Reflectance
    band5_surface_reflectance = calculate_surface_reflectance(band5_dn, reflectance_mult_band,
                                                              reflectance_add_band, sun_elevation)
    ## Xuất TOA Reflectance
    export_toa_radiance(band5_toa_radiance, band5_transform, "band5_TOA_Radiance_Python.TIF")
    ## Xuất Surface Reflectance
    export_surface_reflectance(band5_surface_reflectance, band5_transform, "band5_TOA_Reflectance_Python.TIF")

    # Tính NDVI, NDWI, LST
    ndvi = calculate_ndvi(band4_surface_reflectance, band5_surface_reflectance)
    ndwi = calculate_ndwi(band3_surface_reflectance, band5_surface_reflectance)
    # Xuất NDVI, NDWI, LST
    export_ndvi(ndvi, band3_transform, "NDVI_Python.TIF")
    export_ndwi(ndwi, band3_transform, "NDWI_Python.TIF")


if __name__ == "__main__":
    main()
