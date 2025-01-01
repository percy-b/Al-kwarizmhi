# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 02:45:34 2025

@author: KEI
"""
x_array = [1,2,3,4]
y_array = [5,6,7,8,9]

x=0
y=0

for i in range(len(x_array)):
    x += x_array[i] * 10 **i
    
for i in range(len(y_array)):
    y += y_array[i] * 10 **i
    

print(x, y)

x_y = 0

for i in range(len(x_array)):
    for j in range(len(y_array)):
        x_y += x_array[i]*y_array[j]*10**(i+j)

print(x_y)

print(x*y)

z = [0]*9
hold = 0
for k in range(len(x_array)+len(y_array)):
    for i in range(len(x_array)):
        for j in range(len(y_array)):
            if i+j == k:
                hold = hold + x_array[i]*y_array[j]
    z[k] = hold%10
    hold = int(hold/10)
print(z)


23%10
