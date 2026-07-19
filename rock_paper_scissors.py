import random

while True:
    user = input("Enter your move (Rock, Paper, Scissors) or type 'end' to stop: ")

    if user.lower() == "end":
        print("Game over. Thanks for playing!")
        break

    computer = random.choice(["Rock", "Paper", "Scissors"])

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif user == "Rock" and computer == "Scissors":
        print("You win! Rock smashes Scissors.")

    elif user == "Paper" and computer == "Rock":
        print("You win! Paper covers Rock.")

    elif user == "Scissors" and computer == "Paper":
        print("You win! Scissors cut Paper.")

    elif user == "Rock" and computer == "Paper":
        print("Computer wins! Paper covers Rock.")

    elif user == "Paper" and computer == "Scissors":
        print("Computer wins! Scissors cut Paper.")

    elif user == "Scissors" and computer == "Rock":
        print("Computer wins! Rock smashes Scissors.")

    else:
        print("Invalid input! Please type Rock, Paper, or Scissors.")
