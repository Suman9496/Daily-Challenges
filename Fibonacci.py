# Print the Fibonacci sequence
def fibonacci(n):
  """Returns the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to return.

  Returns:
    The nth Fibonacci number.
  """
  if n < 0:
    raise ValueError("n must be a non-negative integer")
  elif n == 0 or n == 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

# Get the input from the user
n = int(input("Enter the number of Fibonacci numbers to print: "))

# Print the Fibonacci sequence
for i in range(n):
  print(fibonacci(i))
