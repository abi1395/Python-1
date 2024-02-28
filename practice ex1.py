def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min (a,b)
    else:
        return max (a,b)
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(3,5))

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Krazy Kangaroo'))
print(animal_crackers('Tiny Moneky'))

def makes_twenty(n1,n2):
    return(n1+n2) == 20 or n1==20 or n2==20
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short'
print(old_macdonald('macdonald'))

def master_yoda(text):
    return ' '.join(text.split()[::-1])
print(master_yoda('I am home'))
print(master_yoda('We are ready'))

def almost_there(n):
    return ((abs(100-n) <= 10) or (abs(200 - n) <= 10))
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))

def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
    return False
print(has_33([1,3,3]))
print(has_33([1,3,1,3]))
print(has_33([3,1,3]))

def paper_doll(text):
    result = ''
    for char in text:
        result += char * 3
    return result
print(paper_doll('Hello'))
print(paper_doll('Mississppi'))

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum ((a,b,c))
    elif sum((a,b,c)) <= 31 and 11 in (a,b,c):
        return sum ((a,b,c)) - 10
    else:
        return 'bust'
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num !=6:
                total += num
                break
            else:
                add = False
            while not add:
                if num != 9:
                    break
                else:
                    add = True
                    break
    return total
print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))

def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)
print(count_primes(100))

def print_big(letter):
    patterns = {1:' * ',2:' * ',3:' * ',4:'*****',5:'**** ',6:'   * ',7:'  *   ',8:'* * ',9:'*   '}
    alphabet = {'A':[1,2,3,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
print(print_big('a'))
