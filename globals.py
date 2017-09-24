import numpy as np

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

nx = 9
ny = 6

#left_fit, right_fit, left_fit_poly, right_fit_poly 
#dst = np.float32([[ (320,0), (980,0), (980,720), (320,720)]])
#src = np.float32([[ (570,470), (720,470), (1130, 720), (200, 720)]])

src = np.float32([[580,460], [200,720],[1130,720], [700,460]])
dst = np.float32([[320,0], [320,720],[980,720], [980,0]])
    

detected_line = False

mtx = None
dist = None

