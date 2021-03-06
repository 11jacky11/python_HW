# -*- coding: utf-8 -*-

"""
hw1
"""

num = [["59647042"], ["01260528"], ["01616970", "69921388", "53451508"], ["710", "042", "633"]]
invoice = ["91132057", "53977042", "69565958", "13359685", "52822508", "64268088", "95756107", "67921388", "15269483", "31208591", "85601171", "31697745", "94191710", "87883887", "33598443", "01260528", "01626970"]
dic = {"特別獎": 0, "特獎": 0, "頭獎": 0, "二獎": 0, "三獎": 0, "四獎": 0, "五獎": 0, "六獎": 0, "沒中獎": 0}

def fullPrice( id, s):
	p = "六獎"
	if s[4:] == num[2][id][4:] :
		p = "五獎"
	if s[3:] == num[2][id][3:] :
		p = "四獎"
	if s[2:] == num[2][id][2:] :
		p = "三獎"
	if s[1:] == num[2][id][1:] :
		p = "二獎"
	if s == num[2][id] :
		p = "頭獎"
	return p
				
def price3( s):
	#頭獎後三
	for i in range( 3):
		if s[5:] == num[2][i][5:] :
			#檢查更高獎項
			dic[ fullPrice( i, s) ] += 1
			return True

	#加開六獎
	for i in range( 3):
		if s[5:] == num[3][i]:
			dic["六獎"] += 1
			return True
	#都沒中
	return False
	
	
# 第一題：中獎次數
for i in range( len( invoice)):
	if invoice[i] == num[0][0]:
		dic["特別獎"] += 1
		continue
	if invoice[i] == num[1][0]:
		dic["特獎"] += 1
		continue
	if price3( invoice[i]) == False :
		dic["沒中獎"] += 1
print("1.")
print(dic)

# 第二題：總獎金
money = {"特別獎": 10000000, "特獎": 2000000, "頭獎": 200000, "二獎": 40000, "三獎": 10000, "四獎": 4000, "五獎": 1000, "六獎": 200, "沒中獎": 0}

total = 0
for key in list(set(dic)):
	total += dic.get(key) * money.get(key)

print("2.")
print(total)







