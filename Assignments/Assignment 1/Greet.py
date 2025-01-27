# Version 1: Prints greeting once.
name = input('Please enter your name: ')
print('Good morning', name)

# Version 2: Prints greeting three times.
name = input('Please enter your name: ')
# For loop uses range function to print the greeting message three times.
for n in range(1,4):
    print('Good morning', name)