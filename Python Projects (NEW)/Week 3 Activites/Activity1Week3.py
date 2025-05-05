#For loop practice

#Print seperate elements of a list
a = [1,3,5,7]
for nums in a:
    print(nums)

#Print all numbers in a range
for num in range(10,21):
    print(num)

#Print all EVEN numbers in a range
for n in range(2,21):
    if n % 2 == 0:
        print(n)

#Print 10 values in the 6 times table
for v in range(1,11):
    print(v * 6)