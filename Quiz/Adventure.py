name = input("Enter your name to continue with the game")
print("Welcome", name, "to this Adventure !")

answer =  input("You are on a dirt road it has come to an end and you can go left or right  ,which way would like to go ?").lower()


if answer == "left":

elif answer == "right":

else:
    print('Not a valid option You Lose.')    