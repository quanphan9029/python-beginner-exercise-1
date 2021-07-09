# New game: Count to 30.
# Rules:
# 2 persons, rolling the dice to decide who go first
# Every turn of each person, you can count 1 number (min) to 3 numbers (max).
# Start with 1, countinue counting the next number from the last count.
# Who first gets 30 is the Winner.

import random


def menu():
    print(f"1. Player vs Computer.")
    print(f"2. Player vs Player.")
    print(f"0. Exit")


def pick_turn(game_type):
    if game_type == 1:
        print(f"You choose Player vs Computer.")
        turn = ['Player', 'Computer']
        turn_result = random.choice(turn)
    else:
        print(f"You choose Player vs Player.")
        turn = ['Player 1', 'Player 2']
        turn_result = random.choice(turn)
    print(f"{turn_result} go first.")


def pvp_count(i):
    turn_number = int(input(f"Enter your number: "))
    while turn_number != (i + 1):
        print(f"Invalid input. Please try again.")
        turn_number = int(input(f"Enter your number: "))
    return turn_number


# Main program

menu()
option = int(input(f"Please choose your game type: "))
pick_turn(option)

numbers_list = [0] * 30

for i in range(0, 30):
    turn_number = pvp_count(i)
    del numbers_list[0]
    numbers_list.append(turn_number)

# numbers_list.reverse() # No need to reverse

print(numbers_list)