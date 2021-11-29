# By making copy of an array
# For merging
def merge(arr_1, arr_2):
    storage = []
    i = j = 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] <= arr_2[j]:
            storage.append(arr_1[i])
            i += 1
        else:
            storage.append(arr_2[j])
            j += 1
    while i < len(arr_1):
        storage.append(arr_1[i])
        i += 1
    while j < len(arr_2):
        storage.append(arr_2[j])
        j += 1

    return storage


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        arr_1 = merge_sort(arr[:mid])
        arr_2 = merge_sort(arr[mid:])
        return merge(arr_1, arr_2)


# Without making copy of an array
def in_place_merge(arr, first, mid, last):
    storage = []
    i, j = first, mid + 1
    while i <= mid and j <= last:
        if arr[i] < arr[j]:
            storage.append(arr[i])
            i += 1
        else:
            storage.append(arr[j])
            j += 1
    while i <= mid:
        storage.append(arr[i])
        i += 1
    while j <= last:
        storage.append(arr[j])
        j += 1

    # Coping the answer in arr
    for k in range(len(storage)):
        arr[first + k] = storage[k]


def in_place_merge_sort(arr, first, last):
    if first >= last:
        return arr
    else:
        mid = (first + last) // 2
        in_place_merge_sort(arr, first, mid)
        in_place_merge_sort(arr, mid + 1, last)
        in_place_merge(arr, first, mid, last)


arr = [5, 4, 3, 2, 1]
in_place_merge_sort(arr, 0, len(arr) - 1)
print(arr)
