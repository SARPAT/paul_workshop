#parsefuction using class 
import cv2
print(cv2.__version__)
width=640
height=320
#import mediapipe as mp


class mphands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=0.5,tol2=0.5):
        self.hands=self.mp.solutions.hands.Hands(static_image_mode=False,max_num_hands=maxHands,min_detection_confidence=tol1,min_tracking_confidence=tol2)

    def Marks(self,frame):
        myhands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks is not None:
            for handlandmarks in results.multi_hand_landmarks:
                myhand=[]

                for  landmark in handlandmarks.landmark:
                   myhand.append((int(landmark.x*width),int(landmark.y*height)))

                myhands.append(myhand) 
        return myhands
        

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findhand=mphands(1,0.5,0.5) # passing 1 so that it does processing just one hand 
while True:
    ignore,frame=cam.read()
    frame=cv2.resize(frame,(width,height))
    handData=findhand.Marks(frame)
    for hand in handData:
        for index in [0,5,6,7,8]:
            cv2.circle(frame,hand[index],10,(255,125,0),2)

            
    cv2.imshow('my WEBcam', frame) 
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
       break
 
cam.release()        
cv2.destroyAllWindows()
