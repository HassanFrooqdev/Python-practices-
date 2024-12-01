#2. Write a function to find the nth Fibonacci number using recursion.
def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    
    # Base case: If n is 0, return 0
    if n == 0:
        return 0
    
    # Base case: If n is 1, return 1
    elif n == 1:
        return 1
    
    # Recursive case: Return the sum of the two previous Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = 5
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")