list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
for num in list1:
    if num % 2 == 0:
        print(num)
for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('odd number')
list_sum = 0
for num in list1:
    list_sum = list_sum + num
print(list_sum)
list_sum = 0
for num in list1:
    list_sum += num
print(list_sum)
for letter in 'this is a string':
    print(letter)
tup = (1,2,3,4,5)
for t in tup:
    print(t)
list2 = [(2,4), (6,8), (10,12)]
for tup in list2:
    print(tup)
for (t1,t2) in list2:
    print(t1)
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)
print(d.items())
for k,v in d.items():
    print(k)
    print(v)
print(list(d.keys()))
print(sorted(d.values()))

