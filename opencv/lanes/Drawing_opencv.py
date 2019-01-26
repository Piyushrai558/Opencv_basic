# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:51:51 2019

@author: Piyush
"""

import cv2
import matplotlib.pyplot as lib
import numpy as np 
%matplotlib qt

img = cv2.imread('wrist_watch2.jpg', cv2.IMREAD_COLOR )

cv2.line(img , (0,0) ,(150, 150) , (255,255,255), 15)

cv2.rectangle(img , (15, 25), (200,150) , (0, 255 , 0), 5)    

cv2.circle(img , (100,63) , 55 , (0, 0,255) , 1)

pts = np.array([[10,5] , [20,30] , [70,20 ], [50,20 ]], np.int32)

cv2.polylines(img , [pts] , False, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img , 'Piyush RAi' , (0, 180), font , 1, (0, 0 , 255 ), 1 , cv2.LINE_AA )


cv2.imshow('image ' , img)
k = cv2.waitKey(0)
if k == 27 or ord('q'):
    cv2.destroyAllWindows()
