# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

print("Giải phương trình bậc 2:")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            x = -c / b
            print("Phương trình có 1 nghiệm x = ")
else:
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Phương trình vô nghiệm!")
    elif d == 0:
        x0 = -b / (2 * a)
        print("Phương trình có 1 nghiệm x = ", x0)
    else:
        x1 = float((-b - math.sqrt(d)) / (2 * a))
        x2 = float((-b + math.sqrt(d)) / (2 * a))
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", x1)
        print("x2 = ", x2)