from PIL import Image, ImageDraw

new_color = (0, 0, 0)
size_x = 512
size_y = 200

new_image = Image.new("RGB", (size_x, size_y), new_color)
draw = ImageDraw.Draw(new_image)

for x in range(0, 512, 2):
    draw.line((x, 0, x, 200), fill=(x, 0, 0), width=2)

new_image.save('line.png', "PNG")