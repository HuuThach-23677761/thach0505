# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:10:58 2024

@author: Student
"""
print ('kiểm tra 3 cạnh')
a = float(input('nhập a: '))
b = float(input('nhập b: '))
c = float(input('nhập c: '))
if a + b > c and a + c > b and c + b > a:
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print (a,b,c,' là 3 cạnh của tam giác vuông')
    elif a==b and b==c:
        print (a,b,c, 'là 3 cạnh của tam giác đều')
    elif a==b or b==c or c==a:
        print (a,b,c, "là 3 cạnh của tam giác cân")
    else:
        print(a,b,c, 'là 3 cạnh của tam giác thường')
     
else:
    print (a,b,c," không là 3 cạnh của 1 tam giác")

