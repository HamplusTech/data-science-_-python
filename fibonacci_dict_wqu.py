def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci_recursive(n-1) +
                fibonacci_recursive(n-2))

from collections import defaultdict
def fibonacci_count(n, d):
    d[n] += 1
    if n == 0:
        return 0, d
    elif n == 1:
        return 1, d
    else:
        n1, _ = fibonacci_count (n-1, d)
        n2, _ = fibonacci_count (n-2, d)
        return n1+n2, d

n = 5
ans, d = fibonacci_count(n, defaultdict(int))
for i in range(5):
    print(i, d[i])

def fibonacci_memo(n, d):
    if n in d:
        return d[n]
    elif n == 0:
        ans = 0
    elif n == 1:
        ans = 1
    else:
        ans = (fibonacci_recursive(n-1, d) +
                fibonacci_recursive(n-2, d))
    d[n] = ans
    return ans

def percentile (data, rank):
    data = sorted(data)
    idx = int(len(data) * (rank/100))
    return f'The {rank} percentile is {data[idx]}'

