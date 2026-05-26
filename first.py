import numpy as np
import cv2

#print(cv2.imread("image.jpg", cv2.IMREAD_COLOR))
#print(cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE))
#print(cv2.imread("image.jpg", cv2.IMREAD_UNCHANGED))

img1 = cv2.imread("image.jpg")
#print(img1.shape)
#print(img1.dtype)
#print(img1.size)

cv2.imshow('Window', img1)

while True:
    key = cv2.waitKey(0)
    if key == ord('s'): #Converts 's' to ASCII character
        break


print(cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY))

b,g,r = cv2.split(img1) #passes tuple of three arrays #colours are split

cv2.imshow('Blue', b)
key = cv2.waitKey(0)
if key == ord('b'):
    cv2.destroyWindow('Blue')

cv2.imshow('Green', g)
key = cv2.waitKey(0)
if key == ord('g'):
    cv2.destroyWindow('Green')

cv2.imshow('Red', r)
key = cv2.waitKey(0)
if key == ord('r'):
    cv2.destroyWindow('Red')

x=cv2.merge([b,r,g])
cv2.imshow('merged',x)
cv2.waitKey(0)

print(np.array_equal(img1, x))
print(np.array_equal(img1, cv2.merge([b,g,r])))

