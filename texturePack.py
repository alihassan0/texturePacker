import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

path = "assets"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

print onlyfiles

