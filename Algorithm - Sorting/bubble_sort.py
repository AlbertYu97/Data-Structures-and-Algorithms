def bubble_sort(ls):
    for end_index in range(len(ls) - 1, 0, -1):
        for i in range(0, end_index):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
        print(ls)
    return ls

ls = [2, 3, 8, 5, 10, 29, 4]
print(bubble_sort(ls))

# Time complexity O(n^2), space complexity O(1)
