def mersenne_number(p):
    return (2 ** p) - 1

def mersenne_number_reverse(p):
	return (p ** 1/2) - 1
##
def is_prime(number):
    if number <= 1: return False
    for factors in range(2, number):
        if number % factors == 0: return False
##        elif number % 3 == 0: return False
##        elif number % 5 == 0: return False
    return True
##
def get_primes(n_start, n_end):
    temp = list()
    for number in range(n_start, n_end):
        if is_prime(number):
            temp.append(number)
    return temp

primes_list = get_primes(3,65)
print('primes = ', primes_list)
##
##mersennes = [number for number in get_primes(3,65) if mersenne_number(number)]
##print('mersennes = ', mersennes)
##
####y = [number for number in mersennes if mersenne_number(number)]
####print('y = ', y)
##mersennes_primes = list()
##a = range(3, 65)
##for num in a:
##    if mersenne_number(num) in a:
##        mersennes_primes.append(num)
##print(mersennes_primes)

##def lucas_lehmer (p):
##    n0 = 4
##    np = 0
##    n = list()
##    for i in (range(p-2+1)):
##        if i == 0:
##            np = ((n0 ** 2) - 2) % ((2 ** p) - 1)
##        else:
##            np = ((np ** 2) - 2) % ((2 ** p) - 1)
##        n.append(np)
##    return n

def ll_prime(p):
    count = list()
    mersennes = list()
    a = list(range(3,p))
    for num in a:
        check = is_prime(num)
        if check == mersenne_number(num):
            mersennes.append(num)
            count.append(True)
        else:
            mersennes.append(num)
            count.append(False)
    mersennes = list(zip(mersennes,count))
    return mersennes
ll_prime(65)

def ll_prime2(p=list(range(3,65))):
    count = list()
    mersennes = list()
    for p in p:
        number = is_prime(p)
        if mersenne_number(number):
            mersennes.append(p)
            count.append(True)
        else:
            mersennes.append(p)
            count.append(False)
    mersennes_final = list(zip(mersennes,count))
    return mersennes_final

def ll_prime2_1(p=get_primes(3,65)):
    count = list()
    mersennes = list()
    for p in p:
        number = is_prime(p)
        if mersenne_number(number):
            mersennes.append(p)
            count.append(True)
        else:
            mersennes.append(p)
            count.append(False)
    mersennes_final = list(zip(mersennes,count))
    return mersennes_final

import math
def is_prime_fast(number):
    if number <= 1: return False
    if number == 2: return True
    if number == 3: return True
    if number == 5: return True
    #for factor in range(3,number):
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        return False
    return True

def get_primes_fast(n_start, n_end):
    temp = list()
    for number in range(n_start, n_end):
        if is_prime_fast(number):
            temp.append(number)
    return temp

import math
def is_prime_fast2(number):
    if number <= 1: return False
    if number == 2: return True
    if number > 2 and number % 2 == 0: return False
    for factor in range(2,number):
        if factor % 2 == 0 or factor < math.sqrt(number):
            return True
        return False
