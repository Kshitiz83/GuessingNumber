import random

comp_num = random.randint(1, 100)

turns = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        num = int(input("Enter your guess: "))
        turns += 1
        
        if num == comp_num:
            print(f"Congratulations! You guessed the number {comp_num} in {turns} attempts.")
            break
        elif num < comp_num:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
    except ValueError:
        print("Please enter a valid number.")

