import time


class Clock:

  def __init__(self, h, m, s, am_pm):
    if ((h >= 1 and h <= 12) and (m >= 0 and m <= 59)
        and (s >= 0 and s <= 59)):
      self.__h = h
      self.__m = m
      self.__s = s
      self.__am_pm = am_pm
      self.__am = "AM"
      self.__pm = "PM"
      self.__day = 0
    else:
      print("Please Enter Valid input")

  def disp(self):
    while (True):
      for i in range(self.__h, 13):
        for j in range(self.__m, 60):
          for k in range(self.__s, 60):
            print("%2dday :%2d:%2d:%2d %2s" %
                  (self.__day, i, j, k, self.__am_pm),
                  "\r",
                  end="")
            time.sleep(1)
            if (i == 12 and j == 0 and k == 0):
              if (self.__am_pm == self.__am):
                self.__am_pm = self.__pm
              else:
                self.__am_pm = self.__am
                self.__day += 1
            if (i == 12 and j == 59 and k == 59):
              self.__h = 1
              self.__m = 0
              self.__s = 0
              break
            if (i == 12 and j == 0):
              break
          if (i == 12):
            break


try:
  h = int(input("Enter hour (1 to 12) :- "))
  m = int(input("Enter minuts :- "))
  s = int(input("Enter seconds :- "))
  try:
    am_pm = input("Enter AM or PM in capital latter:- ")
    obj = Clock(h, m, s, am_pm)
    obj.disp()
  except (ValueError):
    print("Please Enter AM & PM in capital latter")
except (ValueError):
  print("Please Enter Valid input")
