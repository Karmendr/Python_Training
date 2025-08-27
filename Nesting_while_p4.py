i = 1
while i <= 4:
  j = 1
  while j <= i:
    if(j%2)==0:
      print("0",end=" ")
    else:
      print("1",end=" ")
    j+=1
  print(" ")
  i+=1