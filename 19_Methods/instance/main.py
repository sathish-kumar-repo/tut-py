# instance Methods
class Student:
    name = "Sathish kumar"
    age = 25

    # This is instance method
    def printall(self, gender: str):
        print("Name : ", Student.name)
        print("Age  : ", Student.age)
        print("Gender  : ", gender)


o = Student()

"""
o.printall()
Student.printall(o)
"""

o.printall("Male")
Student.printall(o, "Male")
