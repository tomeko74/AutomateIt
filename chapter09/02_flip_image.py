from PIL import Image

# Get the image object
img = Image.open('beach_sunset.png')

# Rotate the image by 180 deg
img.rotate(180).save('beach_sunset180deg.jpg')

# Flip the images horizontally and vertically
img.transpose(Image.FLIP_LEFT_RIGHT).save('beach_sunset_horizontal_flip.png')
img.transpose(Image.FLIP_TOP_BOTTOM).save('beach_sunset_vertical_flip.png')
