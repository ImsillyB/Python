# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = range(1, 10)
print(a)
b = ["a", "b", "c"]
print(b)

print (a[0])

a[-1]

print (a[1:3])
print (a[1:])
print (a[-1:])
print (a[:-1])

a = [1, 2]
b = [3, 4]
print(a + b)

print(min(a), max(a))

if 1 in a:
    print("Element 1 is available in list a")
else:
    print ("Element 1 is not available in list a")


a_stack = []

a_stack.append(1)
a_stack.append(2)
a_stack.append(3)

print (a_stack.pop())
print (a_stack.pop())
print (a_stack.pop())

a_queue = []

a_queue.append(1)
a_queue.append(2)
a_queue.append(3)

print(a_queue.pop(0))
print(a_queue.pop(0))
print(a_queue.pop(0))

from random import shuffle

a = range(1, 20)
shuffle(a)

print(a)

a.sort()
print(a)

a.reverse()
print(a)