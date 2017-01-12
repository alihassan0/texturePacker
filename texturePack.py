from os import listdir
from os.path import isfile, join
from util import crop,stamp, Frame, dumper

import cv2
import numpy as np
import json

path = "assets"
jsonObject = {'frames':[],'meta':{}}

#get fileNames
fileNames = [f for f in listdir(path) if isfile(join(path, f))]

#load all images in a dict
for fileName in fileNames:
    img = cv2.imread(path+'/'+fileName, cv2.IMREAD_UNCHANGED)
    frame = Frame(fileName, img)
    jsonObject['frames'].append(frame)

# #create Texture atlass images
width = 512;
height = 512;
img = np.zeros((height, width,4), np.uint8)

lastX = 0
lastY = 0
maxHeightInRow = 0
for frame in jsonObject['frames']:

    ## trim image
    image_data_bw = frame.img.max(axis=2)
    non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
    non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
    cY1, cY2, cX1, cX2 = min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns)
    frame.spriteSourceSize =  {"x":cX1,"y":cY1,"w":cX2-cX1+1,"h":cY2-cY1+1}
    frame.img = crop(frame.img, cX1 , cY1, cX2+1 , cY2+1)
    
    h,w,c = frame.img.shape
    
    if lastX + w >= 512 :
        lastY += maxHeightInRow
        lastX = 0
        maxHeightInRow = 0
    
    if h > maxHeightInRow:
        maxHeightInRow = h 

    stamp(frame.img,img,lastX,lastY)
    frame.frame =  {"x":lastX,"y":lastY,"w":cX2-cX1+1,"h":cY2-cY1+1}
    lastX += w
    

# with open('output/output.json', 'w') as outfile:
#     json.dumps(jsonObject, outfile, )

import io, json
with io.open('output/myTest.json', 'w', encoding='utf-8') as f:
  f.write(unicode(json.dumps(jsonObject, default=dumper, indent=4, sort_keys=True, ensure_ascii=False)))

cv2.imwrite("output/myTest.png", img)

cv2.imshow("opencv",img)
cv2.waitKey(0)