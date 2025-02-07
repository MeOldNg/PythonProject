import json
import os

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
           ("A. 75", "B. 50", "C. 75", "D. 65"))

answers = ("C", "C", "A", "D", "B", "A", "C", "D", "D", "B", "A", "C", "C")

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
        if os.path.exists(PLAYER_DATA_FILE):
            with open(PLAYER_DATA_FILE, "r") as f:
                players = json.load(f)
            print("\n=== LEADERBOARD ===")
            for player, high_score in sorted(players.items(), key=lambda x: x[1], reverse=True):
                print(f"{player}: {high_score}")
        else:
            print("No saved scores yet!")
    except Exception as e:
        print(f"Error loading leaderboard: {e}")

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

def gameplay():
    global score, lives, question_no
    score = 0
    lives = 3
    question_no = 0

    while question_no < len(questions) and lives > 0:
        print(f"\nLives: {lives} | Score: {score}")
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
                print("Wrong! JUMPSCARE!")
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
        print(">>> View Leaderboard (2) <<<")
        print(">>> Exit (3) <<<")
        print(">>> Options (4) <<<")

        choice = input("Choose option: ").strip()
        if choice == "1":
            
            while True:
                current_player = input("Enter your name: ").strip()
                if current_player:
                    break
                print("Name cannot be empty!")
            gameplay()
        elif choice == "2":
            load_leaderboard()
        elif choice == "3":
            print("Thanks for playing!")
            exit()
        elif choice == "4":
            settings()
        else:
            print("Invalid choice! Please enter 1-4.")

if __name__ == "_main_":
    main_menu()
