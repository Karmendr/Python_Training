l = eval(input("Enter a List :- "))
g = l[0]
for i in l:
  if i>g:
    g = i
print("%d"%g)