# merge left list and right list
def merge(left, right):
    ls = []
    left_index, right_index = 0, 0
    # the while loop breaks when one of the index get to the end of the list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            ls.append(right[right_index])
            right_index += 1
        else:
            ls.append(left[left_index])
            left_index += 1
    # Only one list get to the end, need to add the rest of the list
    return ls + left[left_index:] + right[right_index:]

# USe recursion to split
def merge_sort(ls):
    if len(ls) == 1:
        return ls
    mid = len(ls) // 2
    left = ls[:mid]
    right = ls[mid:]
    return merge(merge_sort(left), merge_sort(right))

ls = [ 34, 32, 83, 26, 20, 38, 92, 64]
print(merge_sort(ls))