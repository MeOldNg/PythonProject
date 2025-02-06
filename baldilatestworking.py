questions = ("What is 4 to the power of 2?",
             "What is the square root of 144?",
             "What is 68 plus 42",
             "What is 15 divided by 3?",
             "What is the result of 7 times 6?",
             "What is 100 minus 45?",
             "What is the cube root of 27?",
             "What is 81 divided by 9?",
             "What is 2 to the power of 5?",
             "What is the square root of 225?",
             "What is 11 to the power of 2?",
             "What is the square root of 169?",
             "What is 50 plus 25?")

options = (("A. 12", "B. 8", "C. 16", "D. 44"),
           ("A. 64", "B. 8", "C. 12", "D. 14"),
           ("A. 110", "B. 100", "C. 102", "D. 120"),
           ("A. 7", "B. 3", "C. 13", "D. 5"),
           ("A. 76", "B. 42", "C. 48", "D. 67"),
           ("A. 55", "B. 45", "C. 50", "D. 35"),
           ("A. 9", "B. 13", "C. 3", "D. 6"),
           ("A. 8", "B. 12", "C. 10", "D. 9"),
           ("A. 16", "B. 22", "C. 24", "D. 32"),
           ("A. 25", "B. 15", "C. 5", "D. 20"),
           ("A. 121", "B. 111", "C. 152", "D. 144"),
           ("A. 14", "B. 12", "C. 13", "D. 15"),
           ("A. 75", "B. 50", "C. 75", "D. 65"))

answers = ("C",
           "C",
           "A",
           "D",
           "B",
           "A",
           "C",
           "D",
           "D",
           "B",
           "A",
           "C",
           "C")

guesses = []
score = 0
question_no = 0
incorrect = 0
jumpscares = 0

def gameplay():
    global question_no
    global score
    global incorrect
    global jumpscares
    while True:
        if question_no < 13:
            if incorrect < 4:
                print("\n\n\nCurrent Score: " + str(score))
                print("Question " + str(question_no + 1) + ", " + questions[question_no])
                for i in options[question_no]:
                    print(i)
                guess = input("Enter your answer: ")
                if guess.upper() == answers[question_no]:
                    print("Correct!")
                    score += 1
                    question_no += 1
                    continue
                else:
                    incorrect += 1
                    question_no += 1
                    if jumpscares == 0:
                        print("Incorrect!")
                    elif jumpscares == 1:
                        if incorrect < 2:
                            print("Incorrect!")
                        elif incorrect > 1:
                            print("Jumpscare Incorrect")
                    continue
            else:
                print(" \n\n\n| GAME OVER!!! |")
                endscreen()
        else :
            print(" \n\n\n| CONGRATULATIONS!!! |")
            endscreen()

def leaderboard():
    print("Leaderboard")
    mainmenu()

def jumpscaretoggle():
    global jumpscares
    if jumpscares == 0:
        jumpscares += 1
    else:
        jumpscares -= 1

def settings():
    print("\n\n\n| Options |")
    while True:
        if jumpscares == 1:
            print("Jumpscares are currently on.\n"
                  ">>> Toggle Jumpscares (1) <<<\n"
                  ">>> Return to Main Menu (2) <<<")
        else:
            print("Jumpscares are currently off.\n"
                    ">>> Toggle Jumpscares (1) <<<\n"
                    ">>> Return to Main Menu (2) <<<")
        break
    option = input("Enter your choice: ")
    if option == "1":
        jumpscaretoggle()
        settings()
    elif option == "2": 
        mainmenu()
    else:
        print("Invalid choice")
        settings()

def mainmenu():
    print("\n\n\n| Welcome to the Baldi's Basic Clone Game! |")
    print(">>> Play Game (1) <<<\n"
          ">>> View Leaderboard (2) <<<\n"
          ">>> Options (3) <<<\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        gameplay()
    elif choice == "2":
        leaderboard()
    elif choice == "3":
        settings()
    else:
        print("Invalid choice")
        mainmenu()

def endscreen():
    global question_no
    global score
    global incorrect
    global jumpscares
    print("Your score is: " + str(score))
    print(">>> Play Again (1) <<<\n"
          ">>> Return to Main Menu (2) <<<\n"
          ">>> Quit (3) <<<")
    returnchoice = input("Enter your choice: ")
    if returnchoice == "1":
        score = 0
        question_no = 0
        incorrect = 0
        jumpscares = 0
        gameplay()
    elif returnchoice == "2":
        mainmenu()
    elif returnchoice == "3":
        exit()
    else:
        print("Invalid choice")
        mainmenu()

mainmenu()