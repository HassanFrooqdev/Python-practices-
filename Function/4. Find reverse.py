#4. Write a function that takes a string and returns it reversed.
def reverse_string(x):
    return x[::-1]
x = str(input("Enter a string : "))
print(reverse_string(x))