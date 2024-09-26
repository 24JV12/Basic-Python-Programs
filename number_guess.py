from random import choice

guesses = 1

possible_numbers = []

inital = int(input("Initial: "))
final = int(input("Final: "))

for possible_number in range(inital, final+1):
    possible_numbers.append(possible_number)
number = choice(possible_numbers)


while True:
    total_guesses = int(input("How many chances? [1, 25] "))
    if total_guesses >= 25 or total_guesses <= 1:
        print("Error Detected!")
        continue
    else:
        break

while True:
    cmd = int(input(f"Guess {guesses}: "))
    if guesses != total_guesses:
        if cmd == 0:
            confirm = input("Reveal Answer? [Y/n] ").lower()
            if confirm == "y" or confirm == "yes":
                print(f"Number: {number}")
            elif confirm == "n" or confirm == "no":
                continue
        elif cmd != number:
            if cmd > number:
                print("Try something less than that")
            else:
                print("Try with something more than that")
            guesses+=1
            continue
        elif cmd == number:
            print("You Won!")
            break
        else:
            print("Error Detected!")
            continue
    else:
        print("You Lost!")
        break