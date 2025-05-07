#walking through the files system 
import os 
import cv2
import face_recognition as FR
print(cv2.__version__)
imageDir='/home/patel/Documents/paul_ai/demoimages /known'

if not os.path.exists(imageDir):
    print(f"directory does not exists:{imageDir}")

for root,dirs,files in os.walk(imageDir):
    print('my working folder(root):',root)
    print('dirs in root :',dirs)
    print('my files in root',files)
    for file in files:
        print(f"your file is :{file}")
        #joining the full root path to file name 
        fullfilepath=os.path.join(root,file)
        print(fullfilepath) #fullfilepath will return the full file path 
        #now getting person's name from nitin.jpg 
        name=os.path.splitext(file)[0]# ('Chase', '.jpg') for chase only we use [0]
        print(name)
        
        mypicture=FR.load_image_file(fullfilepath)
        mypicture=cv2.cvtColor(mypicture,cv2.COLOR_RGB2BGR)
        cv2.imshow(name,mypicture)
        cv2.moveWindow(name,0,0)
        cv2.waitKey(2500)
        cv2.destroyAllWindows()
