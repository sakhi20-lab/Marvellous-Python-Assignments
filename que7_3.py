def get_even_numbers(numbers):
  """
    Filters a list to keep only even numbers.

    Args:
      numbers: A list of numbers.

    Returns:
      A new list containing only the even numbers from the input list.
  """
  even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
  return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)  