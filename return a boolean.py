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

