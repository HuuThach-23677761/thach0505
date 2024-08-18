# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:33:21 2024

@author: Student
"""
print ('tính phương trình: ax + b =0')
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
if a != 0: 
    x = -b/a
    print('Nghiệm của phương trình là: ', x)
else:
    if b == 0:
        print('Phương trình có vô số nghiệm.')
    else:
        print('Phương trình vô nghiệm.')