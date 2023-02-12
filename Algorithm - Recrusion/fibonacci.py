def fibonacci_Iter(n):
    array = [0, 1]
    for i in range(2, n):
        array.append(array[-1] + array[-2])
    return array[-1]

# Time O(n)
print(fibonacci_Iter(8))

def fibonacci_Rec(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_Rec(n-1) + fibonacci_Rec(n-2)

# Time O(2^n) exponential time
print(fibonacci_Rec(9))
