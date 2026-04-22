def binary_search(arr, target)://function
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid  
        if guess > target:
            high = mid - 1  # Too high, look left.
        else:
            low = mid + 1   # Too low, look right.

    return -1  # Target not found

# Example usage:
my_list = [1,2,3,4]
print(binary_search(my_list, 3)) # Output: 1
print(binary_search(my_list, -1)) # Output: -1
print("done")