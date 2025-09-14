import os

class File_Handling:

  def create_file(self, filename):
    try:
      with open(filename, 'x') as f:
        print(f"{f} created")
    except FileExistsError:
      print(f"{filename} already exists")
    except Exception:
      print("An error")

  def read_file(self, filename):
    try:
      with open(filename, 'r') as f:
        print(f.read())
    except FileNotFoundError:
      print("File not found")

  def read_dir(self):
    try:
      files = os.listdir()
      if not files:
        print("File not Found")
      else:
        print("Files in Directory!")
        for file in files:
          print(file)
    except FileNotFoundError:
      print("Please Enter valid Path")

  def add_contant(self, filename):
    try:
      with open(filename, 'a+') as f:
        f.write(input("Enter your data :- "))
    except FileNotFoundError:
      print("File Not Found")

  def delete_file(self, filename):
    try:
      os.remove(filename)
      print(f"{filename} is successfully deleted")
    except FileNotFoundError:
      print("File Not Found")
    except Exception:
      print("an error accurred")


class File_menu(File_Handling):

  def __init__(self, n):
    match (n):
      case 1:
        super().read_dir()
      case 2:
        filename = input("Enter file name :- ")
        super().create_file(filename)
      case 3:
        filename = input("Enter file name :- ")
        super().read_file(filename)
      case 4:
        filename = input("Enter file name :- ")
        super().add_contant(filename)
      case 5:
        filename = input("Enter file name :- ")
        super().delete_file(filename)
      case _:
        print("Select valid Options")


# main()
while True:
  print("1. Print Total files")
  print("2. Create new file")
  print("3. Read file")
  print("4. Add Contant of a file")
  print("5. Delete a file")
  print("6. Exit")
  n = int(input("Enter your choice :- "))
  if n == 6:
    break
  else:
    File_menu(n)
