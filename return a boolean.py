def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
            return False
print(check_even_list([1,2,4]))
print(check_even_list([1,3,5]))

def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
        return even_numbers 
print(check_even_list([1,3,6]))

stock_prices = [('AAPL' ,200),('GOOG' ,300),('MSFT' ,400)]
for items in stock_prices:
    print(items)

for stock,price in stock_prices:
    print(stock)

for stock,price in stock_prices:
    print(price)

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]
def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month,current_max)
print(employee_check(work_hours))


def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a number:0,1, or 2: ")
    return int(guess)
print(player_guess())

def check_guess(mylist,guess):
    if mylist[guess] == 'o':
        print('correct guess')
    else:
        print('wrong better luck next time')
        print(mylist)

mylist = ['','o','']
mixedup_list = shuffle_list(mylist)
guess = player_guess()
print(check_guess(mixedup_list,guess))
