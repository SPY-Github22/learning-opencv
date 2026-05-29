import numpy as np
import cv2

#print(cv2.imread("image.jpg", cv2.IMREAD_COLOR))
#print(cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE))
#print(cv2.imread("image.jpg", cv2.IMREAD_UNCHANGED))

img1 = cv2.imread("image.jpg")
#print(img1.shape)
#print(img1.dtype)
#print(img1.size)



canvas = img1.copy()


import cv2

cap = cv2.VideoCapture(0)   # 0 = first webcam

if not cap.isOpened():
    print('Camera not found')
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break              # stream ended or camera lost

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break              # press q to quit


fps    = cap.get(cv2.CAP_PROP_FPS)
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f'FPS: {fps}, Size: {width}x{height}')

cap.release()
cv2.destroyAllWindows()


import cv2
import time

cap = cv2.VideoCapture(0)
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    curr_time = time.time()
    delta = curr_time - prev_time
    fps = 1.0 / delta           # actual FPS this frame
    prev_time = curr_time

    cv2.putText(
        frame,
        text=f'FPS: {fps:.1f}',
        org=(10, 30),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.0,
        color=(0, 255, 0),
        thickness=2,
        lineType=cv2.LINE_AA
    )

    cv2.imshow('Live Feed', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


cv2.putText(
    canvas,
    text='Hello OpenCV',
    org=(50, 50),              # bottom-left of text
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1.0,
    color=(255, 255, 255),    # white in BGR
    thickness=2,
    lineType=cv2.LINE_AA        # anti-aliased
)

cv2.imshow('Text', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# rectangle: top-left corner, bottom-right corner
cv2.rectangle(canvas, (50, 50), (200, 150), (0, 255, 0), thickness=2)

# circle: center, radius. thickness=-1 fills it
cv2.circle(canvas, (300, 100), radius=50, color=(255, 0, 0), thickness=-1)

# line: start point, end point
cv2.line(canvas, (0, 0), (400, 300), (0, 0, 255), thickness=3)

cv2.imshow('Shapes', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()


# this is a VIEW — shares memory with img
crop_view = img1[50:200, 100:400]
crop_view[0, 0] = [0, 0, 255]  # modifies img too!

# this is a COPY — independent
crop_copy = img1[50:200, 100:400].copy()
crop_copy[0, 0] = [0, 0, 255]  # does NOT modify img

cv2.imshow('Crop', crop_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

# flipCode: 0=vertical, 1=horizontal, -1=both
flip_v  = cv2.flip(img1, 0)
flip_h  = cv2.flip(img1, 1)
flip_both = cv2.flip(img1, -1)

cv2.imshow('Vertical flip', flip_v)
cv2.imshow('Horizontal flip', flip_h)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('Window', img1)

while True:
    key = cv2.waitKey(0)
    if key == ord('s'): #Converts 's' to ASCII character
        cv2.destroyWindow('Window')
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

resized = cv2.resize(img1, (32, 24), interpolation = cv2.INTER_LINEAR)
half = cv2.resize(img1, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)
big_nn = cv2.resize(img1, None, fx=4, fy=4, interpolation = cv2.INTER_NEAREST)
big_li = cv2.resize(img1, None, fx=4, fy=4, interpolation = cv2.INTER_LINEAR)

cv2.imshow('Nearest', big_nn)
cv2.imshow('Linear', big_li)
cv2.waitKey(0)
cv2.destroyAllWindows()