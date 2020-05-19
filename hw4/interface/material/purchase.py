# -*- coding: utf-8 -*-

from interface.situation import getMoney, getMaterial

def M_buy():
	
	Finish = False
	while( Finish == False):
		print("請輸入進貨材料詳情")
		n = input("商品名稱：")
		p = int(input("商品單價："))
		a = int(input("商品數量："))

		if( p * a > getMoney.money):
			print("資金不足！請重新輸入...")
			Finish = False
		else:
			m = getMaterial.getFromName(n)
			if ( m == None):
				getMaterial.materials.append( getMaterial.Material( n, p, a))
				getMoney.money -= p * a
				print("新增成功！剩下金額：", getMoney.money)
				Finish = True
			else:
				m.amount += a
				getMoney.money -= p * a
				print("新增成功！剩下金額：", getMoney.money)
				Finish = True