import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    
    cv2.imshow('Camera',frame)
    
    k=cv2.waitKey(1)
    if k==32:
        fileName='MyImage.jpg'
        cv2.imwrite(fileName,frame)
        print('Image captured successfully...')
        break   