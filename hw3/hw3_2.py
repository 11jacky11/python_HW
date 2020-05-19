# -*- coding: utf-8 -*-

"""
2. 例外處理 – 題目二
"""

flag = True
while( flag):
	flag = False
	file = input("請輸入檔案名稱：")
	try:
		f = open( file, mode="r")
	except FileNotFoundError:
		print( "找不到檔案!")
		flag = True
	except:
		print("錯誤的輸入!")
		flag = True

print( f.read())
f.close()