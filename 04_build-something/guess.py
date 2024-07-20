# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

import random

num = random.randint(0,10)
guess = None

while guess!=num:
    guess = input('Guess a number between 0 and 10 :')
    guess = int(guess)
    if guess==num:
        print('Congratulations, you won!')
        break
    else:
        print('Nope, try again')
    
