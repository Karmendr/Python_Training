class abc:
  def __init__(self):
    self.x = 10
    self.y = 20

  def disp(self):
    print(self.x)
    print(self.y)

class bbc(abc):
  def __init__(self):
    super().__init__()
    self.z = 200

  def disp1(self):
    super().disp()
    print(self.z)

o = bbc()
o.disp1()