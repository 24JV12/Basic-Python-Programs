from random import randint
import time, os

def clear(): os.system('cls' if os.name == 'nt' else 'clear')
clear()
while True:
    initial = randint(-100, 100)
    number = randint(initial, randint(initial, 100))
    while True:
        total_guesses = int(input(r".\totalGuesses> "))
        if total_guesses == 0: print("Don't be ridiculous")
        else: break
    print(f"Final Answer: {number}\n")

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
    else: print("Lost!")
    while True:
        againQ = input("Again? (Y/n) ").lower()
        if "y" in againQ:
            clear()
            break
        elif "n" in againQ: exit()
