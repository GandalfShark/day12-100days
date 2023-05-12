# day 12 number guessing game

from random import randint
secret_number = randint(1, 100)
# use the randint function to generate a random integer between 1 and 100

# print(secret_number)

game_over = False

title = """
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  GUESS THE NUMBER !
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
instructions:
game uses whole numbers only
easy mode 10 chances
hard mode 5 chances
chose your mode and enter your guesses
when you run out of chances the game will exit
"""

# functions #


def out_of_time(chances_left):
    print('*')
    if chances_left == 0:
        return True
    else:
        return False


def mode_selection():
    choice = (input('easy or hard?')).lower()
    mode = {'easy': 10, 'hard': 5}
    try:
        return mode[choice]
    except KeyError:
        print(f'ERROR: "{choice}" is not valid input\nMode set to easy.\n')
        return 10


# # main section with gameplay # #

print(title)
chances = mode_selection()
# call the function to return either 5 or 10

while not game_over:
    user_guess = int(input('Make a guess: '))
    if user_guess < secret_number:
        print('TOO LOW.')
        chances -= 1
        print(f'You have {chances} chances left.')
        game_over = out_of_time(chances)
    elif user_guess > secret_number:
        print('TOO HIGH!')
        chances -= 1
        print(f'You have {chances} chances left.')
        game_over = out_of_time(chances)
    else:
        print(f'Bingo Bango!\n You guessed {user_guess} and the number is {secret_number}!')
        game_over = True

print(f"""
^^^^^^^^^^^^^^^^^^^
Thanks for playing.
the secret number was: {secret_number}
^^^^^^^^^^^^^^^^^^^
""")