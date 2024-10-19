from random import randint
import time

initial = randint(-100, 100)
number = randint(initial, randint(initial, 100))
total_guesses = int(input(r".\totalGuesses> "))
print(f"Final Answer: {number}\n\nTotal Guesses: {total_guesses}\n")

low, high = -100, 100

for guesses in range(1, total_guesses + 1):
    guess = randint(low, high)
    print(f"Guess {guesses}: {guess}")
    
    if guess == number:
        print("Won!")
        break
    elif guess > number:
        print("less than that\n")
        high = guess - 1
    else:
        print("more than that\n")
        low = guess + 1
    
    time.sleep(1)
else:
    print("Lost!")
