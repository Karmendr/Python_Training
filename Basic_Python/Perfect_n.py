n = int(input("Enter a Number :- "))
count = 0
for i in range(1,n+1):
  if(n%i)==0:
    count+=i
per_n = n*2
if(per_n==count):
  print(f"{n} is Perfect Number")
else:
  print(f"{n} is Not Perfect Number ")