import random

# Guessing game. Computer secret number. Player guess.
def player_guess(max_number):
    secret_number = random.randint(1,max_number)
    guess_number = int(input(f'Guess an integer number from 1 to {max_number}: '))

    def compare(secret_number, guess_number):
        while guess_number != secret_number:
            if guess_number < secret_number:
                guess_number = int(input('Sorry. Guess again. Too low: '))
            elif guess_number > secret_number:
                guess_number = int(input('Sorry. Guess again. Too high: '))
        print(f'Yays. Congrats. You have guessed secret number {secret_number} correctly.')

    compare(secret_number, guess_number)
#player_guess(10) #----> Play!


# Guessing game. Player secret number. Computer guess.
def computer_guess(max_number):
    min_num = 1
    max_num = max_number
    guess_number = random.randint(min_num, max_num)



    def player_answer(guess):
        print(f"Computer's guessing number is: {guess_number}.")
        print(f'Choose, ')
        print(f'(c) or (C) for "Correct answer."')
        print(f'(l) or (L) for "Too low.')
        print(f'(h) or (H) for "Too high".')
        answer = input('Please choose your answer: ')
        return answer

    choice = player_answer(guess_number)

    while choice != 'c' and choice != 'C':
        if choice == "h" or choice == "H":
            max_num = guess_number
            guess_number = random.randint(min_num, max_num)
            choice = player_answer(guess_number)
        elif choice == "l" or choice =="L":
            min_num = guess_number
            guess_number = random.randint(min_num, max_num)
            choice = player_answer(guess_number)

    print(f"Congratulations. Yon have guess the right number {guess_number}")

# ----> Play...
#    player_answer()

computer_guess(100)
