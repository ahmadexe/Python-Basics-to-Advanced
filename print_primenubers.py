n = int(input("Enter the range,\n"))
i = 1

while i != n:
    c = 0
    i += 1
    for j in range (1, i+1):
        if i % j == 0:
            c = c + 1
        
        
    if c == 2:
        print(i)
    
        
           