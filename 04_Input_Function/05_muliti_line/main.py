# Multiple Line String Input

a = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
"""
print(type(a))
print(a)


para = []
print("Enter a Para : ")

while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
print(para)
output = "\n".join(para)

print(output)
