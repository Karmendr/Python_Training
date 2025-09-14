import SI_Func
p = float(input("Enter Principle :- "))
r = float(input("Enter Rate :- "))
t = float(input("Enter Time :- "))

si = SI_Func.si_int(p,r,t)
print(f"Simple Intrest :- {si}")