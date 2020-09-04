import cv2
import numpy as np
def nothing(x):
    pass
def draw_circle(event, x, y, flags, param):
    global r, g, b, rad, ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),rad,(b,g,r),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),rad,(b,g,r),-1)
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('Paint')
cv2.putText(img, 'Press C to clear',(5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255),1)
cv2.createTrackbar('Red', 'Paint',0,255,nothing)
cv2.createTrackbar('Green', 'Paint',0,255,nothing)
cv2.createTrackbar('Blue', 'Paint',0,255,nothing)
cv2.createTrackbar('Radius', 'Paint',5,10,nothing)
while(1):
    r = cv2.getTrackbarPos('Red', 'Paint')
    g = cv2.getTrackbarPos('Green', 'Paint')
    b = cv2.getTrackbarPos('Blue', 'Paint')
    rad = cv2.getTrackbarPos('Radius', 'Paint')

    cv2.setMouseCallback('Paint',draw_circle)
    cv2.imshow('Paint', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        img = np.zeros((300,512,3), np.uint8)
        cv2.imshow('Paint', img)
        cv2.putText(img, 'Press C to clear',(5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
        (255,255,255), 1, cv2.LINE_AA)
cv2.destroyAllWindows()