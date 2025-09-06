from math import *

a = float(input("Enter first side :- "))
b = float(input("Enter second side :- "))
c = float(input("Enter third side :- "))

s = (a+b+c)/2

area = sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of Triangle is :- ",area)