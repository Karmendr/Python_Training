# create a empty set -> set()
s = set()
# Set initialize with value
s = set({4,6,8,1})

# 1. s.add(value) -> Add new element at end 
s.add(3)
s.add(2)
print(s)

# 2. s.copy() -> Copy whole set
k = set()
print(k)
k = s.copy()
print(k)

# 3. s.clear() -> remove all set elements
k.clear()
print(k)

# 4. s.difference(k) -> check difference and return new set
k = set({2,4,5,7,10})
print(f"Set s :- {s} and Set k :- {k}")
print(f"S-K :- {s.difference(k)}")

# 5. s.difference_update() -> check difference and update elements
print(s)
s.difference_update(k)
print(s)

# 6. s.discard(value) -> remove a single element from a set. if the element is not present in set then it not throw the error.
s.discard(6)
print(s)
s.discard(10)
print(s)

# 7. s.remove(value) -> remove a single element from a set. if the element is not present in set then it throw the error.
s.remove(1)
print(s)
# s.remove(10)
# print(s)

# 8. a.intersection(b) -> find the common elements of both set and return a new set. 
a = set({1,8,2,5,3,6})
b = set({1,2,5,10,29,26})
c = a.intersection(b)
print(c)

# 9. a.intersection_update(b) -> find the common elements of both set and update.
print(a)
a.intersection_update(b)
print(a)

# 10. a.pop() -> remove randomly a single element from a set
print(a)
a.pop()
a.pop()
print(a)

# 11. b.union(d) -> collect all element of both set but repitative elements collect only one time. 
d = set({3,1,2,4,10,7,8})
print(b)
print(d)
print(f"Union of BUD :- {b.union(d)}")