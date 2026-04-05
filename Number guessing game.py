import random

number = random.randint(1,100)
print("Computer selected number: ", number)
attempts = 0

print("Guess the Number(1 to 100)")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("Enter number between 1 and 100")
        elif guess > number:
            print("Guess number is Too High!")
        elif guess < number:
            print("Guess number is Too Low!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number!")