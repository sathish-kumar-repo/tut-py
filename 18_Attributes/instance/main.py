"""
Namespace are availble in class and instance of class
"""


class user:
    # Class Attribute
    course = "Java"


# Create instance of class
o = user()

print(user.__dict__)

# Print Class attribute
print(user.course)

print(o.__dict__)

# To set attribut in instance
print(o.course)
o.course = "C++"

print(o.__dict__)
print(o.course)


o2 = user()
print(o2.course)
