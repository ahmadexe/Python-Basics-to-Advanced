i = int(input("Enter the number: "))
j = 0
c = 0
while j != i:
    j += 1
    if i%j == 0:
        c += 1

if c == 2:
    print("Yes the is prime.")
else:
    print("The number isn't prime.")