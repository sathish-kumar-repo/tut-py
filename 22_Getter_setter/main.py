# Property Decorators Getter Setter
class Student:
    def __init__(self, total):
        self.__total = total

    def average(self):
        return self.__total / 5.0

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, t):
        print("setter", t)
        if t < 0 or t > 500:
            print("Invalid Total and can't Change")
        else:
            self.__total = t


s = Student(450)
print("Total   : ", s.total)
print("Average : ", s.average())
s.total = 550
print("Total   : ", s.total)
print("Average : ", s.average())
