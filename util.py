import json
def crop(img, x, y, width, height):
    return img[y:height, x:width] # Crop from x, y, w, h -> 100, 200, 300, 400

def stamp(src, dst, x, y):
    h,w,c = src.shape
    dst[y:y+h,x:x+w] = src

def getRegion(img, index, hstrips, vstrips):
     h,w,c = img.shape
     x = (index % hstrips)* (w/hstrips)
     y = (index // hstrips)* (h/vstrips)
     width = (w/hstrips)
     height = (h/vstrips)
     return crop(img, x, y, x+width, y+height)

     returnedImage = np.zeros((h, w,c), np.uint8);

class Frame:
    def __init__(self, filename, img):
        self.filename = filename
        self.img = img
        self.rotated = False
        self.trimmed = True
        self.index = 0
        self.sourceSize = {"w":img.shape[1],"h":img.shape[0]}
        self.pivot ={"x":0.5,"y":0.5}
    ### end getP function

    def toJSON(self):
        d = {
            "filename" :self.filename,
            'rotated' :self.rotated,
            'trimmed' :self.trimmed,
            'index' :self.index,
            'sourceSize' :self.sourceSize,
            'pivot' :self.pivot,
            'spriteSourceSize': self.spriteSourceSize,
            'frame': self.frame
        }
        return d

def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__