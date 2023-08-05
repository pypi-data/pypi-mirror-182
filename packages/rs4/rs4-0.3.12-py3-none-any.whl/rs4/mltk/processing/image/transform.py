import numpy as np
from skimage import exposure
import cv2

def contrast_stretching (x, r1 = 2, r2 = 98):
    floated = True
    if np.max (x) > 1:
         floated = False
         x = x / 255
    p2, p98 = np.percentile (x, (r1, r2))
    x = exposure.rescale_intensity (x, in_range = (p2, p98))
    if not floated:
         return np.clip ((x * 255).astype ('int64'), 0, 255)
    return x

def adaptive_equalization (x, clip_limit = 0.03):
     return exposure.equalize_adapthist (x, clip_limit = clip_limit)
                
def histogram_equalization (x):
    return exposure.equalize_hist (x)

def rotate (x, angle):
    row, col = x.shape [:2]
    center = tuple (np.array ([row,col]) / 2)
    rot_mat = cv2.getRotationMatrix2D (center, angle, 1.0)
    new_image = cv2.warpAffine(x, rot_mat, (col, row))
    return new_image

def flip (x):
    return cv2.flip(x, 1)
vflip = flip

def hflip (x):
    return cv2.flip(x, 0)    

def whitening (x):
    mean = np.mean (x)    
    std = np.std (x)  
    return (x - mean) / std
