import cv2
import numpy as np

#img = cv2.imread("img/moon1.png")
#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
#print(img_gray.shape)
#img[:,:,2]=0
# imgBlue=img[:,:,0]
# imgGreen=img[:,:,1]
# imgRed=img[:,:,2]
# new_img=np.hstack((imgBlue,imgGreen,imgRed))
#img_resize=cv2.resize(img,(256,256))
#img_resize=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
#print(img_resize.shape)
# img_flip=img[0:300,0:300]
# cv2.imwrite("moon_new.png", img_flip)
#img=np.zeros((512,512,3))
# cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=-1)
# cv2.circle(img, center= (100,400), radius=50, color=(0,255,0), thickness=-1)
# cv2.line(img,pt1=(0,0),pt2=(502,502),color=(0,0,255), thickness=3)
# cv2.putText(img,org=(100,200), fontScale=4, color=(0,255,0), thickness=2,lineType=cv2.LINE_AA, text='HELLO', fontFace=cv2.FONT_ITALIC)
# cv2.imshow("window",img)
# cv2.waitKey(0)
# def draw(event, x,y, flags, params):
#     #print(event)
#     if event==1:
#        cv2.circle(img,center=(x,y), radius=50, color=(0,255,0), thickness=-1)
# cv2.namedWindow(winname="window")
# cv2.setMouseCallback("window", draw)
#
# img=cv2.imread("img/moon1.png")
#
# while True:
#     cv2.imshow("window",img)
#     if cv2.waitKey(1) & 0xFF == ord("X"):
#          break
# cv2.destroyAllWindows()


import cv2
import numpy as np


flag=False
ix=-1
iy=-1

img=cv2.imread("img/solar1.png")

def crop (event,x,y,flags,params):
    global flag, ix, iy
    if event == 1:
      flag = True
      ix=x
      iy=y
    # elif event==1:
    #    cv2.rectangle(img,pt1=(ix,iy), pt2=(x,y), color=(0,0,0), thickness=1)
    elif event == 4:
       fx = x
       fy = y
       flag=False
       cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y), thickness=1, color=(0,0,0))
       cropped = img[iy:fy,ix:fx]
       cv2.imshow("new_window",cropped)
       cv2.waitKey(0)




# creating event listener
cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',crop )

while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF==ord("x"):
        break
cv2.destroyAllWindows()