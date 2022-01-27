main = True
while True:
    name = str(input("Enter the name of student: "))
    if main == True:
        while True:
            print(
            '''
            1. Enter fee details.
            2. Enter subject and marks
            3. Enter attendance summary.
            4. Exit.
            '''        )        
            c = int(input("Enter your choice: "))
            if c == 1:
                a = str(input("Fee of this month has been paid?"))
                print('Noted')
            if c == 2:
                b = str(input('Enter subject and marks: '))
                print("Noted.")
            if c == 3:
                z = str(input("Enter marks of any subject: "))
                print("Noted.")
            if c == 4:
                break
    break


f = open('info.txt', 'a')
f.write(f"\n{name},{a}, {b}, {z}")
f.close()