from math import pow
class Ci:

  def __init__(self,p1,r1,n1):
    self.p = p1
    self.r = r1
    self.n = n1

  def calc(self):
    self.a = self.p*pow((1+self.r/100),self.n)
    self.ci = self.a-self.p

  def __str__(self):
    return(f"Compaund Intrest :- {self.ci}")

  def __del__(self):
    self.p = 0
    self.r = 0
    self.n = 0
    self.a = 0
    self.ci = 0

p1 = float(input("Enter Principle :- "))
r1 = float(input("Enter Rate :- "))
n1 = float(input("Enter Time :- "))
obj = Ci(p1,r1,n1)
obj.calc()
print(obj)