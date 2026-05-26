import numpy as np
import cv2
import keyboard

#print(cv2.imread("image.jpg", cv2.IMREAD_COLOR))
#print(cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE))
#print(cv2.imread("image.jpg", cv2.IMREAD_UNCHANGED))

img1 = cv2.imread("image.jpg")
#print(img1.shape)
#print(img1.dtype)
#print(img1.size)

cv2.imshow('Window', img1)

cv2.waitKey(0)
while True:
    if keyboard.is_pressed('s'): #to use letters as escape character to exit window
        cv2.waitKey(1)
        break


print(cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY))

b,g,r = cv2.split(img1) #passes tuple of three arrays #colours are split

cv2.imshow('Blue', b)
cv2.waitKey('b')
cv2.imshow('Green', g)
cv2.waitKey('g')
cv2.imshow('Red', r)
cv2.waitKey('r')

