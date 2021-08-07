def binary_search(arr, find):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == find:
            return mid
        elif arr[mid] < find:
            left = mid + 1
        else:
            right = mid - 1

    return False


data = [1, 2, 3]

find_data = binary_search(data, 4)

if find_data:
    print("Data found at index:", find_data)
else:
    print("Data not found!")
