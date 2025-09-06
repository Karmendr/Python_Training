class Abc:
  def __init__(self):
    self.name="Raj"
    self.age=23
obj=Abc()
print(hasattr(obj,"name"))
k = getattr(obj,"age")
setattr(obj,"rolln",25)
print(hasattr(obj,"rolln"))
delattr(obj,"rolln")
print(hasattr(obj,"rolln"))