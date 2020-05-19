# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter

"""
2. 
"""

imageFile = "bird.jpg"
im2 = Image.open( imageFile)


# 對A做五次的模糊
for i in range(5): 
	A = im2.filter( ImageFilter.BLUR)
A.show()

B = im2.crop((800, 400, 1700, 1150))
# 把B左右反轉
B = B.transpose(Image.FLIP_LEFT_RIGHT)
# 對B做輪廓
B = B.filter(ImageFilter.CONTOUR)
B.show()