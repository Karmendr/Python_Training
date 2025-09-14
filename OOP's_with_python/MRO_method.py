class First:

  def m(self):
    print("I'm in Class First")


class Second(First):

  # def m(self):
  #   print("I'm in Class Second")
  pass


class Thired(First):

  # def m(self):
  #   print("I'm in Class Thired")
  pass


class Four(Second, Thired):

  # def m(self):
  #   print("I'm in Class Four")
  pass


obj = Four()
obj.m()
