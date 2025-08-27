print("Simple Calculator")
print("Operation Available :- (add,sub,multi,div)")
try:
  a = int(input("Enter first Number :- "))
  b = int(input("Enter Second Number :- "))
  mode = input("Select mode (add,sub,multi,div) :-  ")
  
  if mode=="add":
    print("Result :- ",a+b)
  elif mode=="sub":
    print("Result :- ",a-b)
  elif mode=="multi":
    print("Result :- ",a*b)
  elif mode=="div":
    print("Result :- ",a/b)
  else: 
    print("Please Select given Mode only")
except ValueError:
  print("Please Select Numeric value only")