from random import randint

num1 = randint(1,10)
num2 = randint(1,10)

ans = int(input(f'What is {num1} + {num2} ? '))
if ans == num1 + num2:
    print('Correct!')
else:
    print('Incorrect, please try again.')

div = int(input('Input a number: '))
if div % 3 == 0:
    print(f'{div} is divisible by 3')
elif div % 2 == 0:
    print(f'{div} is divisible by 2')
else:
    print(f'{div} is not divisible by 2 or 3')

numprint = input('Please input a number: ')
if numprint == '1':
    print('ONE')
elif numprint == '2':
    print('TWO')
elif numprint == '3':
    print('THREE')
elif numprint == '4':
    print('FOUR')
elif numprint == '5':
    print('FIVE')
elif numprint == '6':
    print('SIX')
elif numprint == '7':
    print('SEVEN')
elif numprint == '8':
    print('EIGHT')
elif numprint == '9':
    print('NINE')
else:
    print('OTHER')

examscore = int(input('Input your exam score: '))
if examscore <= 100 and examscore >= 0:
    print('Exam score is', examscore, 'out of 100.')
else:
    print('Invalid entry. Please try again.')
