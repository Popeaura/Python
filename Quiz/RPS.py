import random

user_wins = 0
computer_wins = 0

options =  ["Rock", "Paper", "Scissors"]

while True:
    user_input = input("Type Rock/Paper/scissors or Q to quit : ").lower()
    if user_input ==  "q": 
        break

    if user_input not in options:
        continue

    random_number = random.int(0, 2) 
    #   rock: 0, paper:1 , scissors: 2


print("Goodbye !")    
