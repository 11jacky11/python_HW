# -*- coding: utf-8 -*-

from interface.situation import getMoney, getMaterial

def S_sales():

	while( True):
		print("\n請輸入欲銷售的商品資訊")
		n = input("商品名稱：")
		p = int(input("商品單價："))
		a = int(input("商品數量："))
		
		m = getMaterial.getFromName(n)
		if ( m == None):
			print("商品數量不足，銷售失敗！請重新輸入...")
		elif ( a > m.amount):
			print("商品數量不足，銷售失敗！請重新輸入...")
		else:
			m.amount -= a
			if ( m.amount == 0 ):
				getMaterial.material.remove(m)
			getMoney.money += p * a
			print("銷售成功！剩下金額：", getMoney.money)
			return