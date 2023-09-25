def reverse_string(string):
    """Reverses the given string and returns the reversed string."""
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string


# Example usage:

print(reverse_string("hello"))  # olleh
print(reverse_string("world"))  # dlrow
