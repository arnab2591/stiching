import cv2,numpy as np
import panorama

import imutils
import cv2

# construct the argument parse and parse the arguments

# load the two images and resize them to have a width of 400 pixels
# (for faster proces
imageB = cv2.imread("scottsdale_left_01.png")
imageA = cv2.imread('scottsdale_right_01.png')

imageA = imutils.rotate(imutils.resize(imageA, width=400),0)
imageB = imutils.rotate(imutils.resize(imageB, width=400),0)
# stitch the images together to create a panorama
stitcher = panorama.Stitcher()
print(stitcher)
result, vis = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
# print(result)
result = imutils.rotate(result,0)
cv2.imshow("Result", result)
cv2.waitKey(0)
