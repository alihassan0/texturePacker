from os import listdir
from os.path import isfile, join
from util import crop,stamp

import cv2
import numpy as np

path = "assets"
dict = {}

#get fileNames
fileNames = [f for f in listdir(path) if isfile(join(path, f))]

#load all images in a dict
for fileName in fileNames:
    dict[fileName] = cv2.imread(path+'/'+fileName, cv2.IMREAD_UNCHANGED);

#create Texture atlass images
width = 512;
height = 512;
img = np.zeros((height, width,4), np.uint8)

lastX = 0
for key in dict:
    image_data_bw = dict[key].max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
    cY1, cY2, cX1, cX2 = min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns)
    
    dict[key] = crop(dict[key], cX1 , cY1, cX2+1 , cY2+1)
    h,w,c = dict[key].shape
    stamp(dict[key],img,lastX,0)
    lastX += w

cv2.imwrite("output/L5_output.png", img)

cv2.imshow("opencv",img)
cv2.waitKey(0)