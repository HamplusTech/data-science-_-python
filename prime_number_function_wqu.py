def is_prime(number):
    if number <= 1:
        return False
    
    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True

def print_primes(n):
    for number in range(1, n):
        if is_prime(number):
            print('%d is prime' % number)

list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
prime_list = []
for number in list_of_numbers:
    if is_prime(number):
        prime_list.append(number)
print(prime_list)

print([number for number in list_of_numbers if is_prime(number)])

