def simple_int(p1,r1,t1):
  si = (p1*r1*t1)/100
  return si

#main()

p = float(input("Enter Principle :- "))
r = float(input("Enter Rate :- "))
t = float(input("Enter Time :- "))

si = simple_int(p,r,t)
print(f"Simple Intrest :- {si}")