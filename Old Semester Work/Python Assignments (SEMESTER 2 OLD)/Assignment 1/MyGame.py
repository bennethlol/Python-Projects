from random import randint

# Each player "rolls the dice" and gets a random number from 1 to 6.
player1 = randint(1,6)
print('Player 1 has rolled ', player1)
player2 = randint(1,6)
print('Player 2 has rolled ', player2)
player3 = randint(1,6)
print('Player 3 has rolled ', player3)

# Find the highest roll out of all the players using the max funtion.
highest = max(player1, player2, player3)
print('The highest roll between the three players was', highest)