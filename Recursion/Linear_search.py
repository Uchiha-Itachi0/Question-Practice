def LinearSearch(arr, target, index):
    if len(arr) == index:
        return -1
    elif arr[index] == target:
        return index
    else:
        return LinearSearch(arr, target, index + 1)


# Searching for multiple index

# taking storage as a global variable
storage = []


def LinearSearch2(arr, target, index):
    if len(arr) == index:
        return
    elif arr[index] == target:
        storage.append(index)
    return LinearSearch2(arr, target, index + 1)


# taking storage as an local variable
def LinearSearch3(arr, target, index):
    local_storage = []
    if len(arr) == index:
        return []
    elif arr[index] == target:
        local_storage.append(index)
    return local_storage + LinearSearch3(arr, target, index + 1)


print(LinearSearch3([1, 1, 2, 3, 4, 5], 1, 0))
