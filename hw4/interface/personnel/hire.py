# -*- coding: utf-8 -*-

from interface.situation import getMoney, getPersonnel

def P_hire():

	print("請輸入欲聘任的人事資訊")
	n = input("姓名：")
	i = input("員工ID：")
	p = int(input("薪資："))
	s = input("狀態(在職/離職)：")

	for e in getPersonnel.employees :
		if ( e.id == i and e.status == "在職"):
			print("此人已在職！無法再次聘任。")
			return
		if ( e.id == i and e.status == "離職"):
			if( p > getMoney.money):
				print("資金不足！無法聘任。剩下資金：", getMoney.money)
				return
			e.name = n
			e.payment = p
			if( s == "在職"):
				e.status = "在職"
				getMoney.money -= p
			print("聘任成功！剩下資金：", getMoney.money)
			return

	if( p > getMoney.money):
		print("資金不足！無法聘任。剩下資金：", getMoney.money)
		return
	
	if( s == "在職"):
		getMoney.money -= p
	getPersonnel.employees.append( getPersonnel.Employee( n, i, p, s))	
	print("聘任成功！剩下資金：", getMoney.money)