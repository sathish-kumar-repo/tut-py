# Tuple in Python
# Immutable
# Surrounded by Round Brackets (1,1,5)

# To Store any type of value
a = (1, 2.5, True, "Ram")
print(a)

# To check the type
print(type(a))

# Slice the Tuple
print(a[1])
print(a[-1])
print(a[0:2])

# To convert tuple into list
b = list(a)
print(b)
b.append("Raja")
print(b)
print(type(b))

# To convert list into tuple
a = tuple(b)
print(a)
print(type(a))

# to print value in tuple using for loop
for i in a:
    print(i)

if "Raj" in a:
    print("Raja is Found")
else:
    print("Not Found")

# Find the length of tuple
print(len(a))

# to define single element in tuple
a = (1,)  # It is Tuple
print(type(a))
tup = 1  # It is Integer
print(type(tup))

# To delete the tuple
del a
# print(a)

# To concatenate the Tuple
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)

# To count the occurence
print(c.count(7))

# To create Nested Tuple
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
c = (a, b)
print(c)

# To access the value in tuple
print(c[0])
print(c[1])
print(c[0][1])

# Repetition the Tuple
x = ("Sathish",) * 10
print(x)

# To find max and min
a = (1, 2, 7, 4)
b = (5, 6, 7, 8)
print(min(a))
print(max(a))
