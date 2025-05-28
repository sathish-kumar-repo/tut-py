# List in Python
"""
Sequence Type
Mutable
a[5]
a={1,2,3,4,5}
a[0]
"""

# Declare the List
a = [1, 2, 3, 4, 5]
print(a)

# To check the Type
print(type(a))

# To change the value in particular imdex
a[0] = 100
print(a)

# Slicing the List
print("Slicing")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

print("-----------------------------")

# Array can store any value
a = [1, True, "Ram", 2.5, [1, 2, 3, 4]]
print(a)
print(type(a))

# To access the List element
print(a[0], " type is ", type(a[0]))
print(a[1], " type is ", type(a[1]))
print(a[2], " type is ", type(a[2]))
print(a[3], " type is ", type(a[3]))
print(a[4], " type is ", type(a[4]))

# To access the element in nested list
print(a[4][1])

print("-----------------------------")

a = [10, 25, 35, 45]
print(a)
a.clear()
print(a)

# To Take clone
a = [10, 25, 35, 45]
b = a.copy()
print(b)

a = [10, 25, 35, 45, 25, 4, 25]

# Return how many element are in List
print(a.count(25))

# Return index based upon value and only find first occurence
print(a.index(25))

# Return Length of List
print(len(a))

# To return max and min element in List
print(max(a))
print(min(a))
print(a)

# remove Element using index
a.pop(0)
print(a)

# remove Element using Values and remove first occurence
a = [10, 25, 35, 45, 25, 4, 25]
a.remove(25)
print(a)

print("-----------------------------")

names = ["Ram"]
print(names)
# To add element at end of List
names.append("Sam")
names.append("Ravi")
names.append("Kumar")
print(names)

# To add multiple element in List
name2 = ["Sara", "Anitha"]
names.extend(name2)

# To add element at particular index
print(names)
names.insert(0, "Suriya")
print(names)

print("-----------------------------")

# List of number from 0  to 4
print(list(range(5)))

# List of Character
print(list("Sathishkumar"))


a = [10, 50, 100, 25, 85]
print(a)

# Sort the List => default is asscending order
a.sort()
print(a)

# Sort the List in descending order
a.sort(reverse=True)
print(a)

#  Similarly for String
a = ["Orange", "Apple", "Zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# To sort the Array based upon size
a = ["Orange", "Apple", "Zebra"]
a.sort(key=len)
print(a)
