def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    if second == float('-inf'):
        return None  # no second largest
    return second
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))
result = second_largest(arr)
if result is None:
    print("No second largest number (need at least 2 unique numbers).")
else:
    print("Second largest:", result)