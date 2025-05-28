# No Return Type Without Argument Function
def add():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a + b
    print("Total ", c)


add()


# No Return Type With Argument Function
def sub(a: int, b: int):
    c = a - b
    print("Difference : ", c)


sub(25, 2)


# Return Type Without Argument Function
def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c


x = mul()
print("Mul ", x)


# Return Type With Argument Function
def div(a: int, b: int):
    c = a / b
    return c


x = div(25, 2)
print("Division ", x)


# Default Parameter Function
def user(name, city="Salem"):
    print(name, " is from ", city)


user("Ram", "Namakkal")
user("Sam")
