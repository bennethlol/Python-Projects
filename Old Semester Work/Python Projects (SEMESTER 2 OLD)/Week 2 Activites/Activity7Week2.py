from random import randint

count = 0
while count != 9:
    count = randint(1,10)
    print(count)
    if count == 9:
        print('Count has reached 9.')
        break