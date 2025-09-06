l = eval(input("Enter a list :- "))
s_odd = 0
s_even = 0
for i in l:
  if(i%2==0):
    s_even+=i
  else:
    s_odd+=i
print(f"Sum of Even Elements :- {s_even}")
print(f"Sum of Odd Elements :- {s_odd}")