import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a valid number next time.")
    quit()

random_number = random.randint(0, top_of_range)
print(f"A random number between 0 and {top_of_range} has been generated.")

guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess < 0:
            print("Please type a number larger than 0.")
            continue

        # Compare user_guess with random_number
        if user_guess == random_number:
            print("Congratulations! You got it in ",guesses "guesses.")
            break
        elif user_guess < random_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")
    else:
        print("Please type a valid number.")
        