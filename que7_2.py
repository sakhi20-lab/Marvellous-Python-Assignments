input_string = input("Enter a list of integers separated by spaces: ")
string_list = input_string.split()
integer_list = []

for element in string_list:
  try:
    integer_list.append(int(element))
  except ValueError:
    print(f"Invalid input: '{element}' is not an integer.")

doubled_list = list(map(lambda x: x * 2, integer_list))

print("Original list:", integer_list)
print("Doubled list:", doubled_list)