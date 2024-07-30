import random

def user_choice():
    choice = ["gun","water","snake"]
    user_choice_input =input("Enter your choice gun or water or snake: ").lower()
    while (user_choice_input not in choice):
        print("Invalid input. Please chose gun, water , snake")
        user_choice_input =input("Enter your choice gun or water or snake: ").lower()
    return(user_choice_input)

def computer_choice():
    choice = ["gun","water","snake"]
    return random.choice(choice)

def winner(user_choice, computer_choice):
    if (user_choice == computer_choice):
        return "Draw match!"
    
    elif ((user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake") or \
         (user_choice == "snake" and computer_choice == "water")):
        return "You win!"
    
    else:
        return "computer win!"

def play_game():
    print("****** Welcome to the Water-Gun_Snake game ******")
    while True:
        user_choice_vairiable = user_choice()
        computer_choice_variable = computer_choice()
        print(f"You chose: {user_choice_vairiable}\n Computer chose: {computer_choice_variable}")
        result = winner(user_choice_vairiable, computer_choice_variable)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()

