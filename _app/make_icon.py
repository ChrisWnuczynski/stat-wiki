"""Draw the wiki's desktop icon (wiki.ico). Run once: python _app/make_icon.py"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SIZE = 256

image = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)
draw.rounded_rectangle((8, 8, SIZE - 8, SIZE - 8), radius=44, fill=(51, 102, 204, 255))
font = ImageFont.truetype("georgia.ttf", 190)
box = draw.textbbox((0, 0), "Σ", font=font)
x = (SIZE - (box[2] - box[0])) / 2 - box[0]
y = (SIZE - (box[3] - box[1])) / 2 - box[1]
draw.text((x, y), "Σ", font=font, fill=(255, 255, 255, 255))
image.save(HERE / "wiki.ico", sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print(HERE / "wiki.ico")
