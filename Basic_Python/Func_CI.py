from math import pow


def ci_int(p1, r1, n1):
  a = p1 * pow((1 + r1 / 100), n1)
  ci = a - p1
  return ci


# main()

p = float(input("Enter Principle :- "))
r = float(input("Enter Rate :- "))
n = float(input("Enter Time :- "))

ci = ci_int(p, r, n)
print(f"Compound Intrest :- {ci}")
