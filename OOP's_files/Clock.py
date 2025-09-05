import time


class Clock:

  def __init__(self, h, m, s, am_pm):
    if ((h >= 0 and h <= 12) and (m >= 0 and m <= 59)
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
            if self.__am_pm == self.__am:
              print("%2dday :%2d:%2d:%2d %2s" %
                    (self.__day, i, j, k, self.__am_pm),
                    "\r",
                    end="")
              time.sleep(1)
              if (i == 12 and j == 59 and k == 59):
                i = 0
                j = 0
                k = 0
                self.__h = 0
                self.__m = 0
                self.__s = 0
                self.__am_pm = self.__pm
                self.__day += 1
            elif self.__am_pm == self.__pm:
              print("%2dday %2d:%2d:%2d %2s" %
                    (self.__day, i, j, k, self.__am_pm),
                    "\r",
                    end="")
              time.sleep(1)
              if (i == 12 and j == 59 and k == 59):
                i = 0
                j = 0
                k = 0
                self.__h = 0
                self.__m = 0
                self.__s = 0
                self.__am_pm = self.__am
            else:
              print("Please Enter Valid Input")
              return


try:
  h = int(input("Enter hour :- "))
  m = int(input("Enter minuts :- "))
  s = int(input("Enter seconds :- "))
  try:
    am_pm = input("AM or PM :- ")
    obj = Clock(h, m, s, am_pm)
    obj.disp()
  except (ValueError):
    print("Please Enter AM & PM in capital latter")
except (ValueError):
  print("Please Enter Valid input")
