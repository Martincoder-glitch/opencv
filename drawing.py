import cv2
image=cv2.imread("pika.png")
startpoint=(0,0)
endpoint=(250,250)
color=(50,20,132)
Thickness=9
image=cv2.line(image,startpoint,endpoint,color,Thickness)
cv2.imshow("pika",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
