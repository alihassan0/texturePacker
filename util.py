
def crop(img, x, y, width, height):
    return img[y:height, x:width] # Crop from x, y, w, h -> 100, 200, 300, 400

def stamp(src, dst, x, y):
    h,w,c = src.shape
    dst[y:y+h,x:x+w] = src