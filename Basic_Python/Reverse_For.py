n = input("Enter a Number :- ")

s = 0
v = int(n)

for i in range(1,len(n)+1):
  k = v%10
  s = s*10+k
  v = v//10

print(s)