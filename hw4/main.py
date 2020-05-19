# -*- coding: utf-8 -*-
from interface.material import purchase
from interface.personnel import hire, resignation
from interface.sales import confirmEmp, sales
from interface.situation import getMoney, getMaterial, getPersonnel

#材料系統
def M_interface():
	welcome = "材料系統啟動完成。請輸入需要使用的功能："
	while( True):
		print("\n1. 代表執行「進貨」\n2. 代表返回「介面」")
		Func = input(welcome)
		if( Func == "1"):
			purchase.M_buy()
			return
		elif( Func == "2"):
			print("返回「介面」中")
			return
		else :
			print("無此代碼！請重新輸入")

#人事系統
def P_Interface():
	while( True):
		print("\n1. 代表執行「聘任」\n2. 代表執行「離職」\n3. 代表返回「介面」")
		P_welcome = "人事系統啟動完成。請輸入需要使用的功能："
		P_Func = input(P_welcome)
		if( P_Func == "1"):
			hire.P_hire()
		elif( P_Func == "2"):
			resignation.P_fire()
		elif( P_Func == "3"):
			print("返回「介面」中")
			return
		else:
			print("無此代碼！請重新輸入")

#銷售系統
def S_Interface():
	while( True):
		print("\n1. 代表執行「銷售」\n2. 代表返回「介面」")
		welcome = "銷售系統啟動完成。請輸入需要使用的功能："
		Func = input(welcome)
		if( Func == "1"):
			confirmEmp.S_ConfirmEmp()
		elif( Func == "2"):
			print("返回「介面」中")
			return
		else :
			print("無此代碼！請重新輸入")

#店面情況
def G_Interface():
	while( True):
		print("\n1. 代表執行「材料情況」\n2. 代表執行「人事情況」\n3. 代表執行「財務情況」\n4. 代表返回「介面」")
		welcome = "店面情況啟動完成。請輸入需要顯示的資訊："
		Func = input(welcome)
		if( Func == "1"):
			getMaterial.printMaterials()
		elif( Func == "2"):
			getPersonnel.printEmployees()
		elif( Func == "3"):
			getMoney.printMoney()
		elif( Func == "4"):
			print("返回「介面」中")
			return
		else:
			print("無此代碼！請重新輸入")


#介面
welcome = "商店管理系統啟動完成。請輸入需要使用的功能："
while(True):
	print("\n1. 代表進入「材料系統」\n2. 代表進入「人事系統」\n3. 代表進入「銷售系統」\n4. 代表進入「店面情況」\n5. 代表離開「商店管理系統」")
	Func = input(welcome)
	if( Func == "1"):
		print("進入材料系統中")
		M_interface()

	elif ( Func == "2"):
		print("進入人事系統中")
		P_Interface()

	elif ( Func == "3"):
		print("進入銷售系統中")
		S_Interface()

	elif ( Func == "4"):
		print("進入店面情況中")
		G_Interface()
		
	elif ( Func == "5"):
		print("離開商店管理系統")
		break
	else :
		print("無此代碼！請重新輸入")


