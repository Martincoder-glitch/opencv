import cv2
image=cv2.imread("Ronaldo.jpg")
Thickness=-1
startpoint=(0,0)
endpoint=(250,250)
color=(200,50,30)
image=cv2.rectangle(image,startpoint,endpoint,color,Thickness)
cv2.imshow("ronaldo",image)
cv2.waitKey(0)
cv2.destroyAllWindows()