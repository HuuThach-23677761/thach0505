# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:42:21 2024

@author: Student
"""

a = input("Nhập ngày tháng năm: ")
if '/' in a:
    b = '/'
    parts = a.split('/')
elif '-' in a:
    b = '-'
    parts =a.split('-')
else:
    print('Ngày tháng năm không hợp lệ')
    exit()
if len(parts) !=3:
    print("ngày tháng năm không hợp lệ.")
    exit()
day, month, year = parts
if not (day.isdigit() and month.isdigit() and year.isdigit()):
    print ('Ngày tháng năm không hợp lệ:')
    exit()
day = int(day)
month = int(month)
year = int(year)
if year < 1:
    print ('Ngày tháng năm không hợp lệ')
    exit()
if month < 1 or month > 12:
    print ('Ngày tháng năm không hợp lệ')
    exit()
day_in_month = [31,29 if(year%4==0 and year % 100 != 0) or (year % 400 == 0) else 28,30,31,30,31,31,30,31,30,31]
if day < 1 or day > day_in_month [month-1]:
    print('ngày ko hợp lệ')
else:
    print("ngày tháng năm hợp lệ")
    