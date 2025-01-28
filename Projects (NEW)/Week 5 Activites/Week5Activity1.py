# Write a program that prints the times tables of all numbers from 2 to 20
# Each number should be multiplied by all numbers between 2 to 20

for num in range(2,21):
    for multi in range(2,21):
        print(num,'x',multi,'=',(num*multi))