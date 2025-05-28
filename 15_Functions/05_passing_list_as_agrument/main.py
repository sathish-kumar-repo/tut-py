# Passing a List as an Argument in Function Python


def total(marks: list):
    print(marks)
    return sum(marks)


print("Total : ", total([55, 75, 80, 95, 47]))
