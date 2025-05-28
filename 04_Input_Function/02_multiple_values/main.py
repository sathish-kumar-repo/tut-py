# Multiple Values in Single Line

name1, name2, name3 = input("Enter 3 Names : ").split()
print("Name 1 : ", name1)
print("Name 2 : ", name2)
print("Name 3 : ", name3)

name1, name2, name3 = input("Enter 3 Names : ").split(",")
print("Name 1 : ", name1)
print("Name 2 : ", name2)
print("Name 3 : ", name3)
