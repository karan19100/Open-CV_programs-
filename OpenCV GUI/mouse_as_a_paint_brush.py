import cv2
import numpy as np
def draw_circle(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True: cv2.circle(img,(x,y),9,(255,255,255),-1)
    elif event == cv2.EVENT_LBUTTONUP: 
        drawing = False 
        cv2.circle(img,(x,y),9,(255,255,255),-1)
drawing = False
img = np.zeros((300,512,3), np.uint8) 
cv2.namedWindow('Paint')

while(1):
    cv2.setMouseCallback('Paint',draw_circle) 
    cv2.imshow('Paint', img)
    if cv2.waitKey(1) & 0xff == 27:
        break 
cv2.destroyAllWindows()





