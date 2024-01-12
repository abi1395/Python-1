my_dict = {'key1' : 'value1' , 'key2' : 'value2'}
print(my_dict)
print(my_dict['key2'])
my_dict = {'key1' : 123, 'key2' : {12,22,33}, 'key3':['item0','item1','item2']}
print(my_dict['key3'])
print(my_dict['key3'][0])
print(my_dict['key3'][0].upper())
print(my_dict['key1'])
my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])
my_dict['key1'] -= 123
print(my_dict['key1'])
d = {}
d['animal'] = 'dog'
d['answer'] = 42
print(d)
