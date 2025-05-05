count = 0
while count != 10:
    inter = int(input('Enter an integer: '))
    count += 1
    if inter == 3:
        print('Skipping the rest of this iteration.')
        count = 0
    elif inter == 9:
        print('Skipping the rest of this iteration.')
        count = 0
    elif inter == 5:
        print('Exit condition reached.')
        break
print('Loop terminated')

