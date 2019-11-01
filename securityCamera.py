import cv2
from datetime import datetime

cam = cv2.VideoCapture(0)  # set camera
cam.set(cv2.CAP_PROP_FPS, 60)  # set FPS
cam.set(3, 1920)  # x axis resolution
cam.set(4, 1080)  # y axis resolution

font = cv2.FONT_HERSHEY_TRIPLEX  # set font

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # set codec (*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, 20, (1280, 720))

while True:
    re, img = cam.read()  # set camera read

    img = cv2.flip(img, 1)  # flip image

    cv2.putText(img, "You Are Being Recorded", (270, 100), font, 2, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img, str(datetime.now()), (1000,700), font, .5, (255,255,255), 1, cv2.LINE_AA)
    cv2.imshow('Security Camera', img)  # display window

    out.write(img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press ESC to quit
        break

cam.release()
cv2.destroyAllWindows()
