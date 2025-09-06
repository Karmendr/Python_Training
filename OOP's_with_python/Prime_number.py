class Prime:

  def __init__(self, n1):
    self.__n = n1

  def calc(self):
    for i in range(2, self.__n):
      if (self.__n%i) == 0:
        self.f = False
        break
      else:
        self.f = True

  def __str__(self):
    if self.f:
      return (f"{self.__n} is Prime Number ")
    else:
      return (f"{self.__n} is Not Prime Number ")


n = int(input("Enter a Number :- "))
obj = Prime(n)
obj.calc()
print(obj)
