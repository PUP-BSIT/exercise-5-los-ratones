
# TODO(Kenji Enishi Campos): Create question 1.
def question_1():
    pass

def question_2():
    member = "Jedi Duncan S. Gonot"
    question = "In Valorant, who is the agent that uses knives as their ult?"
    choices = ["Brimstone", "Waylay", 
                "Kay-o", "Jett"]
    right_answer = False
    
    print(f"({member}) {question}")
    print(f"A. {choices[0]} B. {choices[1]}")
    print(f"C. {choices[2]}  D. {choices[3]}")
    answer = input("Enter your answer: ").capitalize()

    if answer == 'D':
        right_answer = True
        print("You are correct! Jett is the agent that uses knives as their ult!")
    else:
        print(f"{answer} is incorrect. The correct answer is D.")

    if right_answer == True:
        return 1
    else:
        return 0

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
print("-=-=-LOS RATONES QUIZ-=-=-")
for x in range(5):
    print(f"Question {x+1}:")
    match x:
        case 0:
            pass
        case 1:
            score += question_2()
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