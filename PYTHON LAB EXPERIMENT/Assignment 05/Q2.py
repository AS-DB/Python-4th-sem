def remove_duplicates(dictionary):
    unique_values = {}  
    for key, value in dictionary.items():
        if value not in unique_values.values():
            unique_values[key] = value
    return unique_values

# Example dictionary with duplicate values
sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

# Call the remove_duplicates function
result_dict = remove_duplicates(sample_dict)

# Print the original and resulting dictionaries
print("Original Dictionary:", sample_dict)
print("Dictionary with Duplicates Removed:", result_dict)
