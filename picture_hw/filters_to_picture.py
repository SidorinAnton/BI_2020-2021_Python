import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import numpy as np

# Open image
path = "The_witcher.jpg"
img = plt.imread(path)

print(img.shape)  # Size 1200 (height), 1920 (width), 3 (RGB)


# 1. Cut off the image to the right
plt.imshow(img[:, 500:])
plt.axis("off")
plt.savefig("1.The_witcher_cut.jpg")
plt.close()


# 2. Negative
img = plt.imread(path)
img = 1 - img
plt.imshow(img)
plt.axis("off")
plt.savefig("2.The_witcher_negative.jpg")
plt.close()


# 3. Grayscale convertion
# img = plt.imread(path)
gray_img = Image.open(path).convert("L")
gray_img.save("3.The_witcher_grayscale.jpg", "JPEG")
plt.close()


# 4. Blur
pil_img = Image.open(path)
blur_img = pil_img.filter(ImageFilter.BLUR)
blur_img.save("4.The_witcher_blur.jpg", "JPEG")


# 5. Contour
pil_img = Image.open(path)
contour_img = pil_img.filter(ImageFilter.CONTOUR)
contour_img.save("5.The_witcher_contour.jpg", "JPEG")

