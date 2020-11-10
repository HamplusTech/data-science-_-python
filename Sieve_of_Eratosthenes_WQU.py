def gen_list_true(n):
    return [number > 1 for number in range(n+1)]

def mark_false(bool_list, p):
    for index in range(2*p, len(bool_list), p):
        bool_list[index] = False
    return bool_list

def find_next(bool_list, p):
    for index, element in enumerate(bool_list[p+1:], p+1):
        if element:
            return index
    return None

def prime_from_list(bool_list):
    return [index for index, element in enumerate
            (bool_list) if element]

def sieve(n):
    bool_list = gen_list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)


