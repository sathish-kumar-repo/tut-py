class Student:
    name = "Sathish Kumar"
    age = 25


# Attributes means variable or data

""" This is Class Attributes """

# To access the attribut using getattr method
print(getattr(Student, "name"))
print(getattr(Student, "age"))
print(getattr(Student, "gender", "No Such Attribute Found"))

# To access the attribut using Dot Notation
print(Student.name)
print(Student.age)

# Update Attribute to the class
setattr(Student, "name", "Sam")
print(Student.name)

# Set Attribute to the class using setattr method
setattr(Student, "gender", "Male")
print(Student.gender)

# Set Attribute to the class using Dot notation
Student.city = "Salem"
print(Student.city)

# Store attributes and Functions like Dictionary form that is MappingProxyObject( or Type)
print(Student.__dict__)

# To delete the attrubute in Class using delattr method
delattr(Student, "city")
print(Student.__dict__)

# To delete the attrubute in Class using Dot Notation and del command
del Student.gender
print(Student.__dict__)

"""
MappingProxyType . This type is a read-only proxy for a dict or other mapping. Python uses this type internally for important dictionaries, which is why you can't monkey-patch built-in types willy-nilly. The only change in Python 3.3 was to expose this type for user code.05
"""
