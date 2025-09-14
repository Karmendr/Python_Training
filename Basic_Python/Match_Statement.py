n = int(input("Enter a Number (1-3) :- "))
match n:
  case 1:
    print("One")
  case 2:
    print("Two")
  case 3:
    print("Three")
  case _:
    print("Number is Not match")