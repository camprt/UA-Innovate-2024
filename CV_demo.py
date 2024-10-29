
# Refined version of the test file to include yellow states
# and selectable red zones
# created: 12:15 am

import numpy as np
import cv2 as cv

# open webcam
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()

#red zone initializers
redZone = -1
quadH = 200
quadW = 200
rpt_x = 0
rpt_y = 0
rwidth = 100
rheight = 100
#redCenter = (0,0)

while (1):
    #get input redZone
    if (redZone == -1):
        redZone = int(input("Designated a quadrant to be your red zone: "))
        #move to higher level for even sections)
        if (redZone % 2 == 0):
            rpt_x = int(quadW * (redZone/2) - quadW)
            rpt_y = int(quadH)
        #else just increment width
        else:
            rpt_x = int(quadW * ((redZone + 1)/2) - quadW)

        rpt_x += rwidth
        rpt_y += rheight
        #redCenter = (rpt_x + (rwidth*.5), rpt_y + (rheight * .5))
       

    else:
        #read in camera capture
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)
        if not ret:
            print("Failed to open camera")
            break
        color = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', color)
        cv.rectangle(frame, (rpt_x, rpt_y), (rpt_x + rwidth, rpt_y + rheight), (0, 0, 255), 2)

        # use haars cascade to get face
        haars_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = haars_cascade.detectMultiScale(
            color,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        #put box around face
        x = 0
        y = 0
        w = 0
        h = 0
        for (a, b, c, d) in faces:
            x = a
            y = b
            w = c
            h = d
            cv.rectangle(frame, (a, b), (a+c, b+d), (0, 255, 0), 2)
        cv.imshow('frame', frame)

        # origin
        if ((x > rpt_x and x < rpt_x+rwidth) and (y > rpt_y and y < rpt_y+rheight)):
            break
        #point (x, 0)
        elif((x+w > rpt_x and x+w < rpt_x+rwidth) and (y > rpt_y and y < rpt_y+rheight)):
            break
        #(0, y)
        elif((x > rpt_x and x < rpt_x+rwidth) and (y+h > rpt_y and y+h < rpt_y+rheight)):
            break
        #(x,y)
        elif ((x+w > rpt_x and x+w < rpt_x+rwidth) and (y+h > rpt_y and y+h < rpt_y+rheight)):
            break
       
        #failsafe quit
        if (cv.waitKey(1) == ord('q')):
            break

cap.release()
cv.destroyAllWindows()


