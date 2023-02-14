# Move the smallest value to top

def selection_sort(ls):
    for i in range(0, len(ls)):
        # set current index as minimum
        min_val = ls[i]
        index = i
        for j in range(i+1, len(ls)):
            if ls[j] < min_val:
                # Update min_val if current value is lower
                min_val = ls[j]
                index = j
        # Switch numbers at two indexes
        ls[i], ls[index] = ls[index], ls[i]
    return ls

ls = [ 8, 5, 4, 2, 1, 6]
print(selection_sort(ls))

# Time complexity O(n^2), space complexity O(1)