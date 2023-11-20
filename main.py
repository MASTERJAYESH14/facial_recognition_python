import cv2
import pickle
import face_recognition
import numpy as np
import cvzone 
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import  storage
import os
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionbu-default-rtdb.firebaseio.com",
    'storageBucket':"facerecognitionbu.appspot.com"})

bucket = storage.bucket()
#code to open webcam
cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

#loading the encoding file
print("Loading encoding file......................")

file = open("Encodings.p","rb")
encodelistwithids = pickle.load(file)
file.close()
encodeslistknown,studentidlist = encodelistwithids
#print(studentidlist)
print("Encodings file loaded succesfully............")
#importing the mode images into the list

imgBackground = cv2.imread('Resources/background.png')

folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))



mode = 0
counter = 0
while True:
    success, img=cap.read()

# resizing the image to make it 0ne-fourth of size for less computational power
    imgsmall = cv2.resize(img,(0,0), None, 0.25, 0.25)
#converting BGR TO RGB
    imgsmall=cv2.cvtColor(imgsmall, cv2.COLOR_BGR2RGB)

    facecurrentframe = face_recognition.face_locations(imgsmall)
    encodecurrentframe = face_recognition.face_encodings(imgsmall, facecurrentframe)
    
    imgBackground[162:162 + 480, 55:55 + 640] = img 
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode]
    if facecurrentframe:
        for encodeface, facelocation in zip(encodecurrentframe, facecurrentframe):
            matches = face_recognition.compare_faces(encodeslistknown, encodeface)
            facedistance= face_recognition.face_distance(encodeslistknown,encodeface)
            matchleastindex = np.argmin(facedistance)
            #print("Matchindex", matchleastindex)


            if matches[matchleastindex]== True:
                #print("Known face detected!!!!!!!!")
                #print("Studentid:", studentidlist[matchleastindex])
                y1,x2,x1,y2 = facelocation
                y1,x2,x1,y2 = y1*4,x2*4,x1*4,y2*4
                bbox = x1,y1,x2-x1,y2-y1
                img = cvzone.cornerRect(img,bbox,rt=0)
                id  = studentidlist[matchleastindex]

                if counter ==0:
                    cvzone.putTextRect(imgBackground,"Loading", (275,400))
                    cv2.imshow("Face Attendance",imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    mode = 1
                
        if counter != 0:


            if counter == 1:

                #get the data of student
                studentinfo = db.reference(f'students/{id}').get()

                #get picture of student
                blob = bucket.get_blob(f'images/{id}.jpg')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                studentimage = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                #update the data in database
                datetimeobject = datetime.strptime(studentinfo["Last_Attendance"],
                                                "%Y-%m-%d %H:%M:%S")
                secondselapsed = (datetime.now()-datetimeobject).total_seconds()

                if secondselapsed>30:
                    ref = db.reference(f'students/{id}')
                    studentinfo["Total_attendence"] +=1
                    ref.child("Total_attendence").set(studentinfo["Total_attendence"])
                    ref.child("Last_Attendance").set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    mode = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode]
            if mode !=3: 
                if 10<counter<20:
                    mode = 2
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode]

                if counter<=10:    
                    cv2.putText(imgBackground, str(studentinfo['Name']), (990,532),
                                cv2.FONT_HERSHEY_COMPLEX,1 ,(147,255,255), 1)
                    cv2.putText(imgBackground, str(studentinfo['Enrollment_No']), (990,575),
                                cv2.FONT_HERSHEY_COMPLEX,0.7 ,(255,255,255), 1)
                    
                    imgBackground[175:175+216 , 909:909+216] = studentimage
                
                counter  = counter+1
                
                if counter>=20:
                    counter=0
                    mode = 0
                    studentinfo= []
                    studentimage=[]
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[mode]

    else:
        mode=0
        counter=0

    cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance",imgBackground)
    cv2.waitKey(10)