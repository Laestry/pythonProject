from PIL import Image


def make_preview(size, n_colors):
    image = Image.open("Portada-1-1200x675.jpg")
    image = image.resize(size)
    image = image.quantize(n_colors)
    image.save('res.bmp', 'BMP')


make_preview((100, 100), 200)
