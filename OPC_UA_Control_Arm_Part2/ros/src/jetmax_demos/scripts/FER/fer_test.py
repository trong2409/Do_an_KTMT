import cv2
import fer

raw_img = cv2.imread('FER/images/2.jpg')
ep = fer(raw_img)

print("The Expression is %s" %ep)


