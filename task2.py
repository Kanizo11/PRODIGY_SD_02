import random

def guessing_game():
    random_num = random.randint(1, 100)
    attempts = 0
    
    while True:
        user_guess = int(input("Guess the number: "))
        attempts += 1
        if user_guess < random_num:
            print("Your guess is too low, try again.")
        elif user_guess > random_num:
            print("Your guess is too high, try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break


guessing_game()
