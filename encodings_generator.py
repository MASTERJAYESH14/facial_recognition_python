import cv2
import face_recognition
import pickle
import os


#importing student images
folderpath= 'images'
pathlist=os.listdir(folderpath)
#print(pathlist)
imglist=[]
studentidlist=[]
for path in pathlist:
    imglist.append(cv2.imread(os.path.join(folderpath,path)))
    #print(path)
    studentidlist.append(str(path[0:11]))
print(studentidlist)
#print(len(imglist))

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