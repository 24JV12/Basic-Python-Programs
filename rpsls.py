import random, os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

arsenal, commands = ("rock", "paper", "scissors", "lizard", "spock"), ('clear', 'exit')

def handleCommands(player1, player2):
    if player1 in commands or player2 in commands:
        if player1 == "exit" or player2 == "exit":
            exit()
        elif player1 == "clear" or player2 == "clear":
            clear()

def main(player1, player2, isAlone):
    result = None
    handleCommands(player1, player2)

    if player1 in arsenal and player2 in arsenal:
        input("Press enter to reveal the answer...")
        if player1 == player2:
            result = "It's a Tie"
        elif (player1 == "rock" and (player2 == "scissors" or player2 == "lizard")) or \
                (player1 == "paper" and (player2 == "rock" or player2 == "spock")) or \
                (player1 == "scissors" and (player2 == "paper" or player2 == "lizard")) or \
                (player1 == "lizard" and (player2 == "paper" or player2 == "spock")) or \
                (player1 == "spock" and (player2 == "rock" or player2 == "scissors")):
            result = "You Win" if isAlone else "Player 1 Wins!"
        else:
            result = "You Lose" if isAlone else "Player 2 Wins!"
            
        if isAlone:
            print(f"I choose '{player2.title()}'. {result}")
        else:
            print(result)
    else:
        print("Error!")

clear()

while True:
    isAlone = input("Are you playing Alone? (Y/n) ").lower()
    if "y" in isAlone:
        while True:
            player = input(r".\Computer\RPSLS\Player> ").lower()
            computer = random.choice(arsenal)
            main(player, computer, True)
    elif "n" in isAlone:
        while True:
            player1 = input(r".\Humans\RPSLS\Player1> ").lower()
            clear()
            handleCommands(player1, None)
            player2 = input(r".\Humans\RPSLS\Player2> ").lower()
            clear()
            handleCommands(None, player2)
            main(player1, player2, False)
