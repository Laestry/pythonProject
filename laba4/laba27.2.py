from PIL import Image


def image_filter(pixels, i, j):
    r = px[j, j][0]
    g = px[i, j][1] + 100
    b = px[i, j][2] - 100
    return r, g, b


image = Image.open("Portada-1-1200x675.jpg")
px = image.load()
x, y = image.size

for n in range(x):
    for m in range(y):
        px[n, m] = (image_filter(px, n, m))

image.save('filter.bmp', 'BMP')
