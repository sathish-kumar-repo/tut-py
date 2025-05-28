# Keys are unique
# To declare the Dictionarr=y
user = {
    "name": "Ram",
    "age": 25,
    "isMarried": True,
}
print(user)

# To check the Type
print(type(user))

# To access the value using key
print(user["name"])

# To access the value using key
print(user.get("age"))

# To get all keys in Dictionary
print(user.keys())

# To values all keys in Dictionary
print(user.values())

# To items(Keys and Values) all keys in Dictionary
print(user.items())

# To access dictionary using for loop

# To keys are access the in for loop
for x in user:
    print(x, " ", user[x])

# To access the values using for loop
for x in user.values():
    print(x)

# To access the keys using for loop
for x in user.keys():
    print(x)

# To access the values and keys using for loop
for x, y in user.items():
    print(x, y)  # (key,value)

# To check the particular index in Dictionary
if "gender" in user:
    print("Present")
else:
    print("Not Present")


# Changing Values in Dictionary
user.update({"gender": "male"})
print(user)

# Update value in particular keys
user["age"] = 35
print(user)

# To remove the particular index using pop
user.pop("age")
print(user)

# To clear all the datas in Dictionary
user.clear()
print(user)

# To delete the Dictionary
del user

# Nested Dictionary
users = {
    "user1": {
        "name": "Ram",
        "age": 25,
        "isMarried": True,
    },
    "user2": {
        "name": "SAm",
        "age": 35,
        "isMarried": False,
    },
}
print(users)

# To access the Dictionary
for user in users:
    # print(user["name"])
    print(user)
