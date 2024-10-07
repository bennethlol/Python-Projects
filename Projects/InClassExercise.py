from random import randint
# Exercise 1: Basic Calculator
inputOne = float(input('Please enter the first number: '))
inputTwo = float(input('Please enter the second number: '))
answer = float(0)

operation = input('Which operation are you using: ')

if operation == 'addition':
    answer = inputOne + inputTwo
elif operation == 'subtraction':
    answer = inputOne - inputTwo
elif operation == 'multiplication':
    answer = inputOne * inputTwo
elif operation == 'division':
    answer = inputOne / inputTwo

print(f'The answer of your equation is: {answer}')

# Exercise 2: Number Guessing Game

RandomNumber = randint(0, 100)
while True:
    Guess = int(input('Guess the random number: '))
    if Guess > RandomNumber:
        print('Too high! Guess again.')
    elif Guess < RandomNumber:
        print('Too low! Guess again.')
    elif Guess == RandomNumber:
        print('Congradulations! You guessed it right!')
        break

# Exercise 3: Even or Odd checker

def check_even_odd(start, end):
    for x in range(start, end+1):
        if x % 2 == 0:
            print(f'{x} is even.')
        else:
            print(f'{x} is odd.')

# Exercise 4: Pattern Printing

def print_triangle(rows):
    for row in range(1, rows+1):
        for i in range(row):
            print('*', end='')
        print()

print_triangle(int(input('How many rows for the triangle: ')))