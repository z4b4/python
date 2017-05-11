# -*- coding:utf-8 -*-
# @Author: z4b4 <z4b4>
# @Date:   2017-05-09T23:18:31+08:00
# @Email:  z4b4@qq.com
# @Filename: 1.py
# @Last modified by:   z4b4
# @Last modified time: 2017-05-10T23:27:00+08:00
n=int(input("Input a number Please"))
d=2
print(n,"=",end=" ")
while(1):
    if n%d==0:
        k=d
        if n==k:
            print(int(n),end=" ")
            break
        else:
            n=n/k
            d=1
            print(k,"*",end=" ")
    d=d+1
