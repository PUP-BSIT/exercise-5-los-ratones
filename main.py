
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

def question_2():
    member = "Jedi Duncan S. Gonot"
    question = "In Valorant, who is the agent that uses knives as their ult?"
    choices = ["Brimstone", "Waylay", "Kay-o", "Jett"]
    right_answer = False
    
    print(f"({member}) {question}")
    print(f"A. {choices[0]}     B. {choices[1]}")
    print(f"C. {choices[2]}         D. {choices[3]}")
    answer = input("Enter your answer: ").capitalize()

    if answer == 'D':
        right_answer = True
        print("You are correct! Jett is the agent that uses knives as their ult!\n")
    else:
        print(f"{answer} is incorrect. The correct answer is D.\n")

    if right_answer == True:
        return 1
    else:
        return 0

def question_3():
    member = "Dion Kylo C. Manicio"
    question = "In Minecraft, what is the name of the blocky enemy that explodes?"
    choices = ["Skeleton", "Enderman", "Creeper ", "Zombie"]
    right_answer = False
    
    print(f"({member}) {question}")
    print(f"A. {choices[0]}      B. {choices[1]}")
    print(f"C. {choices[2]}      D. {choices[3]}")
    answer = input("Enter your answer: ").capitalize()

    if answer == 'C':
        right_answer = True
        print("You are correct! The Creeper is the blocky enemy that explodes!\n")
    else:
        print(f"{answer} is incorrect. The correct answer is C.\n")

    if right_answer == True:
        return 1
    else:
        return 0
    
def question_4():
    member = "Paul Benidict L. Reduta"
    question = "In the game 'League of Legends', which item grants bonus health scaling with stacks."
    choices = ["Sunfire Aegis", "Seraph's Embrace", 
               "Heartsteel", "Overlord's Bloodmail"]
    right_answer = False 

    print(f"({member}) {question}")
    print(f"A. {choices[0]} B. {choices[1]}")
    print(f"C. {choices[2]}    D. {choices[3]}")
    answer = input("Enter your answer: ").capitalize()

    if answer == 'C':
        right_answer = True
        print("You are correct! Heartsteel grants a stack that gives bonus health!\n")
    else:
        print(f"{answer} is incorrect. The correct answer is C.\n")

    if right_answer == True:
        return 1
    else:
        return 0

def question_5():
    member = "John Paul Rodriguez"
    question = "Which video game features a battle royale mode called 'Warzone'?"
    choices = ["Fortnite", "Call of Duty", "PUBG", "Apex Legends"]
    right_answer = False

    print(f"({member}) {question}")
    print(f"A. {choices[0]}      B. {choices[1]}")
    print(f"C. {choices[2]}          D. {choices[3]}")
    
    answer = input("Enter your answer: ").capitalize()

    if answer == 'B':
        right_answer = True
        print("You are correct! Call of Duty features the Warzone battle royale mode!\n")
    else:
        print(f"{answer} is incorrect. The correct answer is B.\n")

    if right_answer == True:
        return 1
    else:
        return 0

score = 0
print("-=-=-LOS RATONES QUIZ-=-=-\n")
for x in range(5):
    print(f"Question {x+1}:")
    match x:
        case 0:
            score += question_1()
        case 1:
            score += question_2()
        case 2:
            score += question_3()
        case 3:
            score += question_4()
        case 4:
            score += question_5()

if score >= 1:
    print(f"Congratulations! You scored {score} out of 5!")
else:
    print("You scored 0 out of 5. Better luck next time!")