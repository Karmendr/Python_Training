def add(x,y):
  return x+y

def sub(x,y):
  return x-y

def multi(x,y):
  return x*y

def divid(x,y):
  return(x/y)

n = 1
while n==1:
  print("Available Operations :- (+,-,*,/)")
  a = int(input("Enter First Number :- "))
  b = int(input("Enter Second Number :- "))
  choice = input("Enter your choice :- ")
  
  if(choice=="+"):
    c = add(a,b)
    print(f"{a} + {b} = {c}")
  elif(choice=="-"):
    c = sub(a,b)
    print(f"{a} - {b} = {c}")
  elif(choice=="*"):
    c = multi(a,b)
    print(f"{a} * {b} = {c}")
  elif(choice=="/"):
    c = divid(a,b)
    print(f"{a} / {b} = {c}")
  else:
    print("Please Enter Valid Input")
  n = int(input("if you want to exit from code then Enter 0 \nif you want to continou the code then Enter 1\n"))