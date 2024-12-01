#6. Write a function to count the vowels in a given string.
def count_vowel(n):
    vowels = 'aeiouAEIOU'
    count =0 
    for char in n :
        if char in vowels:
            count += 1
            return count
input_user=input("Enter a String: ")
print ("The number of vowels in your string is : ", count_vowel(input_user))