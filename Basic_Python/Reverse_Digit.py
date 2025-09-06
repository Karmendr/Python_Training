n = int(input("Enter a number :- "))
s = 0
v = n

while n!=0:
  k = n%10
  s = s*10+k
  n = n//10
print(s)