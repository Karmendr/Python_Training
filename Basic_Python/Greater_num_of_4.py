a = int(input("Enter first Number :- "))
b = int(input("Enter second Number :- "))
c = int(input("Enter third Number :- "))
d = int(input("Enter fourth Number :- "))

if a > b:
  if a > c:
    if a > d:
      print(a, " is greater")
    else:
      print(d, " is greater")
  elif c > d:
    print(c, " is greater")
  else:
    print(d, " is greater")
elif b > c:
  if b > d:
    print(b, " is greater")
  else:
    print(d, "is greater")
elif c > d:
  print(c, " is greater")
else:
  print(d, " is greater")
