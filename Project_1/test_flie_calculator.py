import pytest

from calculator import calculator


def test_add():
  """
  This test ensures that the calculator function correctly adds two numbers.
  """

  result = calculator(10, 20, "add")
  assert result == 30


def test_subtract():
  """
  This test ensures that the calculator function correctly subtracts two numbers.
  """

  result = calculator(10, 20, "subtract")
  assert result == -10


def test_multiply():
  """
  This test ensures that the calculator function correctly multiplies two numbers.
  """

  result = calculator(10, 20, "multiply")
  assert result == 200


def test_divide():
  """
  This test ensures that the calculator function correctly divides two numbers.
  """

  result = calculator(10, 20, "divide")
  assert result == 0.5