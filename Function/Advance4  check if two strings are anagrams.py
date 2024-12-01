#4. Create a function to check if two strings are anagrams.

def are_anagrams(str1, str2):
    # Remove any spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare sorted versions of the strings
    return sorted(str1) == sorted(str2)

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Call the function and print the result
if are_anagrams(string1, string2):
    print(string1, "and", string2, "are anagrams.")
else:
    print(string1, "and", string2, "are not anagrams.")
