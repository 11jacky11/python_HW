# -*- coding: utf-8 -*-
"""
1. set()
"""

a = set([1, 12, 32, 74, 45, 16, 87])
b = set([12, 87, 55, 32, 16])
c = set([92, 87, 74, 55, 41, 23, 8])

print("1.")
print(a & b & c)
print("2.")
print(a & c)
print("3.")
print((a ^ b  ^ c) - (a & b & c))
print("4.")
print( ( (a&b) | (b&c) | (a&c) ) - (a & b & c))