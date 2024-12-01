print("Welcome to my computer quiz!")

play = input("Do you want to play my game? ").lower()

if play != "yes":
    quit()

print("Okay, let's play :)")
score = 0

# Question 1
answer = input("Which team has won the most Premier League titles? ").lower()
if answer == "manchester united":
    print("Correct!")
    score += 1
else:
    print("Incoryesrect!")

# Question 2
answer = input("Who is the all-time top scorer in the Premier League? ").lower()
if answer == "alan shearer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("Which player holds the record for the most assists in a single Premier League season? ").lower()
if answer == "kevin de bruyne":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("Which team went unbeaten for an entire Premier League season, earning the nickname The Invincibles? ").lower()
if answer == "arsenal":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 5
answer = input("Who was the first player to score five goals in a single Premier League match? ").lower()
if answer == "andy cole":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 6
answer = input("Which goalkeeper has the most clean sheets in Premier League history? ").lower().replace("č", "c")
if answer == "petr cech":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 7
answer = input("Who was the first manager to win the Premier League Manager of the Season? ").lower()
if answer == "sir alex ferguson":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 8
answer = input("Which team holds the record for the longest winning streak in a single Premier League season? ").lower()
if answer == "manchester city":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 9
answer = input("Who was the first African player to win the Premier League Golden Boot? ").lower()
if answer == "didier drogba":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Question 10
answer = input("Which Premier League club has the nickname The Toffees? ").lower()
if answer == "everton":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Display final score
print("You got"   +   str(score) +  "questions correct!")

print("You got"   +    str(score /10 *100) + "%.")
