# -*- coding: utf-8 -*-

from interface.situation import getMoney, getPersonnel

def P_fire():

	print("請輸入欲離職的員工ID")
	i = input("員工ID：")

	for e in getPersonnel.employees:
		if( e.id == i and e.status == "在職"):
			e.status = "離職"
			getMoney.money += e.payment
			print("離職成功！剩下資金：", getMoney.money)
			return
		elif( e.id == i):
			print("離職失敗！此人已離職。")
			return

	print("離職失敗！此人不存在。")