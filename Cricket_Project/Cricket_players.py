import pandas as pd
import os

class Cricketplayers:

  def writeData(self, filename):
    try:
      with open(filename, 'w') as f:
        f.write(input("Write your data :- "))
        print("Your data is added successfully!")
    except FileNotFoundError:
      print(f"{filename} is Not Found!")
    except Exception as e:
      print(e)

  def createNewFile(self, filename):
    try:
      with open(filename, 'x'):
        print(f"{filename} is Successfully Created!")
    except FileExistsError:
      print(f"{filename} is already Exist")
    except Exception as e:
      print(e)

  def readData(self, filename):
    try:
      count = 0
      words = list()
      with open(filename, "r") as f:
        for line in f:
          words = line.split()
          count += len(words)
      nlist = list(range(1, len(words) + 1))
      data = {"sn": nlist, "players_name": words}
      df = pd.DataFrame(data)
      print("--------------------------------------")
      print("sn   players_name")
      for i in range(len(df)):
        print(f"{df['sn'][i]}    {df['players_name'][i]}")
      print("--------------------------------------")
    except FileNotFoundError:
      print(f"{filename} is not found!")
    except Exception as e:
      print(e)

  def appendData(self, filename):
    try:
      with open(filename, 'a+') as f:
        f.write(" " + input("Apppend Data :- "))
        print("data append successfully!")
    except FileNotFoundError:
      print("File not found!")
    except Exception as e:
      print(e)

  def countLineAndWords(self, filename):
    try:
      line_count = 0
      word_count = 0
      with open(filename, 'r') as f:
        for line in f:
          line_count += 1
          words = line.split()
          word_count += len(words)
      print(f"Number of Line :- {line_count}")
      print(f"Numbe of Words :- {word_count}")
    except FileNotFoundError:
      print("File Not found!")
    except Exception as e:
      print(e)

  def viewFileList(self):
    try:
      file_list = os.listdir()
      if len(file_list) > 0:
        for file in file_list:
          if file == "Cricket_players.py":
            continue
          else:
            print(file)
      else:
        print("Empty Diractory!")
    except Exception as e:
      print(e)


obj = Cricketplayers()
while True:
  print("1. View Available Files ")
  print("2. Create New File ")
  print("3. Write data to the file")
  print("4. Read data from the file")
  print("5. Append data to the file")
  print("6. Count number of lines and words in the file")
  print("7. Exit ")
  n = int(input("Enter Your Choice :- "))

  if n == 1:
    obj.viewFileList()
  elif n == 2:
    filename = input("Enter File Name :- ")
    obj.createNewFile(filename)
  elif n == 3:
    filename = input("Enter File Name :- ")
    obj.writeData(filename)
  elif n == 4:
    filename = input("Enter File Name :- ")
    obj.readData(filename)
  elif n == 5:
    filename = input("Enter File Name :- ")
    obj.appendData(filename)
  elif n == 6:
    filename = input("Enter File Name :- ")
    obj.countLineAndWords(filename)
  elif n == 7:
    break
  else:
    print("Entre Valid Input!")
