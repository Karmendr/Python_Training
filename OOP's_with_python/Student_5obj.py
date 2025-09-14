class Student:
  __name = ""
  __age = 0
  __class = 0
  __teacher = ""

  def __init__(self, name, age, st, teacher):
    self.__name = name
    self.__age = age
    self.__class = st
    self.__teacher = teacher

  def __str__(self):
    return (
        f"Name:- {self.__name}\nAge:- {self.__age}\nClass:- {self.__class}th\nTeacher:- {self.__teacher}"
    )


for i in range(1, 6):
  name = input("Enter Name :- ")
  age = int(input("Enter age :- "))
  st = int(input("Enter Class :- "))
  teacher = input("Enter Teacher name :- ")

  obj = Student(name, age, st, teacher)
  print(obj)
  obj = Student(name, age, st, teacher)
  print(obj)
