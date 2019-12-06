# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 23:11:13 2019

@author: vignesh
"""
print("to check the year is leap or not")
n=input("enter the year you need to check out?\n")
c=int(n)
if(c%4==0):
    print("the year",c,"is leap year")
else:
    print("the year",c,"is not an leap year")