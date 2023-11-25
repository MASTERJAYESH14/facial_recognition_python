import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
from firebase_admin import  storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognitionbu-default-rtdb.firebaseio.com",
    'storageBucket':"facerecognitionbu.appspot.com"})


folderpath = 'images'
pathlist = os.listdir(folderpath)

imglist = []
studentidlist = []
for path in pathlist:
    imglist.append(cv2.imread(os.path.join(folderpath,path)))
    studentidlist.append(str(path[0:11]))
#adding images to the fairebase storage  
    imagefile  = (f'{folderpath}/{path}')
    bucket123 = storage.bucket()
    blob = bucket123.blob(imagefile)
    blob.upload_from_filename(imagefile)

print(studentidlist)


def findencodings(imageslist):
    encodes_list=[]
    for img in imageslist:
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodes_list.append(encode)
    return(encodes_list)

print("Encoding started..........................")
encodeslistknown=findencodings(imglist)
print(encodeslistknown)
print("Encoding finished.........................")
encodelistwithids=[encodeslistknown,studentidlist]


#generating pickle file to dump the encodings along with the ids
print("Adding values to file..............................")
file=open("Encodings.p","wb")
pickle.dump(encodelistwithids,file)
file.close()
print("Encodings added successfully.......................")