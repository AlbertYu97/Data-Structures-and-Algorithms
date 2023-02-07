# The goal is to write a function that takes a string as input and returns the
# first character that appears more than once in the string, or None if
# no such character exists.

# Naive approach nested loop, time complexity O(n^2), space complexity O(1)
def first_recurring(array):
    repeat_index = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            # store all repeated indexes in a list and choose the min
            if array[i] == array[j]:
                repeat_index.append(array[j])
        return array[min(repeat_index)]
    return "undefined"

# By storing all the repeated indexes, we avoid edge cases like [2,5,5,2,3,5]
# With just a nested loop, this would return 2, which is not the first recurring
# character. By storing all repeated indexes, we correctly return 5

# With hash table, we reduce time complexity to O(n) and  sacrifice the space complexity
# to O(n)

def first_recurring_char(array):
    char_collection = {}
    for i in array:
        if i in char_collection:
            return i
        else:
            char_collection[i] = 1
    return "Undefined"



