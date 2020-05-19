# -*- coding: utf-8 -*-

materials = []

class Material():
	def __init__( self, n, p, a):
		self.name = n
		self.price = p
		self.amount = a
		
def getFromName( n):
	for m in materials :
		if( m.name == n):
			return m
	return None

def printMaterials():
	print("目前材料項：")
	for m in materials :
		print( "商品名稱：", m.name, "\t商品單價：",m.price, "\t商品數量：", m.amount)
		