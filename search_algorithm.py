def search_algorithm(arr, target, index=0):
    """
    Recursive searching algorithm to search for a number in a list
    """
    if index == len(arr):
        return -1  # Number not found
    if arr[index] == target:
        return index
    return search_algorithm(arr, target, index + 1)


if __name__ == "__main__":
    numbers = [5, 8, 2, 10, 3, 6]
    target = int(input("Enter a number to search: "))
    result = search_algorithm(numbers, target)

    if result != -1:
        print(f"Number {target} found at index {result}.")
    else:
        print(f"Number {target} not found in the list.")
