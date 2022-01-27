def main(a,b,c,d):
    n1 = eval(a)
    n2 = eval(b)
    n3 = eval(c)
    n4 = eval(d)
    d = ((((n3 - n1)**2) + ((n4 - n2)**2)))**(1/2)
    print(d)
    if d < 6:
        print(f"The points are {d} units apart. They lie close to eachother.")
    else:
        print(f"The points are {d} units apart. They are not close to each other.")
x1 = input("Enter the x1 coordinate: ")
y1 = input("Enter the y1 coordinate: ")
x2 = input("Enter the x2 coordinate: ")
y2 = input("Enter the y2 coordinate: ")
main(x1, y1, x2 , y2)

