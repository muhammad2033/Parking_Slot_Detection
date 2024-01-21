import cv2
import pickle
import os

width, height = 107, 48
try:
    with open('CarParkPos','rb') as f:
        posList=pickle.load(f)
except:
    posList=[]

imgpath= os.path.abspath('carParkImg.png')
def mouseClick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        posList.append(x,y)
    if events==cv2.EVENT_RBUTTONDOWN:
        for i, pos in posList:
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                posList.pop(i)
    with open("CarParkPositions",'wb') as f:
        pickle.dump(posList,f)
while True:
    image= cv2.imread(imgpath)
    for pos in posList:
        cv2.rectangle(image,pos,(pos[0] + width, pos[1] + height), (255,0,255),2)
    cv2.imshow("ParkingImage",image)
    # cv2.setMouseCallback("Image",mouseClick)
    cv2.waitKey(1)