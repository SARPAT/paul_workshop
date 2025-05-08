#making a training file automatically 
import os 
import cv2
import pickle
import face_recognition as FR

print(cv2.__version__)
encodings=[]
names=[]
imageDir='/home/patel/Documents/paul_ai/demoimages /known'
for root,dirs,files in os.walk(imageDir):
    for file in files:
        fullfilepath=os.path.join(root,file)
        print(fullfilepath)

        mypicture=FR.load_image_file(fullfilepath)
        encoding=FR.face_encodings(mypicture)[0]
        name=os.path.splitext(file)[0]

        encodings.append(encoding)
        names.append(name)

with open('/home/patel/Documents/paul_ai/train_data.pkl','wb') as f:
    pickle.dump(names,f)
    pickle.dump(encodings,f)




