x = 25
def printer():
    x = 50
    return x
print(x)
print(printer())

x = 50
def func(x):
    print('x is', x)
    x = 2
    print ('changed local x to', x)
func(x)
print('x is still',x )

x = 50
def func():
    global x 
    print('this function is now using global x')
    print('because of global x is:', x)
    x =2
    print('ran func(), changes global x to', x)
print('before calling func(), x is:', x)
func()
print('value of x (outside of func()) is:', x)
