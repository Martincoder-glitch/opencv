import cv2
image=cv2.imread("pika.png")
centercordinate=(50,30) 
radius=20
color=(30,20,5)     
Thickness=-1
image=cv2.circle(image,centercordinate,radius,color,Thickness)
cv2.imshow("pika",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
