x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1

x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
else:
    print('all done')

x = 0
while x < 10:
    print('s is currently:', x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x == 3:
        print('x==3')
    else:
        print('continuing...')
        continue 
x = 0
while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('breaking because x ==3')
        break
    else:
        print('continuing...')
        continue 
