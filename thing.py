import numpy as np
import cv2
import math

trueness = True
imagine = 'rectange15.png'
while trueness:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(grayscale, 16, 50, 50)

    corners = cv2.goodFeaturesToTrack(blur, 40, 0.1, 10)
    corners = np.intp(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(frame, (x, y), 8, 255, -1)

    # Draw line between points to draw triangle
    x1 = corners[0].ravel()[0]
    y1 = corners[0].ravel()[1]
    x2 = corners[1].ravel()[0]
    y2 = corners[1].ravel()[1]
    x3 = corners[2].ravel()[0]
    y3 = corners[2].ravel()[1]
    x4 = corners[3].ravel()[0]
    y4 = corners[3].ravel()[1]
    points = [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
    points.sort()
    print(points)
    line12 = (math.sqrt(((points[0][0]-points[1][0])**2)+((points[0][1]-points[1][1])**2)))/(math.sqrt(((points[2][0]-points[3][0])**2)+((points[2][1]-points[3][1])**2)))
    print(imagine)
    print(line12)
    expected = ((144*(line12**2))+(-373*line12)+223)
    print("anglebyformula")
    print(expected)
    cv2.line(frame, (x2, y2), (x3, y3), (0, 255, 0), thickness=3, lineType=8)
    cv2.line(frame, (x3, y3), (x4, y4), (0, 255, 0), thickness=3, lineType=8)
    cv2.line(frame, (x4, y4), (x1, y1), (0, 255, 0), thickness=3, lineType=8)
    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), thickness=3, lineType=8)
    cv2.imshow('Image', frame)
    cv2.waitKey(1)