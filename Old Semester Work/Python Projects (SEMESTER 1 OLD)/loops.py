#Loops Practice
#Find largest and smallest value in a list of given numbers
largest = None
smallest = None

while True:
    num = input('Please input a number: ')
    if num == 'done':
        break
    elif not num.isnumeric():
        print('Invalid input')
        continue
    num = int(num)
    if largest == None or num>largest:
        largest = num
    if smallest == None or num<smallest:
        smallest = num

print(f'The largest value is: {largest} ')
print(f'The smallest value is: {smallest} ')

#Lists individual letters of name inputted
name = input("Enter Your Name: ")
print("Ok I will display the individual letters of your name as follows: ")
for char in name:
    print(char.upper())
print("The End :)")

#Find largest value in a list
list = [3, 41, 12, 9, 74, 16]
large = -1
for x in list:
    if x > large:
        large = x
print(f'The largest value in the list is: {large}')