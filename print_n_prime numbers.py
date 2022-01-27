n = int(input("Enter the range.\n"))
i = 2
while n != 0:
    for j in range (2,i):
        if i % j == 0:
            break 
    else:
        print(i)
        n -= 1
    i += 1
        
        
    