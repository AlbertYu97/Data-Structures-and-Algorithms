#def mergesortedarr(a,b):
#  x=a+b
#  x.sort()
#  return x

def mergeSortedArray(array1, array2):
    # Deal with empty array
    if len(array1) == 0 or len(array2) == 0:
        return array1 + array2

    merged_array = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):

        if array1[i] > array2[j]:
            merged_array.append(array2[j])
            j = j + 1

        else:
            merged_array.append(array1[i])
            i = i + 1

    merged_array = merged_array + array1[i:] + array2[j:]

    return merged_array
