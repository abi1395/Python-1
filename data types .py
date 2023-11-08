Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

#int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
>>> print(type(10)) 
<class 'int'>

#a float is a data format that represents a number involving a decimal point
>>> print(type(3.14))
<class 'float'>

#a complex number is represented in the form of “a + bi'. In Python, we use the j or J
>>> print(type(1+3j))
<class 'complex'>

#The str() function converts the specified value into a string. String is a collection of alphabets, words or other characters
>>> print(type('abi'))
<class 'str'>

#Lists in Python can be created by just placing the sequence inside the square brackets[]
>>> print(type([1, 2, 3]))
<class 'list'>

#Dictionaries are used to store data values in key:value pairs.
>>> print(type({'name' : 'abi'}))
<class 'dict'>

#Set is a data type in python used to store several items in a single variable.
>>> print(type({9.8, 3.14, 2.7}))
<class 'set'>

#Tuples are used to store multiple items in a single variable.
>>> print(type((9.8, 3.14, 3.7)))
<class 'tuple'>
