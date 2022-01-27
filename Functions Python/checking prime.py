def prime(x):
    c = 0
    for j in range (1,x+1):
        if x % j == 0:
            c += 1
    if c == 2:
        print("The number",x,"is prime")
    else:
        print("The number isn't prime")



prime(6)