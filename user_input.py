#user input
 
# Ask for user name
name = input("What is your name ?")

#Ask for user age
age =  input("What is your age ?")

#Ask user's location 
location = input("Where do you live?")

#print personal info
print(f"Hello {name}, you are {age}, years old and i suppose you stay in {location}")


number = int(input('Enter your Admission number here :'))

#check if the number is valid
if number > 0 :
    print(f'{number} is now fully registered to the system.')
    else {
print('Number input is invalid cannot be registered to our systems.')
    }