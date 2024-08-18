# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:21:21 2024

@author: Student
"""

a = float(input("Nhập điểm trung bình (GPA): "))
if a < 3.5:
    print('Học lực Kém')
elif a >= 3.5 and a < 5.0:
    print('Học lực Yếu')
elif a >= 5.0 and a < 7.0:
    print('Học lực Trung bình')
elif a >= 7.0 and a < 8.0:
    print('Học lực Khá')
elif a >= 8.0 and a < 9.0:
    print('Học lực Giỏi')
elif a >= 9.0 and a <= 10:
    print('Học lực Xuất sắc')
else:
    print ('Không xác định')

