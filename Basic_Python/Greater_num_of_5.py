a = int(input("Enter first number :- "))
b = int(input("Enter second number :- "))
c = int(input("Enter third number :- "))
d = int(input("Enter fourth number :- "))
e = int(input("Enter fifth number :- "))

if a>b:
  if a>c:
    if a>d:
      if a>e:
        print(a," is greater")
      else:
        print(e," is greater")
    elif d>e:
      print(d," is greater")
    else:
      print(e," is greater")
  elif c>d:
    if c>e:
      print(c," is greater")
    else:
      print(e," is greater")
  elif d>e:
    print(d," is greater")
  else:
    print(e," is greater")
elif b>c:
  if b>d:
    if b>e:
      print(b," is greater")
    else:
      print(e," is greater")
  elif d>e:
    print(d," is greater")
  else:
    print(e," is greater")
elif c>d:
  if c>e:
    print(c," is greater")
  else:
    print(e," is greater")
elif d>e:
  print(d," is greater")
else:
  print(e," is greater")   