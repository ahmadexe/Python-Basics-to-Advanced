mainstr = str(input("Enter a number in format (xxx-xxxx-xxxx): "))
first = mainstr[0:3]
second = mainstr[4:8]
third = mainstr[9:13]
change = second.replace('A', '2').replace('B', "3").replace("C", '4').replace("Z", '2')

print(f'{first}-{change}-{third}')