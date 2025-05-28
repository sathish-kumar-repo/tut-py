"""
is
is not
"""

a = [1, 2]
b = [1, 2]
c = a
print(id(a))  # two object instance show same memory location
print(id(c))  # two object instance show same memory location
print(id(b))

# To check the object instance are equal or not
print(a is c)
print(a is b)

# To check the value are equal or not
print(a == b)

# Opposite
print(a is not c)
print(a is not b)
print(a != b)
