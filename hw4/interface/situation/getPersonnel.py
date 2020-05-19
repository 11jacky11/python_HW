# -*- coding: utf-8 -*-

employees = []

class Employee():
	def __init__( self, n, i, p, s):
		self.name = n
		self.id = i
		self.payment = p
		self.status = s

def printEmployees():
	print("人事資訊：")
	for e in employees :
		print( "姓名：", e.name, "\t員工ID：", e.id, "\t薪資：", e.payment, "\t狀態：", e.status)
		