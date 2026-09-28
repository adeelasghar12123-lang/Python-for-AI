def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":

    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_value = 23
    result = binary_search(sorted_numbers, target_value)
    if result != -1:
        print(f"Element {target_value} found at index {result}") 
    else:
        print(f"Element {target_value} not found in the array")

