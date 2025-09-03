import time
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