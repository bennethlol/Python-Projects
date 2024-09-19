# Void Functions - no parameters

# Compute Pay 

def computepay(hours, rate):
    pay = int(hours) * int(rate)
    print('Your pay is', pay, 'dollars.')

computepay(input('How many hours do you work? '), input('How much is the hourly rate? '))
  