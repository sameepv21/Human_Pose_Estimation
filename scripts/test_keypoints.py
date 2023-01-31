import cv2
import numpy as np

# Load the image
image = cv2.imread("../data/valid/images/18519.jpg")

# Define the keypoints as a list of x, y tuples
keypoints = [
      [89.6, 95.55],
      [90.03495145631068, 94.5],
      [0.0, 0.0],
      [96.55922330097087, 93.1],
      [0.0, 0.0],
      [110.9126213592233, 100.44999999999999],
      [106.99805825242719, 87.14999999999999],
      [91.77475728155339, 118.64999999999999],
      [127.00582524271844, 86.1],
      [68.72233009708738, 120.74999999999999],
      [128.31067961165047, 97.64999999999999],
      [136.13980582524272, 114.8],
      [120.04660194174757, 107.1],
      [121.7864077669903, 134.75],
      [105.25825242718446, 129.15],
      [149.1883495145631, 119.35],
      [127.00582524271844, 119.35]
    ]

# Loop over the keypoints and draw a circle at each location
for x, y in keypoints:
    cv2.circle(image, (int(x), int(y)), 5, (0, 0, 255), -1)

# Display the image with the keypoints superimposed
cv2.imshow("Keypoints", image)
cv2.waitKey(0)
cv2.destroyAllWindows()