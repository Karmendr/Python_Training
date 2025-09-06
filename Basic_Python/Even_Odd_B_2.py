a = int(input("Enter frist number :- "))
b = int(input("Enter second number :- "))

e_count = 0
for i in range(a, b):
  if (i % 2) == 0:
    e_count = e_count + 1
    print(i, " is Even")
print("Even :- ", e_count)

o_count = 0
for j in range(a, b):
  if (j % 2) != 0:
    o_count = o_count + 1
    print(j, " is Odd")
print("Odd :- ", o_count)
