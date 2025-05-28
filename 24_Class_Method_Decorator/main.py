# Class Method Decorator
class student:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.count += 1

    def printDetail(self):
        print("Name  : ", self.name, "  Age : ", self.age)

    @classmethod
    def total(cls):
        print(cls)
        return cls.count


o = student("Sathish", 25)
o.printDetail()
a = student("Raja", 45)
a.printDetail()

# Also use object to call the functions and object also access the class variable
print("Total Admission :", student.total())
print("Total Admission :", o.total())
