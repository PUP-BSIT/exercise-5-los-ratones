
# TODO(Kenji Enishi Campos): Create question 1.
def question_1():
    pass

# TODO(Jedi Duncan Gonot): Create question 2.
def question_2():
    pass

# TODO(Dion Manicio): Create question 3.
def question_3():
    pass

# TODO(Paul Benidict Reduta): Create question 4.
def question_4():
    pass


def question_5():
    member = "John Paul Rodriguez"
    question = "Which video game features a battle royale mode called 'Warzone'?"
    choices = ["Fortnite", "Call of Duty", "PUBG", "Apex Legends"]
    right_answer = False

    print(f"({member}) {question}")
    print(f"A. {choices[0]} B. {choices[1]}")
    print(f"C. {choices[2]} D. {choices[3]}")
    
    answer = input("Enter your answer: ").capitalize()

    if answer == 'B':
        right_answer = True
        print("You are correct! Call of Duty features the Warzone battle royale mode!\n")
    else:
        print(f"{answer} is incorrect. The correct answer is B.\n")

    if right_answer:
        return 1
    else:
        return 0

score = 0
print("-=-=-LOS RATONES QUIZ-=-=-")
for x in range(5):
    print(f"Question {x+1}:")
    match x:
        case 0:
            pass
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            score += question_5()

if score > 1:
    print(f"Congratulations! You scored {score} out of 5!")
else:
    print("You scored 0 out of 5. Better luck next time!")