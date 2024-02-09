print(list(range (0,11)))
print(list(range(0,12)))
print(list(range(0,11,2)))
print(list(range(0,101,10)))
index_count = 0
for letter in 'abcde':
    print("at index {} the letter is {}". format(index_count,letter))
    index_count += 1
for i, letter in enumerate('abcde'):
    print("at index {} the letter is {}".format(i,letter))

print(list(enumerate('abcde')))

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
print(zip(mylist1,mylist2))

print(list(zip(mylist1,mylist2)))

for item1, item2 in zip(mylist1, mylist2):
    print('for this tuple, first item was {} and second time was {}'.format(item1, item2))

print('x' in ['x', 'y', 'z'])
print('x' in [1,2,3])

print('x' not in ['x', 'y', 'z'])
print('x' not in [1,2,3])

mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

from random import shuffle
print(shuffle(mylist))

from random import randint
print(randint(0,100))

input ('enter something into the box: ')








