with open("sample.txt", "r") as file:
    content = file.read()  # Read the file contents
    print(content)         # Print the content

with open("sweet.txt", "w") as file:
    file.write("Hello, Python!")
