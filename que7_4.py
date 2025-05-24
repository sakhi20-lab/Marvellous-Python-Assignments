from functools import reduce
from operator import mul

def product_of_list(numbers):
  
  return reduce(mul, numbers)


numbers = [1, 2, 3, 4, 5]
product = product_of_list(numbers)
print(f"The product of the list is: {product}") 