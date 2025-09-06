from math import *

p = int(input("Enter the principle amount :- "))
r = int(input("Enter the rate of intrest :- "))
print("What do you want to Enter time period in years or months?")
print("1. Years")
print("2. Months")
choice = int(input("Enter your choice :- "))
if choice == 1:
  t = int(input("Enter the time period in years :- "))
  ci = p * pow((1 + r / 100), t)
  print("Compound intrest is :- ", ci)
elif choice == 2:
  t = int(input("Enter the time period in months :- "))
  ci = p * pow((1 + r / 100), t / 12)
  print("Compound intrest is :- ", ci)
else:
  print("Invalid choice")
