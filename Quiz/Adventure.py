name = input("Enter your name to continue with the game: ")
print("Welcome", name, "to this Adventure!")

answer = input("You are on a dirt road, it has come to an end, and you can go left or right. Which way would you like to go? (left/right): ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You came to a bridge that looks wobbly. Do you want to go across it or head back? (cross/back): ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger. Do you talk to them? (yes/no): ").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!!")
        elif answer == "no":
            print("You ignore the stranger. They are offended, and you lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name + "!")
