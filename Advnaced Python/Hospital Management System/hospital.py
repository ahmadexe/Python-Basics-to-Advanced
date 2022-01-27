

print('HOSPITAL MANAGMENT SYSTEM')
dates = ['1-5-2021', '2-5-2021', '4-5-2021', '5-5-2021', '7-5-2021', '10-5-2021']
docs = ['Dr. Ahmad (Nuero)', 'Dr. Akhtar (Cardio)', 'Dr. Syeda Sitwat (Gynae)']

main = True

while True:
    print('''
    1. View dates for appointments.
    2. Book a date.
    3. Enter Patient details.
    4. Exit.    
    ''')
    c_main = int(input("Enter your choice: "))
    
    if c_main == 1:
        for item in dates:
            print(item)

    if c_main == 2:
        d = str(input('Enter the date you want to book appointment for, please check the available dates.\n'))
        try:
            print("Date has been booked.")
            dates.remove(d)
        except ValueError as e:
                print("Date isn't available")
        for item in docs:
            print(item)
        doc_c = str(input("Select one of the available doctors, \n"))
        if doc_c in docs:
            print("Date is booked!")
            docs.remove(doc_c)
        else:
            print("This doctor isn't available.")
    if c_main == 3:
        while True:
            print('''
            1. Enter patients name.
            2. Enter disease detail.
            3. Enter age of patient.
            4. Enter gender.
            5. Exit.
            '''

            )
            c = int(input("Enter your choice: "))
            if c == 1:
                pn = str(input("Name: "))
            if c == 2:
                dd = str(input("Enter disease detail."))
            if c == 3:
                ag = str(input("Enter age: "))
            if c == 4:
                g = str(input("Enter gender: "))
            if c == 5:
                break
        break
    

f = open('infos.txt', 'a')
f.write(f"\n{pn},{dd},{ag},{g}.")
f.close()