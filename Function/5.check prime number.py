#5. Create a function to check if a given number is prime.
def is_prime(n):
    """Check if a number is prime."""
    # Step 1: Check if n is less than or equal to 1
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    # Step 2: Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False  # If n is divisible by i, it is not prime
    
    # Step 3: If no divisors were found, n is prime
    return True

number = 21
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")