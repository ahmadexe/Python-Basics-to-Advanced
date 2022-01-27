f = open('poem.txt', 'r')
t = f.read()
if 'twinkle' in t:
    print("Yes it's present.")
else:
    print("No it isn't")
f.close()