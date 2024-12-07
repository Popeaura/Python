name = input("Enter your name to continue with the game")
print("Welcome", name, "to this Adventure !")

answer =  input("You are on a dirt road it has come to an end and you can go left or right  ,which way would like to go ?").lower()


if answer == "left":
    answer = input("You come to a river you can walk around it or swim  to swim across ? Type walk around and to swim across: ")

if answer ==  "swim":

elif answer == "walk":

else:
    print

elif answer == "right":
    print('Not a valid option you lose')

else:
    print('Not a valid option You Lose.')    
    