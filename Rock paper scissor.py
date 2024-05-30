import random

options = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper, or Scissors: ")
computer_choice = random.choice(options)
a=user_choice.capitalize()
print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)

if a == computer_choice:
    print("It's a tie!")
elif a == "Rock" and computer_choice == "Scissors":
    print("You win!")
elif a == "Paper" and computer_choice == "Rock":
    print("You win!")
elif a == "Scissors" and computer_choice == "Paper":
    print("You win!")
else:
    print("Computer wins!")
