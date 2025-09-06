l = eval(input("Enter a List :- "))
s = l[0]
for i in l:
  if(i<s):
    s = i
print("%d"%s)