name = input("Enter your name to continue with the game")
print("Welcome", name, "to this Adventure !")

answer =  input("You are on a dirt road it has come to an end and you can go left or right  ,which way would like to go ?").lower()


if answer == "left":
    answer = input("You come to a river you can walk around it or swim  to swim across ? Type walk around and to swim across: ")

if answer ==  "swim":
    print('You swam across and were eaten by alligator')

elif answer == "walk":
    print('You walked for many miles , ran out of water and yiu lost the game')

else:
    print('Not a valid option you lose')

elif answer == "right"
answer = input('You came to a bridge which looks wobbly do you want to go across it or head back(cross/back) ?')

if answer ==  "back":
    print('You  go back and just lost.')

elif answer == "across":
answer = input ()
else:
    print('Not a valid option you lose')


else:
    print('Not a valid option You Lose.')    
    