import cv2

#code to open webcam
cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img=cap.read()
    cv2.imshow("Face attendence",img)
    cv2.waitKey(1)