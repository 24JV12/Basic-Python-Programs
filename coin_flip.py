from random import choice
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_one():
    jar = []
    interval = 1
    while True:
        cmd = input(f"Choice {interval}: ")
        command = cmd.lower()
        if command == "done":
            break
        elif command == "clear" or command == "cls":
            clear()
        elif command == "exit":
            exit()
        else: 
            jar.append(cmd)
            interval += 1
            continue

    if jar:
        print(f"Random Pick is '{choice(jar)}'")
    else:
        print("No choices were entered.")

clear()

while True:
    pick_one()
