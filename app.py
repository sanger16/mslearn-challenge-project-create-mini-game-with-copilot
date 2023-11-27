#rock, paper, scissors game
# import random module
import random
# import time module
import time
# output welcome message
print('Welcome to Rock, Paper, Scissors!')
# add delay
time.sleep(1)
# input player option prompt again if invalid
player = input('Choose (r)ock, (p)aper, or (s)cissors: ')
# make player input in lower case
player = player.lower()
# add delay
time.sleep(1)
while player not in ['r', 'p', 's']:
    player = input('Invalid choice. Choose (r)ock, (p)aper, or (s)cissors: ')
# add delay
time.sleep(1)
# output player option
print(player, 'vs', end=' ')
# add delay
time.sleep(1)
# input computer option
chosen = random.randint(1,3)
# output computer option
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
else:
    computer = 's'
print(computer)
# add delay
time.sleep(1)
# Save scores to variables and keep playing until player chooses to stop
player_score = 0
computer_score = 0
while True:
    # add delay
    time.sleep(1)
    # determine winner, or tie
    if player == computer:
        print('Tie!')
    elif player == 'r' and computer == 's':
        print('You win!')
        player_score += 1
    elif player == 'r' and computer == 'p':
        print('You lose!')
        computer_score += 1
    elif player == 'p' and computer == 'r':
        print('You win!')
        player_score += 1
    elif player == 'p' and computer == 's':
        print('You lose!')
        computer_score += 1
    elif player == 's' and computer == 'p':
        print('You win!')
        player_score += 1
    elif player == 's' and computer == 'r':
        print('You lose!')
        computer_score += 1
    # add delay
    time.sleep(1)
    # output scores
    print('You: ' + str(player_score))
    print('Computer: ' + str(computer_score))
    # add delay
    time.sleep(1)
    # ask to play again
    play_again = input('Play again? (y)es or (n)o: ')
    # if yes, prompt player for choice
    if play_again == 'y':
        player = input('Choose (r)ock, (p)aper, or (s)cissors: ')
        while player not in ['r', 'p', 's']:
            player = input('Invalid choice. Choose (r)ock, (p)aper, or (s)cissors: ')
        # add delay
        time.sleep(1)
        # output player choice
        print(player, 'vs', end=' ')
        # add delay
        time.sleep(1)
        # input computer choice
        chosen = random.randint(1,3)
        # output computer choice
        if chosen == 1:
            computer = 'r'
        elif chosen == 2:
            computer = 'p'
        else:
            computer = 's'
        print(computer)
    # if no, break
    else:
        break
# add delay
time.sleep(1)
# output final scores
print('Final scores:')
print('You: ' + str(player_score))
print('Computer: ' + str(computer_score))
# add delay
time.sleep(1)
# determine winner
if player_score > computer_score:
    print('You win!')
elif player_score < computer_score:
    print('You lose!')
else:
    print('Tie!')
# add delay
time.sleep(1)
# output goodbye message
print('Thanks for playing!')
