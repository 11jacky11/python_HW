# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter

"""
3. 
"""

imageFile = "coffee.jpg"
im3 = Image.open( imageFile)


# 對C做找邊
C = im3.filter( ImageFilter.FIND_EDGES)
C.show()

D = im3.crop((1100, 750, 1800, 1250))
# 對D做灰階的處理
D = D.convert("L")
D.show()