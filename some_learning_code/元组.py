# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a_tuple = 1, 2, 'a'
b_tuple = 1, 2, 'c'

print (b_tuple[0])
print (b_tuple[-1])

try:
    b_tuple[0] = 20
except:
    print("Cannot change value of tuple by index.\n")

c_tuple = (1, 2, [10, 20, 30])
c_tuple[2][0] = 100

c = a_tuple+b_tuple

print (c)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a[1:], "\n")
print(a[1: 3], "\n")
print(a[1:6:2], "\n")
print(a[:-1], "\n")

print(min(a), max(a), "\n")

if 1 in a:
    print("Element 1 is available in tuple a")
else:
    print ("Element 1 is not available in tuple a")
    


from collections import namedtuple

vector = namedtuple("Dimension", 'x y z')
vec_1 = vector(1, 1, 1)
vec_2 = vector(1, 0, 1)

manhattan_distance = abs(vec_1.x - vec_2.x) + abs(vec_1.y - vec_2.y) + abs(vec_1.z - vec_2.z)

print("Manhattan distance between vectors = %d" %(manhattan_distance))


