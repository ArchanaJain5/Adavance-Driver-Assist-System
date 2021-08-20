import numpy as np
import cv2

#video input
cap=cv2.VideoCapture(0)

#video to n frames
count=0;
#while True:
 #   ret,image=cap.read()
  #  cv2.imwrite("frame%d.jpg" %count, image)
   # if cv2.waitKey(10)==27:
    #    break
    #count+=1
# get total number of frames
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)


     
#working on 1st frame
cap.set(1,0); # Where frame_no is the frame you want
ret, frame = cap.read() # Read the frame

 # Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
I=frame
cb = 0.148* I[:,:,0] - 0.291* I[:,:,1] + 0.439 * I[:,:,2] + 128
cr = 0.439 * I[:,:,0] - 0.368 * I[:,:,1] -0.071 * I[:,:,2] + 128
w = np.size(I[:,1,1])
h = np.size(I[1,:,1])
segment = [[0] * w for i in range(h)] 

count1 = 0
for i in range(1,w):
    for j in range(1,h):
        np.all(135<=cr[i,j] and cr[i,j]<=180 and 120<=cb[i,j] and cb[i,j]<=200 and 0.01<=hsv[i,j] and hsv[i,j]<=0.1)
        segment[i][j]=1
        count1=count1+1
        #else:
        #    segment[i][j]=0
#im[:,:,1]=I[:,:,1].*segment
#im[:,:,2]=I[:,:,2].*segment
#im[:,:,3]=I[:,:,3].*segment
im=np.multiply(I,segment)
cv2.imshow('image',im)
#Calculating the percentage
pixel_count = (count1*5)/100

#rest of frames
num=0

for t in range(2,totalFrames-1,2):
    count2=0
    cap.set(1,t); # Where frame_no is the frame you want
    ret, frame = cap.read() # Read the frame

     # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    I=frame
    cb = 0.148* I[:,:,1] - 0.291* I[:,:,2] + 0.439 * I[:,:,3] + 128
    cr = 0.439 * I[:,:,1] - 0.368 * I[:,:,2] -0.071 * I[:,:,3] + 128
    w = size(I[:,1,1])
    h = size(I[1,:,1])
   
    count2=0
    for i in range(1,w):
        for j in range(1,h):
            if np.any(135<=cr[i,j] and cr[i,j]<=180 and 120<=cb[i,j] and cb[i,j]<=200 and 0.01<=hue[i,j] and hue[i,j]<=0.1):
                segment[i,j]=1
                count2=count2+1
            else:
                segment[i,j]=0
    #im[:,:,1]=I[:,:,1].*segment
    #im[:,:,2]=I[:,:,2].*segment
    #im[:,:,3]=I[:,:,3].*segment
    im=np.multiply(I,segment)
    cv2.imshow('image',im)
   
    if count1-count2 > pixel_count:
        num = num+1
if num>15:
    print('Warning: Head Lowering Detected')
    
cap.release()
cv2.destroyAllWindows()
