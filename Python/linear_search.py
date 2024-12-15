def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

print(linear_search([10, 4, 4, 0], 0))