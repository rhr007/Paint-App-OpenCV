

import numpy as np
import cv2 as cv

background = np.ones((650, 1200, 3), dtype=np.uint8) * 255
drawing = False
color = (0, 255, 0)

def showNotes():
    cv.rectangle(background, pt1=(1011, 4), pt2=(1198, 185), color=(50, 50, 100), thickness=-1)
    cv.putText(background, text='* Essential Buttons', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 20), color=(200, 255, 255))
    cv.putText(background, text='______________________', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 30), color=(200, 255, 255))
    cv.putText(background, text='--> "s" for saving', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 50), color=(200, 255, 255))
    cv.putText(background, text='--> "g" for GREEN', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 70), color=(200, 255, 255))
    cv.putText(background, text='--> "r" for RED', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 90), color=(200, 255, 255))
    cv.putText(background, text='--> "b" for BLUE', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 110), color=(200, 255, 255))
    cv.putText(background, text='--> "o" for BLACK', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 130), color=(200, 255, 255))
    cv.putText(background, text='--> "c" to clear', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 150), color=(200, 255, 255))
    cv.putText(background, text='--> "q" to QUIT', fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=0.9, org=(1020, 170), color=(200, 255, 255))



def draw(event, x, y, param4, param5):
    global drawing

    if event == 1:
        print(x, y)
        drawing = True
        cv.circle(background, center=(x, y), radius=4, color=color, thickness=-1)
        

    elif event == 0 and drawing:
        cv.circle(background, center=(x, y), radius=4, color=color, thickness=-1)

    elif event == 4:
        drawing = False



cv.namedWindow('Board')
cv.setMouseCallback('Board', draw)

showNotes()
while True:
    cv.imshow('Board', background)
    key = cv.waitKey(1)

    if key == ord('q'):
        break

    elif key == ord('g'):
        color = (0, 255, 0)

    elif key == ord('r'):
        color = (0, 0, 255)
    
    elif key == ord('b'):
        color = (255, 0, 0)

    elif key == ord('o'):
        color = (0, 0, 0)

    elif key == ord('c'):
        background[:] = 255
        showNotes()

    elif key == ord('s'):
        cv.imwrite('./myPaint.jpg', background)
