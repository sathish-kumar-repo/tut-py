names = {"Ram", "Sam", "Ravi"}
print(names)
print(type(names))

# Access Values Using For loop
for name in names:
    print(name)

# Adding New Element
names.add("Sara")
print(names)

# Update Another Set of Data
a = {"Kumar", "Sundar", "Suresh"}
names.update(a)
print(names)

# To remove the element
names.remove("Sara")
print(names)

#! This function like as remove but remove function show exception if the removed element does not exist but discard function not show error if the element does not exist
names.discard("Suresh")
print(names)

# To remove last index last of element but set is unorder and unindexed so , pop function remove random element in set
names.pop()
print(names)

# To clear all the elements in Sets
names.clear()
print(names)

# To delete the set
del names
# print(names)

names = {"Ram", "Ram", "Sam", "Ravi", "Kumar", "Sundar", "Suresh"}
print(names)

# Union is set
a = {1, 2, 3, 4}
b = {"a", "b", "c", "d"}
c = a.union(b)
print(c)

# Union and Update the existing Set
a.update(b)
print(a)

# Intersection is set
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
c = a.intersection(b)
print(c)

# Intersection and Update the existing Set
a.intersection_update(b)
print(a)

# Symmetric difference is set
c = a.symmetric_difference(b)
print(c)

# Symmetric difference and Update the existing Set
a.symmetric_difference_update(b)
print(a)

# Boolean Functions
a = {5, 6, 7}
b = {5, 6, 7}

c = a.isdisjoint(b)
print(c)

c = a.issubset(b)
print(c)

c = a.issuperset(b)
print(c)
