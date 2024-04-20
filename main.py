import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('assets/dog.jpg')

kernel = np.array(
    [[-1, 0, 1],
     [-2, 0, 2],
     [-1, 0, 1]]
)

result = cv2.filter2D(image, -1, kernel)

plt.imshow(result, cmap='gray')
plt.show()