with open("sample.txt", "r") as file:
    content = file.read()  # Read the file contents
    print(content)         # Print the content

with open("sweet.txt", "w") as file:
    file.write("Hello, Python!")

# Read from the file
with open("sweet.txt", "r") as file:
    content = file.read()
    print(content)    

with open("sample.txt", "r") as file:
    data = file.read()
    print(data)

try:
    with open("prom.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file 'prom.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
