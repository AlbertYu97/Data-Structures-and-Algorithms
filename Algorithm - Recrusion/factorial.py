def factorial_recrusion(num):
    if num == 1:
        return 1
    else:
        return num * factorial_recrusion(num - 1)


def factorial_iterative(num):
    result = 1
    while num != 1:
        result = result * num
        num -= 1
    return result

print(factorial_recrusion(5))
print(factorial_iterative(5))

# Time complexity O(n)
