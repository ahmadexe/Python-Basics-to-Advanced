def readfile(name):
    try:
        f = open(name, 'r')
        print(f.read())
        f.close
    except Exception as e:
        print("File not found")

readfile('one.txt')
readfile('two.txt')
readfile('three.txt')
readfile('four.txt')