# -*- coding: utf-8 -*-

from interface.situation import getPersonnel
from interface.sales import sales

def S_ConfirmEmp():

	print("\n請輸入銷售員ID")
	i = input("員工ID：")

	for e in getPersonnel.employees :
		if ( e.id == i and e.status == "在職"):
			print("確認成功！進入銷售階段...")
			sales.S_sales()
			return

	print("銷售失敗，原因：此員工可能不存在 或 此員工可能已離職")