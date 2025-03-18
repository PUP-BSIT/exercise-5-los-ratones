
def question_1():
    member = "Kenji Enishi Campos"
    question = "In Honkai Star Rail, which one of the following is NOT an Emanator?"
    choices = ["Madam Herta", "Acheron", "Welt Yang", "Phantylia"]
    right_answer = False

    print(f"({member}) {question}")
    print(f"A. {choices[0]}   B. {choices[1]}") 
    print(f"C. {choices[2]}     D. {choices[3]}")
    answer = input("Enter your answer: ").capitalize()

    if answer == "C":
        right_answer = True
        print("You are correct! Welt Yang is not an Emanator (but he's as strong as them)!\n")
    else:
        print(f"{answer} is incorrect. The correct answer is C.\n")

    if right_answer == True:
        return 1
    else:
        return 0

# TODO(Jedi Duncan Gonot): Create question 2.
def question_2():
    pass

# TODO(Dion Manicio): Create question 3.
def question_3():
    pass

# TODO(Paul Benidict Reduta): Create question 4.
def question_4():
    pass

# TODO(JohnPaul Rodriguez): Create question 5.
def question_5():
    pass

score = 0
print("-=-=-LOS RATONES QUIZ-=-=-\n")
for x in range(5):
    print(f"Question {x+1}:")
    match x:
        case 0:
            score += question_1()
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

if score > 1:
    print(f"Congratulations! You scored {score} out of 5!")
else:
    print("You scored 0 out of 5. Better luck next time!")