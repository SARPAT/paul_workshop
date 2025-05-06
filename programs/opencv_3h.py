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




saranshFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/saransh.jpg')
faceLoc=FR.face_locations(saranshFace)[0]
saranshFaceEncode=FR.face_encodings(saranshFace)[0]



ashishFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/Nancy Pelosi.jpg')
faceLoc=FR.face_locations(ashishFace)[0]
ashishFaceEncode=FR.face_encodings(ashishFace)[0]

kaushFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/Mike Pence.jpg')
faceLoc=FR.face_locations(kaushFace)[0]
kaushFaceEncode=FR.face_encodings(kaushFace)[0]

nitinFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/Paul McWhorter.jpg')
faceLoc=FR.face_locations(nitinFace)[0]
nitinFaceEncode=FR.face_encodings(nitinFace)[0]

sonalFace=FR.load_image_file('/home/patel/Documents/paul_ai/demoimages /known/sonal.jpg')
faceLoc=FR.face_locations(sonalFace)[0]
sonalFaceEncode=FR.face_encodings(sonalFace)[0]


knownEncodings=[saranshFaceEncode,ashishFaceEncode,kaushFaceEncode,nitinFaceEncode,sonalFaceEncode]
names=['SARANSH','ASHISH','KAUSHALENDRA','NITIN','SONAL']


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
         cv2.putText(unknownFace,name,(left,top),font,.75,(0,0,255),2)

    cv2.imshow('My Faces',unknownFace)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break


cam.release()
cv2.destroyAllWindows()
