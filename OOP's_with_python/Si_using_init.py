class SI:
  def __init__(self,p1,r1,t1):
    self.p = p1
    self.r = r1
    self.t = t1

  def calc(self):
    self.si = (self.p*self.r*self.t)/100

  # def disp(self):
  #   print(f"Simple Intrest :- {self.si}")
  def __str__(self):
    return(f"Simple Intrest :- {self.si}")

# main()
p = float(input("Enter Principle :- "))
r = float(input("Enter Rate :- "))
t = float(input("Enter Time :- "))

o = SI(p,r,t)
o.calc()
print(o)