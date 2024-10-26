# Given a tuple of numbers, e.g., (10, 20, 30, 40, 50),
#  write a Python function using a loop that returns the largest number in the tuple.

def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


nums = (10, 20, 30, 40, 50)
print("Largest number:", find_largest_number(nums))
