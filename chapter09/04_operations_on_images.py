# Paste image on other image
from PIL import Image
img = Image.open('sunset-crop.jpg')
pasteImg = Image.open('beach_sunset.png')
pasteImg.paste(img, (0,0))
pasteImg.save('pasted.jpg')
"""
# Watermark images
from wand.image import Image

with Image(filename='beach_sunset.png') as background:
  with Image(filename='watermark.png') as watermark:
    background.watermark(image=watermark, transparency=0.25, left=560, top=300)
    background.save(filename='result.jpg')
"""