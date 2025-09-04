class Palindrome:
  str2 = ""

  def checkPalindrome(self, str1):
    self.str2 = str1[::-1]
    if (self.str2 == str1):
      print(f"{str1} is Palindrome")
    else:
      print(f"{str1} is Not Palindrome")


str1 = input("Enter a word for check Palindrome :- ")
obj = Palindrome()
obj.checkPalindrome(str1)
