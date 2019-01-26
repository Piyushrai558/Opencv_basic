# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:26:31 2019

@author: Piyush
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt

image = cv2.imread("test_image.jpg")
lane_image = np.copy(image) #$because the image is mutable and any change in lane image would effect so we use copy to cover mutation 
gray = cv2.cvtColor(lane_image , cv2.COLOR_RGB2GRAY)
cv2.imshow("result1",image )
k=cv2.waitKey(0)
if k == 27 or ord('q'):
     cv2.destroyAllWindows()
#cv2.destroyAllWindows()
#step 2

lane_image = np.copy(image) #$because the image is mutable and any change in lane image would effect so we use copy to cover mutation 
gray = cv2.cvtColor(lane_image , cv2.COLOR_RGB2GRAY)
cv2.imshow("result2",gray )
k = cv2.waitKey(0)

if k == 27 or ord('q'):
     cv2.destroyAllWindows()

#step 3 
""" finding gaussian blur"""
"""image noise can create false edges and ultimately effetct
image detection"""
blur = cv2.GaussianBlur(gray , (5,5), 0)
cv2.imshow("result3",blur )
k = cv2.waitKey(0)

if k == 27 or ord('q'):
     cv2.destroyAllWindows()
#canny function
     
gray = cv2.cvtColor(lane_image , cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray , (5,5), 0)
canny =  cv2.Canny(blur , 50 , 150)
cv2.imshow("result4", canny)
k = cv2.waitKey(0)
if k == 27 or ord('q'):
    cv2.destroyAllWindows()

#using matplot library for plotting the image in form of x axis amd y axis 
plt.imshow(canny )
plt.show()
  
#to credit the completely black image a mask with same dimension of our road image 
#and fill part of its area with triangular polygon as we can see in the image we havw to specify the right side image

"""region of interest """
def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([[(200, height ), (1100 , height ), (550, 250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons,255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image

crop_image = region_of_interest(canny)
cv2.imshow("result5", crop_image)
k = cv2.waitKey(0)
if k == 27 or ord('q'):
    cv2.destroyAllWindows()


def display_line(image , lines):
    line_image = np.zeros_like(image)
    if lines is not  None:
        for line in lines:
            x1, y1 , x2 , y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255,0,0), 10)
    return line_image
            #print (line)
        
        
""" creating a houghspace for our region of interest space it would select the required images in perfect precision """       
    
lines = cv2.HoughLinesP(crop_image , 2 , np.pi/180, 100  ,np.array([]), minLineLength= 40 , maxLineGap = 5)

line_image = display_line(lane_image, lines)
cv2.imshow("result6", line_image)
k = cv2.waitKey(0)
if k == 27 or ord('q'):
    cv2.destroyAllWindows()
    
combo_image = cv2.addWeighted(lane_image, 0.8, line_image , 1 , 1) 
cv2.imshow('result 7', combo_image)   
k = cv2.waitKey(0)
if k == 27 or ord('q'):
    cv2.destroyAllWindows()
    

    






 



#canny edege detection algorithm
#identifying sharp changes in intensity in adjacent pixels
#try and find regions in an image where there is as sharp
"""a pixel intenisty can be measure by a 0 to 255 o indiacates no intensity 
if something is completely black whereas 255 represent maximum intensity:
is completely black whereas 255 represents maximum intensity something being completely 
white that being said a gradient is the change in brightness over a series of pixel as 
a strong gradient indicates a steep changes whereas a small gradeint represent a small change 
  
whereas edge is defined by the difference in intensity value of pixel
wherever a strong change change in a strong intensity change """

