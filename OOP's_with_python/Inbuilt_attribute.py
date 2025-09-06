class Abc:
  """this is my Class"""
  def __init__(self,name,age):
    self.name = name
    self.age = age

name = input("Enter name :- ")
age = int(input("Enter age :- "))
obj = Abc(name,age)
print(obj.__doc__)
print(obj.__module__)
print(obj.__dict__)
print(Abc.__name__)
print(Abc.__base__)