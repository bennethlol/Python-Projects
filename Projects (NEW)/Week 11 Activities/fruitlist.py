# Create a file with a list of words and display them all on a new line.

with open("fruits.txt", "w") as file:
    file.write('Apple\n')
    file.write('Mango\n')
    file.write('Banana\n')
    file.write('Tomato\n')
    file.write('Mel\n')
    file.write('Lime\n')
    file.write('Kiwi\n')
with open("fruits.txt", "r") as file:
    fruits = list(file)

fruits.sort()
for fruit in fruits:
    print(fruit.strip())