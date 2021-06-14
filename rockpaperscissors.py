# import random

# while True:
#     my_answer = input('Choose: rock, paper or scissor ')
#     my_answer = my_answer.lower()
#     if my_answer != 'rock' and my_answer != 'paper' and my_answer != 'scissor':
#         print('Please choose a correct answer ')
#         continue

#     computer_answer = random.choice(['rock', 'paper', 'scissor'])
#     print(f'Computer chose: {computer_answer}')

#     if my_answer == computer_answer:
#         print('You tied')
#         continue
#     elif my_answer == 'paper' and computer_answer == 'rock':
#         print('You win!')
#         break
#     elif my_answer == 'rock' and computer_answer == 'scissor':
#         print('You win!')
#         break
#     elif my_answer == 'scissor' and computer_answer == 'paper':
#         print('You win!')
#         break
#     else:
#         print('You lose. Try again')



import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Choose: rock, paper or scissor or Q to quit: ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock:0 paper:1 scissors:2
    computer_pick = options[random_number]
    print(f'Computer picked {computer_pick}. ')

    if user_input == 'rock' and computer_pick == 'scissors':
        print('You win!')
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print('You win!')
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print('You win!')
        user_wins += 1
    else:
        print('You Lost')
        computer_wins += 1

print(f'You won {user_wins} ')
print(f'Computer won {computer_wins} ')
print('Congratulations!')
