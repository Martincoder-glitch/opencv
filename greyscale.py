import cv2
s_d="C:/Users/MARTIN EGAHI OGWUCHE/Jetlearn/open cv/assets"
img=cv2.imread("pika.png")
cv2.imshow("old",img)
cv2.waitKey(0)
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("grey",grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
(row,col)=img.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i,j]=sum(img[i,j])*0.33
cv2.imshow("grey",img)
cv2.waitKey(0)
cv2.destroyAllWindows()