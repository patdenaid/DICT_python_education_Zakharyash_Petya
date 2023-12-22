import random


def take_sticks(sticks, player):
    if player == "John":
        turn = int(input(f"{player}, it's your turn: "))
    else:
        turn = random.choice([1, 2, 3])
        print(f"{player}'s turn: {turn}")

    while not (1 <= turn <= 3 and turn <= len(sticks)):
        print("Error: Invalid input. Please enter a valid number.(1-3)")
        turn = int(input(f"{player}, it's your turn: ")) if player == "John" else random.choice([1, 2, 3])

    return sticks[:-turn]


def main():
    number = int(input("How many pencils would you like to use: "))
    sticks = "|" * number

    player1 = "John"
    player2 = "Bot"
    current_player = random.choice([player1, player2])

    print(f"{current_player}'s turn!")

    while sticks:
        print(sticks)
        sticks = take_sticks(sticks, current_player)
        current_player = player1 if current_player == player2 else player2

    print(f"{current_player} won!")


if __name__ == "__main__":
    main()
