#1. Create a function that takes a list of numbers and returns the largest number.
def find_largest(numbers):
    # Check if the list is empty
    if not numbers:
        return None
    
    # Assume the first number is the largest initially
    largest = numbers[0]
    
    # Iterate through the list
    for number in numbers:
        if number > largest:
            largest = number
    
    return largest

numbers_list = [3, 41, 12, 9, 74, 15]

# Call the function and print the result
print("The largest number in the list is:", find_largest(numbers_list))
