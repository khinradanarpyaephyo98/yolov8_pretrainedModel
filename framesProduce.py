import os
import cv2

count = 0
counter = 1

cap = cv2.VideoCapture("30s.mp4")
count = 0
counter += 1
success = True
while success:
    success,image = cap.read()
    if count%30 == 0 :
            cv2.imwrite( './TestData/frame%d.jpg'%count,image)
            print(f"The frame is extracted at count {count}s")
    count+=1
   