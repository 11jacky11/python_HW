# -*- coding: utf-8 -*-
"""
3. Dictionary 操作
"""

s = "Cognitive radio (CR) can effectively alleviate the problems and catches a lot of attention in the world [2-3]."
p = [1, 1, 5, 2, 2, 1, 1, 3, 1, 2, 5, 1, 4, 4, 4, 1, 3, 3, 4, 4, 5, 1, 3, 2, 2, 3]

S = s.lower()
print("1.")
print(S)

d = {}
for c in S:
    d[c] = d.get(c,0) + 1
print("2.")
print(d)

d2 = d.fromkeys( d, 0)
for c in S:
    if c.isalpha():
        d2[c] += p[ord(c) - 97]
    else:
        d2[c] += 1

print("3.")
print(d2)

