# Find the sum of two numbers
def add_numbers(num1, num2):
    """Returns the sum of two numbers.

  Args:
    num1: The first number.
    num2: The second number.

  Returns:
    The sum of num1 and num2.
  """
    return num1 + num2


# Get the input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum of the two numbers
sum = add_numbers(num1, num2)

# Print the sum to the console
print("The sum of the two numbers is: {}".format(sum))
