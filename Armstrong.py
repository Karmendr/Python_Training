n = int(input("Enter a number :- "))
s = 0
v = n
while n!=0:
  k = n%10
  s = s+k*k*k
  n = n//10
if v == s:
  print("Armstrong Number")
else:
  print("Not Armstrong Number")