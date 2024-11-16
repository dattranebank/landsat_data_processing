from matplotlib import pyplot as plt


# Hiển thị ảnh viễn thám
def show_remote_sentinel_image(remote_sensing_img,band_name):
    plt.imshow(remote_sensing_img, cmap='cividis')  # Sử dụng cmap để tạo màu sắc đẹp cho NDVI
    plt.colorbar()
    plt.title(band_name)
    plt.show()
