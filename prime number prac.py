n = int(input("Enter the range: "))
i = 0
while n != i:
    c = 0
    i += 1
    for j in range (1, i+1):
        if i % j == 0:
            c += 1

    if c == 2:
        print(i) 

