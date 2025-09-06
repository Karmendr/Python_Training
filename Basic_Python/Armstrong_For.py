n = input("Enter a number :- ")
s = 0
v = int(n)
r = v
for i in range(1,len(n)+1):
  k = v%10
  s = s+k*k*k
  v = v//10
if s==r:
  print("Armstrong Number")
else:
  print("Not Armstrong Number")
  