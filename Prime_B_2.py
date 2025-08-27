n1 = int(input("Enter first Number :- "))
n2 = int(input("Enter second Number :- "))

prime = 0
n_prime = 0
if n1==1:
  print("%d"%n1," is Not Prime Number")
  n1+=1
for i in range(n1,n2):
  for j in range(2,i):
    if (i%j)==0:
      print("%d"%i," is Not Prime Number")
      n_prime+=1
      break
    else: 
      j+=1
  else:
    print("%d"%i," is Prime Number")
    prime+=1
  i+=1
print("Total Prime :- %d"%prime)
print("Total Not Prime :- %d"%n_prime)