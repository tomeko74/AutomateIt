import imageio
from scipy.linalg import norm


# Method to compare two images and
# return the difference in pixels
def compare_images(img1, img2):
    diff = img1 - img2
    z_norm = norm(diff.ravel(), 0)
    return z_norm


# Read two images and get the reader objects
img1 = imageio.imread("beach_sunset.png").astype(float)
img2 = imageio.imread("pasted.jpg").astype(float)

# Actual comparison and return difference
z_norm = compare_images(img1, img2)
print("Pixel Difference:", z_norm)
