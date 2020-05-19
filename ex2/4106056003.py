# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter

"""
1. 
"""
def printPIC( name):
	imageFile = name + ".jpg"
	im = Image.open( imageFile)

	print( "Image " + name + " information")
	print( "檔案格式：" + im.format)
	print( "色彩模式：" + im.mode)
	print( "圖片寬高：(" + str(im.height) + ", " + str(im.width) + ")")
	
printPIC("bird")
printPIC("coffee")


"""
2. 
"""
im2 = Image.open( "bird.jpg")

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


"""
3. 
"""
im3 = Image.open( "coffee.jpg")

# 對C做找邊
C = im3.filter( ImageFilter.FIND_EDGES)
C.show()

D = im3.crop((1100, 750, 1800, 1250))
# 對D做灰階的處理
D = D.convert("L")
D.show()


"""
4. B與D互換
"""
D = D.resize( (900, 750) )
A.paste( D, (800, 400, 1700, 1150))
A.show()

B = B.resize( (700, 500) )
C.paste( B, (1100, 750, 1800, 1250))
C.show()