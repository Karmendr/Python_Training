import random

print("--------Guess My Number--------")
low = int(input("Enter low number :- "))
high = int(input("Enter high number :- "))

print("---------------------------------")
print(f"Your Number is {low} and {high}")
print("---------------------------------")
num = random.randint(low, high)

ch = 7
gc = 0
r = ch-1
while gc < ch:
  gc += 1
  guess = int(input("Enter Your Guess Number :- "))
  if guess == num:
    print(f"{num}={guess}")
    print("You successfully Guess the Correct Number before your remaining chance is :- ",r)
    break
  elif gc >= ch and guess != num:
    print("NEXT TIME")
  elif guess > num:
    print("TOO High")
    print("You have remaining chance :- ",r)
    r-=1
  elif guess < num:
    print("TOO Low")
    print("You have remaining chance :- ",r)
    r-=1
