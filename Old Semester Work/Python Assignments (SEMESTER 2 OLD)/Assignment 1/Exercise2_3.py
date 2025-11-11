# Question 1
r = 5
pi = 3.14
v = (4/3)*(pi)*(r**3)
print('Volume of the sphere is:',v)

# Question 2
book = 24.95
bookdis = book - (book*0.40)
wholesale = (bookdis + 3) + ((bookdis + 0.75)*59)
print('Total wholesale cost of 60 books is:',wholesale,'dollars.')

# Question 3
def time(a):
    hours = 6
    minutes = 52
    arrive = minutes + a
    if arrive > 60:
        arrive -= 60
        hours += 1
        msg = print('I will arrive at',hours,arrive,'AM')
    return msg
easymin = 8
easysec = 15
tempomin = 7
temposec = 12

totalmin = (easymin*2) + (tempomin*3)
totalsec = (easysec*2) + (temposec*3)
if totalsec > 60:
    totalsec -= 60
    totalmin += 1

newtime = time(totalmin)
print(newtime)


