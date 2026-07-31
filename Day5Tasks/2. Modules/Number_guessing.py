import random
import math

secret_number = random.randint(1, 50)
attempts = 5

print("Guess the number between 1 and 50!")
print(f"You have {attempts} attempts.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"\nAttempt {attempt}/{attempts} - Enter your guess: "))

    if guess == secret_number:
        print(f"Congratulations! You guessed it right — the number was {secret_number}!")
        break
    else:
        difference = math.fabs(guess - secret_number)
        print(f"Wrong guess! You are {difference} away from the correct number.")

        if attempt == attempts:
            print(f"\nGame over! You've used all your attempts. The correct number was {secret_number}.")
            