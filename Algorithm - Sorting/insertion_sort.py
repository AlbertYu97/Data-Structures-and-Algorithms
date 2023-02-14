# def insertion_sort(ls):
#     # insertion list have maximum length: len(ls) - 2
#     for i in range(0, len(ls)-1):
#         for j in range(0, i+1):
#             # Compare the value right outside the insertion list
#             if ls[i+1] < ls[j]:
#                 # the insertion list is ordered, if the value is lower
#                 # then insert the value to the insertion list and remove the original value
#                 ls.insert(j, ls[i+1])
#                 ls.pop(i+2)
#     return ls

def insertion_sort(ls):
    # new numbers outside the sorted list
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i - 1
        while ls[j] > temp and j >= 0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = temp
    return ls


print(insertion_sort([3, 1, 8, 24, 7, 2, 16, 4]))

# worst case time complexity O(n^2), best case (almost sorted) O(n)