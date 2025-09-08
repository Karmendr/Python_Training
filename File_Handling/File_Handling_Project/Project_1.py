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

  def wirte_file(self, filename):
    try:
      with open(filename, 'w+') as f:
        f.write(input("Write your Contant"))
    except FileNotFoundError:
      print("File not fond")

  def read_file(self, filename):
    try:
      with open(filename, 'r') as f:
        print(f.read())
    except FileNotFoundError:
      print("File not found")

  def read_dir(self, path):
    try:
      files = os.listdir(path)
      print(files)
      print(f"Total Files :- {len(files)}")
    except FileNotFoundError:
      print("Please Enter valid Path")

  def edit_file(self,filename):
    try:
      with open(filename,'a+') as f:
        f.write(input())
    except FileNotFoundError:
      print("File Not Found")

class File_menu(File_Handling):

  def __init__(self, n):
    match (n):
      case 1:
        path_of_dir = input("Enter Path :- ")
        p = "/home/runner/workspace/"+path_of_dir
        super().read_dir(p)
      case 2:
        filename = input("Enter file name :- ")
        super().create_file(filename)
      case 3:
        filename = input("Enter file name :- ")
        super().wirte_file(filename)
      case 4:
        filename = input("Enter file name :- ")
        super().read_file(filename)
      case 5:
        filename = input("Enter file name :- ")
        super().edit_file(filename)
      case _:
        print("Select valid Options")


# main()
print("1. Print Total files")
print("2. Create new file")
print("3. Write contant file")
print("4. Read file")
print("5. Edit Contant of a file")
n = int(input("Enter your choice :- "))
File_menu(n)