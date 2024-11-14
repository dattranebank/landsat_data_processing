import rasterio

# Xuất ảnh đã tính TOA Radiance
def export(toa_radiance, band4_path):
    output_path = "band4_output.TIF"
    with rasterio.open(output_path, 'w', driver='GTiff', height=toa_radiance.shape[0],
                       width=toa_radiance.shape[1],
                       count=1, dtype='float32', crs='+proj=latlong',
                       transform=rasterio.open(band4_path).transform) as dst:
        dst.write(toa_radiance, 1)