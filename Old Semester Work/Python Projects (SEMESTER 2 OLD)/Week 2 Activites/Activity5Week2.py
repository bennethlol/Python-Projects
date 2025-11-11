from random import randint

temp = randint(-10, 10)

print('Temperature is', temp)

if (temp < 5):
    if (temp < 0):
        print('Freezing')
    else:
        print('Too cold')
else:
    print('Mild Weather')