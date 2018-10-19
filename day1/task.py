# _*_ coding: utf-8 _*_

import math

r = int(input("enter radius "))

c = 2 * math.pi * r
s = math.pi * math.sqrt(r)
print("area", s)
print("girth", c)