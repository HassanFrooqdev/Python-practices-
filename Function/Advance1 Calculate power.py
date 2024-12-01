#1. Write a function that calculates the power of a number without using the ** operator.
def power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        return 1 / result
    return result

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Call the function and print the result
print("The result of", base, "raised to the power of", exponent, "is", power(base, exponent))
