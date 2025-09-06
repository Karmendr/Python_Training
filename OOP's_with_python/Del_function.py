class abc:

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def calc(self):
    self.c = self.a + self.b

  def __str__(self):
    return (f"{self.c}")

  def __del__(self):
    self.a = 0
    self.b = 0
    self.c = 0


a = int(input("Enter first Number :- "))
b = int(input("Enter second Number :- "))
obj = abc(a, b)
obj.calc()
print(obj)
