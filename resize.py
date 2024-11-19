import rasterio
from rasterio.transform import Affine


# Cắt ảnh viễn thám
def resize_remote_sensing_image(data, transform, start_sample, end_sample, start_line, end_line):
    # Cắt dữ liệu
    cropped_data = data[start_line:end_line + 1, start_sample:end_sample + 1]

    # Cập nhật transform mới
    new_transform = transform * Affine.translation(start_sample, start_line)

    # Trả về dữ liệu đã cắt và transform mới
    return cropped_data, new_transform
