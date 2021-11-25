def RBS(arr, target, first, last):
    if first > last:
        return -1
    mid = (first + last) // 2
    if arr[mid] == target:
        return mid

    # Checking if the first half is sorted
    elif arr[first] <= arr[mid]:

        # if its sorted and target lies in sorted range
        if arr[first] <= target < arr[mid]:
            return RBS(arr, target, first=first, last=mid - 1)

        # if first half is sorted but target lies in other half
        return RBS(arr, target, first=mid + 1, last=last)

    # if first half is not sorted
    # Checking if target is greater than the current mid and last if it is then it will lie in left region
    elif arr[mid] < target > arr[last]:
        return RBS(arr, target, first=first, last=mid - 1)

    # Otherwise it will lie in right region
    return RBS(arr, target, first=mid + 1, last=last)


arr = [5, 6, 1, 2, 3, 4]
length = len(arr)
print(RBS(arr, 2, 0, length - 1))
