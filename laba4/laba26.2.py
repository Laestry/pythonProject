from PIL import Image, ImageDraw


def create_chess(n, s):
    new_color = (255, 255, 255)
    new_image = Image.new("RGB", (s*n, s*n), new_color)
    draw = ImageDraw.Draw(new_image)

    f = True

    for x in range(n):
        for y in range(n):
            if f:
                draw.rectangle((x*s, y*s, x*s+s, y*s+s), fill=(0, 0, 0), width=1)

            f = not f

        f = not f

    new_image.save("bord.png", "PNG")


create_chess(5000, 1)
