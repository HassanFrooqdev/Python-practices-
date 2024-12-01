#5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.
def gcd(a, b):
    # Base case
    if b == 0:
        return a
    else:
        # Recursive case
        return gcd(b, a % b)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function and print the GCD
print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))
