#6. Create a function that accepts a dictionary and returns the key with the highest value.
def key_with_highest_value(d):
    # Check if the dictionary is empty
    if not d:
        return None
    
    # Find the key with the highest value
    highest_key = max(d, key=d.get)
    
    return highest_key

# Example dictionary
example_dict = {'a': 10, 'b': 34, 'c': 56, 'd': 22}

# Call the function and print the result
print("The key with the highest value is:", key_with_highest_value(example_dict))
