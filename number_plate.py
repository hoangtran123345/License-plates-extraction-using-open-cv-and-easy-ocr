import cv2
import numpy as np
import os

number_plates = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4,480)
areaMin = 500
count = 0

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = number_plates.detectMultiScale(imgGray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w*h
        if area > areaMin:
            cv2.rectangle(img,(x,y), (x+w,y+h),(255,0,0),3)
            cv2.putText(img, "License plate",(x,y-5), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

        imgRoi = img[y:y+h, x:x+w]
        cv2.imshow("Img Roi", imgRoi)


    cv2.imshow("Image Original", img)


    if cv2.waitKey(1) & 0xFF == ord("s"):
        filename = "scaned_img" + str(count) + ".jpg"
        filepath = os.path.join("plates", filename)
        while os.path.isfile(filepath):  # Kiểm tra nếu file đã tồn tại
            count += 1
            filename = "scaned_img" + str(count) + ".jpg"
            filepath = os.path.join("plates", filename)
        
        cv2.imwrite(filepath, imgRoi)
        cv2.rectangle(img, (0, 100), (240, 100), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate saved", (0, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1

    elif cv2.waitKey(1) & 0xFF == ord("q"):
        break


