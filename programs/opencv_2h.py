import cv2

print(cv2.__version__)

width=640
height=360

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade=cv2.CascadeClassifier('/home/patel/Documents/paul_ai/haar/haarcascade_frontalface_default.xml')
#eyeCascade=cv2.CascadeClassifier('/home/patel/Documents/paul_ai/haar/haarcascade_eye.xml')
smileCascade=cv2.CascadeClassifier('/home/patel/Documents/paul_ai/haar/haarcascade_smile.xml')
lefticascade=cv2.CascadeClassifier('/home/patel/Documents/paul_ai/haar/haarcascade_lefteye_2splits.xml')
righticascade=cv2.CascadeClassifier('/home/patel/Documents/paul_ai/haar/haarcascade_righteye_2splits.xml')
mytext1='left eye'
mytext2='right eye'
fontH=0.7
fontT=2
myfont=cv2.FONT_HERSHEY_COMPLEX
while True:
    ignore, frame=cam.read()
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    leyes=lefticascade.detectMultiScale(frameGray,1.3,5)
    reyes=righticascade.detectMultiScale(frameGray,1.3,5)
    smiles=smileCascade.detectMultiScale(frameGray,1.3,5)


    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),3)
    for leye in leyes:
        x,y,w,h=leye
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        
        cv2.putText(frame,mytext1,(x-w+30,y),myfont,fontH,(100,0,20),fontT)
        

    for reye in reyes:
        x,y,w,h=reye
        test=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(frame,mytext2,(x-w,y),myfont,fontH,(0,0,0),fontT)
        for count in test:
            if count==1:
                break
        

    '''for smile in smile:
        x,y,w,h=smile
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)'''     
    cv2.imshow("mywebcam",frame)
    cv2.moveWindow("mywebcam",0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()        