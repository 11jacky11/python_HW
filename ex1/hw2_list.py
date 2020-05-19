# -*- coding: utf-8 -*-
"""
2. List 操作
"""

A = []

for i in range( 1, 101):
    A.append( i)
print("1.")
print(A)

for i in range( 1, 101):
    if ( i%2 == 0) or ( i%3 == 0):
        A.remove( i)
print("2.")
print(A)

A.sort(reverse=True)

print("3.")
print(A)