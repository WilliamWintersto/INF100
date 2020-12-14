import random

round_nr = 1
score_me = 0
score_you = 0
move_list = ['Rock', 'Paper', 'Scissors']

# Calculating winner
def rock_paper_scissors(you, me):
    
    if you == me:
        return "It's a draw"
    
    elif you == 'Rock':        
        
        if me == 'Paper':
            return 'You Lose'
        else:
            return 'You Win'
    
    elif you == 'Paper':

        if me == 'Scissors':
            return 'You Lose'
        else:
            return 'You Win'
    
    else:
        if me == 'Rock':
            return 'You Lose'
        else:
            return 'You Win'

# Startup text
print('Welcome to Rock-Paper-Scissors!')
print('Press "q" at any time to quit')

# Game loop
while True:
    
    print(f"Let's play round {round_nr}")

# Taking input and checking if it's valid
    while True:

        you_answer = input('Your choice (Rock/Paper/Scissors)? ')

        if you_answer == 'Rock' or you_answer == 'Paper' or you_answer == 'Scissors':
            break
        elif you_answer == 'q':
            break
        else:
            print('***INVALID INPUT***')
            continue

# If you want to quit at this stage
    if you_answer == 'q':
        print('-----Program closed-----')
        break

# Computer choice    
    me_answer = random.choice(move_list)

# Calculation result and updating scores
    result = rock_paper_scissors(you_answer, me_answer)

    if result == 'You Win':
        score_you += 1
    elif result == 'You Lose':
        score_me += 1

# Displaying result and current score
    print(f'My choice was {me_answer}. {result}.')
    print(f'Score: me {score_me}, you {score_you}')

# Quit the game?
    while True:
        
        continue_playing = input('Continue (y/n)? ')

        if continue_playing == 'n' or continue_playing == 'q':
            break
        elif continue_playing == 'y':
            round_nr += 1
            break
        else:
            print('***INVALID INPUT***')
            continue
    
    if continue_playing == 'n' or continue_playing == 'q':
        print('-----Program closed-----')
        break
