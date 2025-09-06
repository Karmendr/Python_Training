s = "karmendr Deval"

# 1. s.capitalize() -> convert fist latter in capital
print(s.capitalize())

# 2. s.len() -> find length and return int
print(len(s))

# 3. s.upper() -> convert capital latters of whole string
print(s.upper())

# 4. s.lower() -> convert lower latters of whole string
print(s.lower())

# 5. s.replace(old,new) -> replace string and return a new string
print(s.replace("karmendr","Rohit"))

# 6. s.count() -> it is count a repitative element in a string
print(s.count("a"))

# 7. s.find() -> find index of element, but if element is not present in string then it return -1, it's not throw the error.
print(s.find("v"))

# 8. s.rfind() -> fing index of element in a string from right to left. 
print(s.rfind("D"))

# 9. s.index() -> find index of element, but if element is not present in string then it throw error.
print(s.index("a"))