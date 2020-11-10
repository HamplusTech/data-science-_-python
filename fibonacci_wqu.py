def first_n_fibonacci(n):
    prev_num = 0
    curr_num = 1
    count = 2

    print(prev_num)
    print(curr_num)

    while count <= n:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
        count += 1

def below_x_fibonacci(x):
    prev_num = 0
    curr_num = 1

    if curr_num < x:
        print(prev_num)
        print(curr_num)
    elif prev_num < x:
        print(prev_num)
    
    while curr_num + prev_num < x:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num



m = 7
print('First %d Fibonacci numbers' % m)
first_n_fibonacci(m)


print()

y = 40
print('Fibonacci numbers below %d' % y)
below_x_fibonacci(y)


def first_n_fibonacci_while(n):
    prev_num = 0
    curr_num = 1
    count = 2

    print(prev_num)
    print(curr_num)

    while count <= n:
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num
        count += 1

def first_n_fibonacci_for(n):
    prev_num = 0
    curr_num = 1

    print(prev_num)
    print(curr_num)

    for count in range(2, n + 1):
        next_num = curr_num + prev_num
        print(next_num)
        prev_num = curr_num
        curr_num = next_num


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1)  + fibonacci_recursive(n-2)
