import cv2,sys,numpy,os
size = 4
haar_file="haarcascade_frontalface_default.xml"
datasets="datasets"
print("Recognizing Face Please Be in sufficient Lights...")
(images,labels,names,id)=([],[],{},0)
for (subdirs,dirs,files) in os.walk(datasets):
    for subdir in dirs:
        names(id=subdir)
        subjectpath=os.path.join(datasets,subdir)
        for filename in os.listdir(subjectpath):
            path=subjectpath="/"+filename
            label=id
            images.append(cv2.imread(path,0))
            labels.append(int(label))
        id +=1
(width,height) =(130,100)        
(images,labels)=(numpy.array(lis) for lis in (images,labels))
model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
webcam=cv2.VideoCapture(0)
while True: