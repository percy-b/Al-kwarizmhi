# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 07:55:46 2025

@author: KEI
"""
x=4321
y= 98765

prod= 0 

while x>0:
    if x %2 !=0:
        prod = prod + y
    x = x//2
    y = y+y

print(prod)
        