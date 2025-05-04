import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX


width=640
height=360
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
#using face cascades 
#faceCascade=cv2.CascadeClassifier('/home/patel/Documents/paul_ai/haar/haarcascade_frontalface_default.xml')



saranshFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/saransh.jpg')
#faceLoc=FR.face_locations(saranshFace)[0]
saranshFaceEncode=FR.face_encodings(saranshFace)[0]



ashishFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/Nancy Pelosi.jpg')
#faceLoc=FR.face_locations(ashishFace)[0]
ashishFaceEncode=FR.face_encodings(ashishFace)[0]

kaushFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/Mike Pence.jpg')
#faceLoc=FR.face_locations(kaushFace)[0]
kaushFaceEncode=FR.face_encodings(kaushFace)[0]

nitinFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/Paul McWhorter.jpg')
#faceLoc=FR.face_locations(nitinFace)[0]
nitinFaceEncode=FR.face_encodings(nitinFace)[0]

'''ronaldFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/Ronald Reagan.jpg')
#faceLoc=FR.face_locations(ronaldFace)[0]
ronaldFaceEncode=FR.face_encodings(ronaldFace)[0]'''


knownEncodings=[saranshFaceEncode,ashishFaceEncode,kaushFaceEncode,nitinFaceEncode]
names=['SARANSH','ASHISH','KAUSHALENDRA','NITIN']


while True:
    ignore,unknownFace=cam.read()

    
    unknownFaceRGB=cv2.cvtColor(unknownFace,cv2.COLOR_BGR2RGB)
    faceLocations=FR.face_locations(unknownFaceRGB)
    unknownEncodings=FR.face_encodings(unknownFaceRGB,faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
         top,right,bottom,left=faceLocation
         print(faceLocation)
         cv2.rectangle(unknownFace,(left,top),(right,bottom),(255,0,0),3)
         name='Unknown Person'
         matches=FR.compare_faces(knownEncodings,unknownEncoding)
         print(matches)
         #this will tell the position where the match is !!
         if True in matches:
             matchIndex=matches.index(True)
             print(matchIndex)
             print(names[matchIndex]) 
             name=names[matchIndex]
         cv2.putText(unknownFace,name,(left,top),font,.75,(0,125,255),2)

    cv2.imshow('My Faces',unknownFace)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break


cam.release()
cv2.destroyAllWindows()






'''while True:
    ignore,  frame = cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #DETECTING face from the cam
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
    
    cv2.imshow('my web cam',frame)
    cv2.moveWindow('my web cam',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break 

cam.release()    '''