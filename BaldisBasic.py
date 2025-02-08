# *************************************************************************
# Program: BaldisBasic.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC2L / TL4L
# Trimester: 2430
# Names: CHIAM JUIN HOONG | CHONG SENG KIAT | NG JUN WEI
# IDs: 242FC242N8 | 242FC2425Y | 241FC24071 
# Emails: CHIAM.JUIN.HOONG@student.mmu.edu.my | CHONG.SENG.KIAT@student.mmu.edu.my | NG.JUN.WEI@student.mmu.edu.my
# *************************************************************************

import json
import os
import time
import sys

current_time = time.ctime()
PLAYER_DATA_FILE = "players.json"

# Game Variables
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
           ("A. 25", "B. 50", "C. 75", "D. 65"))

answers = ("C", "C", "A", "D", "B", "A", "C", "D", "D", "B", "A", "C", "A")

current_player = ""
score = 0
lives = 3
question_no = 0
jumpscares = 0  

def save_game():
    try:
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, "r") as f:
                players = json.load(f)
        else:
            players = {}

        
        if current_player in players:
            if score > players[current_player]:
                players[current_player] = score
        else:
            players[current_player] = score

        with open(PLAYER_DATA_FILE, "w") as f:
            json.dump(players, f)
    except Exception as e:
        print(f"Error saving game: {e}")

def jumpscaretoggle():
    global jumpscares
    jumpscares = 0 if jumpscares else 1
    status = "on" if jumpscares else "off"
    print(f"Jumpscares are now {status}.")

def load_leaderboard():
    try:
        # Check if file exists AND has content
        if os.path.exists(PLAYER_DATA_FILE) and os.path.getsize(PLAYER_DATA_FILE) > 0:
            with open(PLAYER_DATA_FILE, "r") as f:
                players = json.load(f)
            
            print("\n=== LEADERBOARD ===")
            # Sort players by score descending
            sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
            
            for player, high_score in sorted_players:
                print(f"{player}: {high_score}")
        else:
            print("No saved scores yet!")
    except json.JSONDecodeError:
        print("Corrupted save file detected. Resetting leaderboard.")
        os.remove(PLAYER_DATA_FILE)  # Remove corrupted file
    except Exception as e:
        print(f"Error loading leaderboard: {e}")


def easter_egg():
    print("Congratulations on finding the easter egg!")
    print("   *****   \n"
      "  -------  \n"
      " ********* \n"
      "-----------\n"
      " ********* \n"
      "  -------  \n"
      "   *****   \n")

def settings():
    print("\n| Options |")
    while True:
        print(">>> Toggle Jumpscares (1) <<<")
        print(">>> Return to Main Menu (2) <<<")
        option = input("Enter your choice: ").strip()
        if option == "1":
            jumpscaretoggle()
        elif option == "2":
            main_menu()
            break
        else:
            print("Invalid choice. Please try again.")

def story():
    print("\nOne day as you were walking home from school, you came across a mysterious building.")
    input("Press Enter to continue...")
    print("\nYou decided to enter the building and found yourself in a classroom.")
    input("Press Enter to continue...")
    print("\nSuddenly, the lights went out and you get knocked out.")
    input("Press Enter to continue...")
    print("\nYou wake up, confused, with a single computer in front of you.")
    input("Press Enter to continue...")
    print("\nThe door knocks...")
    input("Press Enter to continue...")
    print("\nBaldi: Oh! You're finally awake! I've been waiting for you.")
    input("Press Enter to continue...")
    print("\nBaldi: You're going to answer my questions. If you get them right, you're free to go.")
    input("Press Enter to continue...")
    print("\nBaldi: But if you get them wrong...")
    input("Press Enter to continue...")
    print("\nBaldi: Anyways, Good Luck!")
    input("Press Enter to continue...")
    gameplay()

def credit():
    print("This game is brought to you by Chiam Juin Hoong, Chong Seng Kiat and Ng Jun Wei.")
    print("TC2L / TL4L - 5")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def gameplay():
    global score, lives, question_no
    score = 0
    lives = 3
    question_no = 0

    while question_no < len(questions) and lives > 0:
        print(f"\n\n\nLives: {lives} | Score: {score}")
        print(f"Question {question_no+1}: {questions[question_no]}")
        for option in options[question_no]:
            print(option)

        while True:
            guess = input("Your answer (A/B/C/D): ").upper()
            if guess in ("A", "B", "C", "D"):
                break
            print("Invalid input! Please enter A, B, C, or D.")

        if guess == answers[question_no]:
            print("Correct!")
            score += 1
        else:
            if jumpscares:
                print("WRONG!!!\n███████▀▀▀░░░░░░░▀▀▀███████\n██████▀░░░░░░░░░░░░░░░▀████\n█████│░░░░░░░░░░░░░░░░│████\n████└┐░░░░░░░░░░░░░░░┌┘░███\n███░░└┐░░░░░░░░░░░░░░┌┘░░██\n███░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██\n██▌░▄██████▄░░░▄██████▄░▐██\n███─┘░░▓▓▓▓░░░░░▓▓▓▓░░└─███\n██▀▓▓▓░▓▓▓▓░░░░░▓▓▓▓░▓▓░▀██\n██▄▓▓▓░▓▓▓▓▄▄▄▄▄▓▓▓▓░▓▓▄███\n████▄─┘█████████████└─▄████\n█████░░▐███████████▌░░█████\n██████░░▀█████████▀░░▐█████\n███████░░░░▓▓▓▓▓░░░░▄██████\n████████▄░░░░░░░░░▄████████\n███████████▓▓▓▓▓███████████\n███████████▓▓▓▓▓███████████")
            else:
                print("Wrong!")
            lives -= 1

        question_no += 1

    # Game over handling
    if lives <= 0:
        print("\nGAME OVER! You ran out of lives!")
    else:
        print("\nCONGRATULATIONS! You answered all questions!")

    print(f"Final Score: {score}")
    save_game()
    main_menu()

def main_menu():
    global current_player
    while True:
        print("\n| Welcome to the Baldi's Basic Clone Game! |")
        print(">>> Play Game (1) <<<")
        print(">>> Exit (2) <<<")
        print(">>> Options (3) <<<")
        print(">>> Credit (4) <<<")
        print(">>> Time Now:",current_time,"<<<")

        choice = input("Choose option: ").strip()
        if choice == "1":
            
            while True:
                current_player = input("Enter your name: ").strip()
                if current_player:
                    break
                print("Name cannot be empty!")
            story()
        elif choice == "2":
            load_leaderboard()
            #print_slow("Thank you for playing the game!")
            #exit()
        elif choice == "3":
            settings()
        elif choice == "4":
            credit()
        elif choice == "8":
            easter_egg()
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main_menu()
