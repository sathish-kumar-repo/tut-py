# Read the file

try:
    f = open("ram.txt", "r")

    # Read Complete file
    print(f.read())

    # Read line by line
    print(f.readline())

    # Read First 2 Character
    print(f.readline(2))

    # Return list of all data
    print(f.readlines())

    # Read file using a for loop
    for line in f:
        print(line)


except FileNotFoundError:
    print("File not Found")
else:
    print("Thank You")
    f.close()  # Dispose the object

# -------------------------------------------

# Write the File
try:
    f = open("ram.txt", "w")

    # Write the file (this is overwrite the file)
    f.write("\nThis is New Line")


except FileNotFoundError:
    print("File not Found")
else:
    print("Thank You")
    f.close()

# -------------------------------------------

# Append the File
try:
    f = open("ram.txt", "a")

    # Add new line to end of the file
    f.write("\nThis is New Line")


except FileNotFoundError:
    print("File not Found")
else:
    print("Thank You")
    f.close()

# -------------------------------------------

# Delete the File

import os  # to get current system permission

if os.path.exists("ram.txt"):
    os.remove("ram.txt")
    # to remove folder
    os.rmdir("folder_name")
else:
    print("File Not Found")
