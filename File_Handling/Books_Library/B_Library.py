import os


class Books:

  def add_book(self, bookname):
    try:
      with open(bookname, 'x') as b:
        print(f"{b} is created")
    except FileExistsError:
      print("Book is already Exist!")
    except Exception:
      print("an error accurred!")

  def all_booklist(self):
    b_list = os.listdir()
    if not b_list:
      print("Books not found!")
    else:
      b_count = 0
      for book in b_list:
        if book == "B_Library.py":
          continue
        else:
          b_count += 1
          print(f"{b_count}. {book}")
      print(f"Total Books in Library :- {b_count}")

  def raed_book(self, bookname):
    try:
      with open(bookname) as f:
        k = f.readlines()
        print(k)
    except FileNotFoundError:
      print("File is not found")
    except Exception:
      print("an error accurred!")


# main()
obj = Books()
while True:
  print("1. See all Book's available in Library")
  print("2. Read a Book")
  print("3. Add a new Book")
  print("4. Exit")
  n = int(input("Enter your Choice (1-4) :- "))

  if n == 1:
    obj.all_booklist()
  elif n == 2:
    bookname = input("Enter Book Name :- ")
    obj.raed_book(bookname)
  elif n == 3:
    bookname = input("Enter Book Name :- ")
    obj.add_book(bookname)
  elif n == 4:
    break
  else:
    print("Enter valid Input !")
