shirts = ['blue shirt xl', 'blue shirt xl', 'black shirt medium', 'grey shirt large', 'white shirt small']
jeans = ['blue large', 'brown medium', 'brown medium', 'blue medium']
bags = ['red bag', 'adidas air', 'nike zero', 'dell g5', 'zara']
perfumes = ['versace','gucci','demi louvato','allure','fragrance de paris','ck into you']

while True:
    print('''Welcome to H&M!
    1. View shirts.
    2. Buy Shirts.
    3. View Jeans.
    4. Buy Jeans.
    5. View Bags.
    6. Buy bags.
    7. View Perfumes
    8. Buy Perfumes
    9. Exit''')
    c = int(input("Enter your Choice: "))
    if c == 1:
        print(shirts)
    if c == 2:
        try:
            s = input("Enter the name of item you want: ").lower()
            shirts.remove(s)
            print("Thanks for buying.")
        except ValueError as e:
            print("This item isn't available at the moment.")
    if c == 3:
        print(jeans)
    if c == 4:
        try:
            j = input("Enter the name of Item: ").lower()
            jeans.remove(j)
            print("Thanks for buying.")
        except ValueError as e:
            print("This item isnt available.")
    if c == 5:
        print(bags)
    if c == 6:
        try:
            bag = input("Enter the name of Item: ").lower()
            bags.remove(bag)
            print("Thanks for buying.")
        except ValueError as e:
            print("This item isnt available.")
    if c == 7:
        print(perfumes)
    if c == 8:
        try:
            p = input("Enter the name of Item: ").lower()
            perfumes.remove(p)
            print("Thanks for buying.")
        except ValueError as e:
            print("This item isnt available.")
    
    if c == 9:
        break

print("Thanks for shopping!")
