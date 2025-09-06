count = 10
i = 1
while i <= 4:
  j = 1
  while j<=i:
    print("%d"%count,end=" ")
    j+=1
    count-=1
  print(" ")
  i+=1