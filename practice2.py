import cv2
import numpy as np

# In videocapture 0 stands for for your primary webcam
cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (648,488))
#recording the video
write = cv2.VideoWriter
while True:
    #ret shows that video is live or not
    ret, frame = cap.read()
    out.write(frame)

    #to grayscale
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("webcam", img_gray)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
out.release()
cv2.destroyAllWindows()