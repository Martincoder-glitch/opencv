import cv2 
import numpy as np
import time 
print (cv2.__version__)

raw_video = cv2.VideoCapture("video.mp4")

time.sleep(1)
count= 0
background = 0
for i in range(60):
    return_val,background = raw_video.read()
    if return_val == False:
        continue
while(raw_video.isOpened()):
    return_val,img = raw_video.read()
    if not return_val:
        break
    count += 1
    img = np.flip(img,axis=1)
    hsv=cv2.cytcolor(img,cv2.COLOR_BGR2HSV)
    lower_red =np.array([100,40,40])
    upper_red = np.array([100,255,255])

    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask1 = mask1 + mask2
    
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,mask1 = cv2.dillate(mask1,np.ones((3,3),np.unit)))
