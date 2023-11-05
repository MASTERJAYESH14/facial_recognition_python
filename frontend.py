import cv2
import os


cap = cv2.VideoCapture(0)
cap.set(3, 590)
cap.set(4, 1004)

imgBackground = cv2.imread('Resources/background.png')

folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))



while True:
    success, img = cap.read()

    
    img = cv2.resize(img, (419, 422))
    


    imgBackground[81:81+422, 103:103+419] = img
   
    

    cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
