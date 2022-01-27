a = 29
def func():
    global a
    print(a)
    a = 19
    print(a)
func()


