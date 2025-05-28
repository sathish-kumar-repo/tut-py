s = "Sathish Kumar"
print(s)

# to check type
print(type(s))

# to transform the text
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())

# Return the count of String
print(s.count("h"))

# Return bool based upon program
print(s.endswith("ED"))

# Return index of String if does not exist it returns -1
print(s.find("s"))

# To search the letter after 5th index
print(s.find("s", 5))

# To replace the Character or String and it returns the String and it does affect the original String, it return String with Replace
print(s.replace("Sathish", "0"))

# Boolean Function
a = "sathish1234"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())

# Special Character
s = "he\nis\ngood"
print(s)

# Splitlines Function
print(s.splitlines())  # It returns List
print(s.splitlines(True))  # It returns List and element with


# Split the String Based upon space or any other delimiter
a = "Sathish Kumar Computer Education"
print(a.split(" "))
a = "Sathish,Kumar,Computer,Education"
print(a.split(","))


s = "    Sathish     "

# To return the lenght of String
print(len(s))

# To remove unwanted white space
print(len(s.strip()))

# To remove left unwanted white space
print(len(s.lstrip()))

# To remove right unwanted white space
print(len(s.rstrip()))

# Partition Function
s = "12-03-2020"
print(s.partition("-"))

s1 = "Sathish|kumar|is|a|programmer"
print(s1.partition("|"))

# String Manipulation
"""
 S  a  m  p  l  e
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
"""

s = "sample"
print(s)

"""String Slicing"""
# Slice first 2 character
print(s[0:2])

# Slice first 5 character
print(s[:5])

# Slice the full String after index 1
print(s[1:])

# Slice the last Character
print(s[-1])

# to last before character
print(s[-3:-1])

# To print all character expect last character
print(s[:-1])

# Print Reverse
print(s[::-1])
