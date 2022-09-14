def binary_search(arr, find):
    low = 0
    high = len(arr) - 1

    while low <= high:
        print(low, high, "-" ,low)
        mid = low + (high - low) // 2
        if arr[mid] == find:
            return mid
        elif arr[mid] < find:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [40, 20, 10, 9]
find = 9

result = binary_search(sorted(arr),find)
if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")
