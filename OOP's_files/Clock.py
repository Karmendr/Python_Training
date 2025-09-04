import time
<<<<<<< HEAD
import os
class Clock:
  __h = 0
  __m = 0
  __s = 0
  
  # def __init__(self,h,m,s):
  #   self.__h = h
  #   self.__m = m
  #   self.__s = s

  def disp(self):
    for i in range(0,23):
      for j in range(0,59):
        for k in range(0,59):
          time.sleep(1)
          os.system('cls')
          return(f"{self.__h}:{self.__m}:{self.__s}")

obj = Clock()
print(obj.disp())
=======


class Clock:

  def __init__(self, h, m, s):
    self.__h = h
    self.__m = m
    self.__s = s
    self.__day = 0

  def disp(self):
    while (True):
      for i in range(self.__h, 24):
        for j in range(self.__m, 60):
          for k in range(self.__s, 60):
            # print(f"{i}:{j}:{k}","\n",end="")
            if self.__day > 0:
              print("%2dday:%2d:%2d:%2d" % (self.__day, i, j, k),
                    "\r",
                    end="")
              time.sleep(1)
              if (i == 23 and j == 59 and k == 59):
                i = 0
                j = 0
                k = 0
                self.__h = 0
                self.__m = 0
                self.__s = 0
            else:
              print("%2d:%2d:%2d" % (i, j, k), "\r", end="")
              time.sleep(1)
              if (i == 23 and j == 59 and k == 59):
                i = 0
                j = 0
                k = 0
                self.__h = 0
                self.__m = 0
                self.__s = 0

      self.__day += 1


h = int(input("Enter hour :- "))
m = int(input("Enter minuts :- "))
s = int(input("Enter seconds :- "))
obj = Clock(h, m, s)
obj.disp()
>>>>>>> 4e95930 (03/09/25)
