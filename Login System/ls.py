un = str(input("Enter name:"))
pw = str(input("Enter pw:"))
f = open('login.txt', 'a')
f.write(f"\n{un} : {pw}")
f.close()
usern = input("Enter username: ")
passw = input("Enter password: ")
f = open("login.txt", "r")
l = f.readline()
f.close
print(l)
for line in l:
    x = line.split(":")
    if x[0].strip() == usern and x[1].strip() == passw:
        print("You in")
   

    
