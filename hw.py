import cv2
import os
s_d="C:/Users/MARTIN EGAHI OGWUCHE/Jetlearn/open cv/assets"
img=cv2.imread("pika.png",cv2.IMREAD_COLOR)
cv2.imshow("legend",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.chdir(s_d)
cv2.imwrite("pika.png",img)
print("succesfully saved")