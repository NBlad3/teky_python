def binary_search(arr, low, high, value):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            return binary_search(arr, low, mid - 1, value)
        else:
            return binary_search(arr, mid + 1, high, value)
    else:
        return -1

arr = [2, 4, 6, 8, 10, 12, 14, 16]
value = 10
result = binary_search(arr, 0, len(arr) - 1, value)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")


 