# -*- coding: utf-8 -*-
from PIL import Image

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
