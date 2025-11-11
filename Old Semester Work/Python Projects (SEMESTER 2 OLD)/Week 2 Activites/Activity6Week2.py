grade = input('Enter the grade: ')

if grade > '80':
    print('A')
elif '70' < grade <= '80':
    print('B')
elif '60' < grade <= '70':
    print('C')
elif '50' < grade <= '60':
    print('D')
else:
    print('F')
