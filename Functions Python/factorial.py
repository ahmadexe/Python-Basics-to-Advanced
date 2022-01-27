def factorial(x):
    product = 1    
    for i in range (1, x+1):
        product = product * i
        i += 1
    return(print(product))



factorial(5), factorial(6)