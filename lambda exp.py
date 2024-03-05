def square(num):
    return num ** 2
my_nums = [1,2,3,4,5]
map(square,my_nums)
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
mynames = ['john','cindy','sarah','kelly','mike']
print(list(map(splicer,mynames)))

def check_even(num):
    return num % 2 == 0
nums = [0,1,2,3,4,5,6,7,8,9,10]
filter(check_even,nums)
print(list(filter(check_even,nums)))

def square(num):
    result = num**2
    return result
print(square(4))

def square(num):
    return num**2
print(square(2))

def square (num): return num**2
print(square(2))


lambda num: num ** 2
square = lambda num: num ** 2
print(square(2))

print(list(map(lambda num: num **2, my_nums)))
print(list(filter(lambda n: n % 2 == 0,nums)))