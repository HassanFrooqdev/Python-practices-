# 5. Write a function that takes a list and removes all duplicate elements.
def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
example_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("The list with duplicates removed is: ", remove_duplicates(example_list))
