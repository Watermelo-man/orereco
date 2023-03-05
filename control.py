import sys
from pathlib import Path
import  universal_model 
import cv2
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage


model = universal_model.kernel.kernel(model_path="C:\\Projects\\orereco\\ourmodels\\onlygold.pt", device="CUDA:0")

#im = cv2.imread("C:\\Projects\\orereco\\source\\bottle.jpg")

im =Image.open("C:\\Projects\\orereco\\source\\0038.png")

#im = cv2.VideoCapture(0)

md = universal_model.modelType.PictureModel(model.kernel)
#md = universal_model.modelType.VideoModel(model.kernel)


print(type(im))


def analyseImg():
    md.predict(im)
    res= md.showLastShot()
    #create from numpy Qpixmap
    h,w,ch = res.shape
    bytes_per_line = ch*w
    convert_to_Qt_format = QImage(res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
    #create from numpy Qpixmap
    return convert_to_Qt_format



'''
while(True):
    

    md.predict(im)

    res = md.showLastShot()


    cv2.imshow("lol",cv2.resize(res,[640,480]))#cv2.resize(res,[640,480]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.waitKey(0)
'''

"""
from universal_model import kernel
from universal_model import modelType

"""
 