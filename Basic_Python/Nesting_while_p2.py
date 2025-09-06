i = 1
count = 1
while i <= 4:
  j = 1
  while j <=i-1:
    print(" ",end=" ")
    j+=1
  k = 1
  while k <= 5-i:
    print("%d"%count,end=" ")
    count+=1
    k+=1
  print(" ")
  i+=1