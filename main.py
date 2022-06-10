import random
while True:
    choices = ["R", "P", "S"]
    # R stands for rock
    # P stands for paper
    # S stands for scissors

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('R, P or S?:').upper()

    if player == computer:
        print('player:', player)
        print('computer:', computer)
        print("Tie!!")
    elif player == "R":
        if computer == "P":
            print('player:', player)
            print('computer:', computer)
            print("You lose!!")
        else:
            print('player:', player)
            print('computer:', computer)
            print("You win!!")
    elif player == "P":
        if computer == "R":
            print('player:', player)
            print('computer:', computer)
            print("You win!!")
        else:
            print('player:', player)
            print('computer:', computer)
            print("You lose!!")
    else:
        if computer == "R":
            print('player:', player)
            print('computer:', computer)
            print("You lose!!")
        else:
            print('player:', player)
            print('computer:', computer)
            print("You win!!")

    play_again = input("Would you like to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
