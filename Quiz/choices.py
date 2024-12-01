def main():
    questions = [
        {
            "question": "Which team has won the most Premier League titles?",
            "options": ["Liverpool", "Manchester City", "Arsenal", "Manchester United"],
            "correct_option": 4
        },
        {
            "question": "Who is the all-time top scorer in the Premier League?",
            "options": ["Alan Shearer", "Wayne Rooney", "Sergio Agüero", "Thierry Henry"],
            "correct_option": 1
        },
        {
            "question": "Which player holds the record for the most assists in a single Premier League season?",
            "options": ["Kevin De Bruyne", "Cesc Fàbregas", "Mesut Özil", "Thierry Henry"],
            "correct_option": 1
        },
        {
            "question": "Which team went unbeaten for an entire Premier League season, earning the nickname 'The Invincibles'?",
            "options": ["Chelsea", "Liverpool", "Arsenal", "Manchester United"],
            "correct_option": 3
        },
        {
            "question": "Who was the first player to score five goals in a single Premier League match?",
            "options": ["Andy Cole", "Sergio Agüero", "Alan Shearer", "Dimitar Berbatov"],
            "correct_option": 1
        },
        {
            "question": "Which goalkeeper has the most clean sheets in Premier League history?",
            "options": ["Petr Čech", "David de Gea", "Edwin van der Sar", "Peter Schmeichel"],
            "correct_option": 1
        },
        {
            "question": "Who was the first manager to win the Premier League Manager of the Season award?",
            "options": ["Arsène Wenger", "Sir Alex Ferguson", "Kenny Dalglish", "José Mourinho"],
            "correct_option": 2
        },
        {
            "question": "Which team holds the record for the longest winning streak in a single Premier League season?",
            "options": ["Chelsea", "Liverpool", "Manchester City", "Arsenal"],
            "correct_option": 3
        },
        {
            "question": "Who was the first African player to win the Premier League Golden Boot?",
            "options": ["Didier Drogba", "Mohamed Salah", "Emmanuel Adebayor", "Yaya Touré"],
            "correct_option": 1
        },
        {
            "question": "Which Premier League club has the nickname 'The Toffees'?",
            "options": ["Newcastle United", "Everton", "West Ham United", "Aston Villa"],
            "correct_option": 2
        }
    ]

    score = 0

    print("Welcome to the Premier League Quiz!\n")

    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        for j, option in enumerate(question["options"], start=1):
            print(f"{j}. {option}")
        
        # Get the user's answer
        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if 1 <= answer <= len(question["options"]):
                    break
                else:
                    print("Invalid input! Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
        
        if answer == question["correct_option"]:
            print("Correct!\n")
            score += 1
        else:
            correct_answer = question["options"][question["correct_option"] - 1]
            print(f"Incorrect! The correct answer was: {correct_answer}\n")

    # Display final score
    print(f"Quiz completed! You got {score}/{len(questions)} questions correct.")

# Run the quiz
if __name__ == "__main__":
    main()
