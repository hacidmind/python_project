# # Introduction
# print('Welcome To The Quiz Game')

# # Input asking if you want to play the game
# play = input('Do you want to play the game? ')


# # conditional statement about the players answer
# if play.lower() != 'yes': #we need to convert our answer to lower case irrespective of what you type
#     quit() #exits the code block

# print("Okay! Let's begin")

# print('1')
# answer = input('What is the name of this bootcamp? ').lower()
# if answer == 'techstudio academy':
#     print("Correct")
# else:
#     print("Incorrect")

# print('2')

# answer = input('What course are you offering? ').lower()
# if answer == 'fullstack web development':
#     print("Correct")
# else:
#     print("Incorrect")

# print('3')

# answer = input('Who created World Wide Web? ').lower()
# if answer == 'tim berners-lee':
#     print("Correct")
# else:
#     print("Incorrect")
# print('1')

# answer = input('Who created python? ').lower()
# if answer == 'guido van rossum':
#     print("Correct")
# else:
#     print("Incorrect")
# print('1')

# answer = input('Who created Javascript? ').lower()
# if answer == 'brenden eich':
#     print("Correct")
# else:
#     print("Incorrect")

# Now to add our score
print('Welcome To The Quiz Game')

# Input asking if you want to play the game
play = input('Do you want to play the game? ')


# conditional statement about the players answer
if play.lower() != 'yes': #we need to convert our answer to lower case irrespective of what you type
    quit() #exits the code block

print("Okay! Let's begin")

score =0

print('1')
answer = input('What is the name of this bootcamp? ').lower()
if answer == 'techstudio academy':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print('2')
answer = input('What course are you offering? ').lower()
if answer == 'fullstack web development':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print('3')
answer = input('Who created World Wide Web? ').lower()
if answer == 'tim berners-lee':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print('4')
answer = input('Who created python? ').lower()
if answer == 'guido van rossum':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print('5')
answer = input('Who created Javascript? ').lower()
if answer == 'brenden eich':
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f'You got {str(score)} questions correctly ')
print(f'You got {str((score / 5) * 100)}% ')

