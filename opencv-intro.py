import cv2
image=cv2.imread("assets\ghost.png")
cv2.imshow("screen1",image)
cv2.waitKey(0)
image=cv2.imread("assets\ghost.png",0)
cv2.imshow("screen1",image)
cv2.waitKey(0)
cv2.imwrite("BlackWhite.png",image)
print("Successfuly Saved")