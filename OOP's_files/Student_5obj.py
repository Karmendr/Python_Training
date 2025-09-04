class Student:
  __name = ""
  __age = 0
  __class = 0
  __teacher = ""
<<<<<<< HEAD
  
=======

>>>>>>> 4e95930 (03/09/25)
  def __init__(self, name, age, st, teacher):
    self.__name = name
    self.__age = age
    self.__class = st
    self.__teacher = teacher

  def __str__(self):
    return (
        f"Name:- {self.__name}\nAge:- {self.__age}\nClass:- {self.__class}th\nTeacher:- {self.__teacher}"
    )

<<<<<<< HEAD
for i in range(1,6):
=======

for i in range(1, 6):
>>>>>>> 4e95930 (03/09/25)
  name = input("Enter Name :- ")
  age = int(input("Enter age :- "))
  st = int(input("Enter Class :- "))
  teacher = input("Enter Teacher name :- ")
<<<<<<< HEAD
  obj = Student(name,age,st,teacher)
  print(obj)
=======
  obj = Student(name, age, st, teacher)
  print(obj)
>>>>>>> 4e95930 (03/09/25)
