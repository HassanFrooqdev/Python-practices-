#4. Create a function that takes a list of integers
# and returns the sum of all even numbers.
def sum_of_even_numbers(numbers):
    # Initialize a sum variable
    total = 0
    
    # Iterate through the list
    for number in numbers:
        if number % 2 == 0:
            total += number
    
    return total

# Example list of integers
numbers_list = [3, 41, 12, 9, 74, 15, 28]

# Call the function and print the result
print("The sum of all even numbers in the list is:", sum_of_even_numbers(numbers_list))
