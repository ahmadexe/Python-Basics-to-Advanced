n = int(input('Enter a number: '))
x = int(input('Enter the number you want to divide your first number by: '))

try:
    
    z = n/x
    print(z)
except ZeroDivisionError as e:
    print("You cant divide a number by zero.")

