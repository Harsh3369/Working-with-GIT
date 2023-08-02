def calculator(x, y, operation):
  """
  This function performs the specified operation on two numbers.

  Args:
    x: The first number.
    y: The second number.
    operation: The operation to perform.

  Returns:
    The result of the operation.
  """

  if operation == "add":
    return x + y
  elif operation == "subtract":
    return x - y
  elif operation == "multiply":
    return x * y
  elif operation == "divide":
    return x / y
  else:
    raise ValueError("Invalid operation")