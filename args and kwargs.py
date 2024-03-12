def myfunc (a,b):
    return sum ((a,b))*.05
print(myfunc(40,60))

def myfunc (a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05
print(myfunc(40,60,20))

def myfunc(*args):
    return sum(args)*.05
print(myfunc(40,60,20))

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"my fav fruit is {kwargs['fruit']}")
    else:
        print("i don't like fruit")
print(myfunc(fruit='pineapple'))
print(myfunc())

def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"i like {' and '.join(args)} and my fav fruit is {kwargs['fruit']}")
        print(f"may i have some {kwargs['juice']} juice?")
    else:
        pass
print(myfunc('eggs','spam', fruit='cherries',juice='orange'))
