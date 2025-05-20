#function and class 
import cv2
print(cv2.__version__)
import mediapipe as mp
width=640
height=360

hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) #false=not a static image , 2= for two hands , 0.5=confidence in tracking 
#draw object
mpDraw=mp.solutions.drawing_utils

def parseLandmarks(frame):
    myhands=[]
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    if results.multi_hand_landmarks !=None :
        for handlandmarks in results.multi_handlandmarks :
            myhand=[]
            mpDraw.draw_Landmarks(frame,handlandmarks,mp.solutions.hands.HAND_CONNECTIONS)
            for landmarks in handlandmarks.landmark:
                myhand.append((int(landmarks.x*width),int(landmarks.y*height)))
            myhands.append(myhand)
    return myhands



cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore,frame=cam.read()
    myHands=parseLandmarks(frame)
    for hand in myHands:
        cv2.circle(frame,hand[20],10,(255,0,0),-1)
    cv2.imshow('my WEBcam', frame) 
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
       break

cam.release()