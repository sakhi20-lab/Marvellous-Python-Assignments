numbers = []
for i in range(5):
    while True:
        try:
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number

print("The largest number is:", largest_number)