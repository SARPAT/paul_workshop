import cv2
print(cv2.__version__)
width=640
height=360
myRadius=30
myColor=(0,0,0)
myThick=2 
fontH=2.5
fontT=2
myText='SARANSH is BOSS '
myFont=cv2.FONT_HERSHEY_DUPLEX
upperLeft=(250,140)
lowerRight=(390,220)
lineW=4
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frame[140:220,250:390]=(255,0,0)
    cv2.rectangle(frame,upperLeft,lowerRight,(100,255,150),lineW)
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)
    cv2.putText(frame,myText,(120,60),myFont,fontH,(0,125,255),fontT)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',320,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()