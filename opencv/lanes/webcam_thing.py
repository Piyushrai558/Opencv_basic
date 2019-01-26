# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:03:31 2019

@author: Piyush
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output3.avi', fourcc, 20.0 , (640,480 ))


while True:
    ret , frame = cap.read()
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    
    cv2.imshow('fram2', frame)
    #cv2.imshow('frame', gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

out.release()

cv2.destroyAllWindows()    
 
       