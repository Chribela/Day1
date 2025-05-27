# takes input from you.
numbers = []

# Gets the 10 numbers
for i in range(10):
    number = int(input(f"Enter number {i+1} (consecutive number): "))
    numbers.append(number)

# Separate even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print(f"\nEven numbers: {even_numbers}")