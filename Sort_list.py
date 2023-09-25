def sort_list(list):
    """Sorts the given list of numbers in ascending order and returns the sorted list."""
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


# Example usage:

list = [5, 3, 2, 1, 4]
sorted_list = sort_list(list)
print(sorted_list)  # [1, 2, 3, 4, 5]
