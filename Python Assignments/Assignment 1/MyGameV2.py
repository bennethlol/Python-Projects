from random import randint

# Each player rolls the dice twice. Adds both rolls together to get final score.
player1r1 = randint(1,6)
player1r2 = randint(1,6)
p1score = player1r1 + player1r2
print('Player 1 has rolled ', player1r1, 'and', player1r2)
print('Player 1s total score is', p1score)
player2r1 = randint(1,6)
player2r2 = randint(1,6)
p2score = player2r1 + player2r2
print('Player 1 has rolled ', player2r1, 'and', player2r2)
print('Player 2s total score is', p2score)
player3r1 = randint(1,6)
player3r2 = randint(1,6)
p3score = player3r1 + player3r2
print('Player 1 has rolled ', player3r1, 'and', player3r2)
print('Player 3s total score is', p3score)


# Find the highest score out of all the players using the max funtion.
highest = max(p1score, p2score, p3score)
print('The highest score between the three players was', highest)