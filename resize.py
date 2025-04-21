import numpy as np
import rasterio
from rasterio.mask import mask
from rasterio.transform import Affine
import geopandas as gpd

# Cắt ảnh viễn thám
def resize_remote_sensing_image(data, transform, start_sample, end_sample, start_line, end_line):
    # Cắt dữ liệu
    cropped_data = data[start_line:end_line + 1, start_sample:end_sample + 1]

    # Cập nhật transform mới
    new_transform = transform * Affine.translation(start_sample, start_line)

    # Trả về dữ liệu đã cắt và transform mới
    return cropped_data, new_transform


def cut_image_by_polygon(raster_path, shapefile_path):
    # Đọc polygon
    shapes = gpd.read_file(shapefile_path)
    geometries = [feature["geometry"] for feature in shapes.__geo_interface__["features"]]

    # Mở raster từ đường dẫn
    with rasterio.open(raster_path) as src:
        out_image, out_transform = mask(src, geometries, crop=True)
        out_meta = src.meta

    return out_image[0], out_transform  # out_image là 3D (bands, height, width) → lấy band[0]