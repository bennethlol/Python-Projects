# Find largest number out of all inputs
largest = 0

for nums in range(1,11):
    num = input('Please input a number: ')
    if num == 'done':
        break
    elif not num.isnumeric():
        print('Invalid input')
        continue
    num = int(num)
    if largest == 0 or num>largest:
        largest = num

print(f'The largest value is: {largest} ')
