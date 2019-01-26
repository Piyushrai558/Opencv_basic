# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 15:32:55 2019

@author: Piyush
"""

import cv2 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib qt


img = cv2.imread('wrist_watch2.jpg')
gray = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)

cv2.imshow("result1",gray )
k=cv2.waitKey(0)
if k == 27 or ord('q'):
     cv2.destroyAllWindows()
     
plt.imshow(gray )
plt.show()     

cv2.imwrite('wrist_watch_gray2.jpg', gray)
