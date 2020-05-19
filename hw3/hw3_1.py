# -*- coding: utf-8 -*-

"""
1. OOP – 題目一
"""

#商品類
class Product():
	def __init__( self, n, p, a):
		self.name = n
		self.price = p
		self.amount = a
	def getTotal(self):
		return self.amount * self.price - ( int(self.amount/2) * (self.price*0.2) )

#購物車
class ShoppingCar():
	products = []
	
	def __init__(self, name):
		self.name = name
		
	def getOwner(self):
		return self.name
		
	def getProduct( self):
		pName = []
		for p in self.products :
			pName.append( p.name)
		return pName
	
	def getDiscount( self):
		pName = []
		for p in self.products :
			if ( p.amount > 1 ):
				pName.append( p.name)
		return pName
		
	def getCost(self):
		cost = 0
		for p in self.products :
			cost += p.getTotal()
		return cost
		
	def addProduct( self, prodName, prodPrice, prodAmount):
		for p in self.products :
			if ( p.name == prodName and p.price == prodPrice):
				p.amount += prodAmount
				return
		
		self.products.append( Product( prodName, prodPrice, prodAmount))
		
	def removeProduct( self, prodName, prodPrice, prodAmount):
		for p in self.products :
			if ( p.name == prodName and p.price == prodPrice):
				p.amount -= prodAmount
			if( p.amount == 0):
				self.products.remove(p)
	
#測資範例
obj1 = ShoppingCar("花輪")
#增加商品至購物車 名稱、價錢、數量
obj1.addProduct( "巧克力", 50, 2) 
obj1.addProduct( "咖啡豆", 120, 3)
obj1.addProduct( "草莓果醬", 70, 5)
obj1.addProduct( "馬卡龍", 30, 1)
#從購物車移除商品 名稱、數量
obj1.removeProduct( "草莓果醬", 70, 2)
obj1.addProduct( "馬卡龍", 30, 2)
obj1.removeProduct( "咖啡豆", 120, 2)
obj1.addProduct( "馬卡龍", 40, 2)

print(obj1.getOwner(), "的購物車裡面有", obj1.getProduct(), "總共", obj1.getCost(), "元", "其中", obj1.getDiscount(), "享有第二件八折的優惠")

