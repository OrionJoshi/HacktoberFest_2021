import cv2
import numpy as np
from matplotlib import pyplot as plt

def pass_fn():
    pass

cap = cv2.VideoCapture(0)
# img = cv2.imread('selfie.JPG',cv2.IMREAD_GRAYSCALE)
# canny = cv2.Canny(img,100,200)
cv2.namedWindow('Tracking the threshold')
cv2.createTrackbar("lower th",'Tracking the threshold',0,500,pass_fn)
cv2.createTrackbar("upper th",'Tracking the threshold',0,500,pass_fn)

# titles = ['image','canny']
# images = [img,canny]

#for i in range(2):
#    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])

while True:
    ret,frame = cap.read()
    if ret == False:
        continue
    l_value = cv2.getTrackbarPos('lower th','Tracking the threshold')
    u_value = cv2.getTrackbarPos('upper th','Tracking the threshold')
    canny = cv2.Canny(frame, l_value, u_value)
    cv2.imshow('frame',frame)
    cv2.imshow('canny',canny)
    k = cv2.waitKey(1)&0xff
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()