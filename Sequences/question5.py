# Write a Python function that takes a dictionary as input and prints all the keys whose values are even numbers. Example: 
# Given the dictionary {'a': 2, 'b': 3, 'c': 4}, the function should print 'a' and 'c'.


def print_even_keys(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(key)


sample_dict = {'a': 2, 'b': 3, 'c': 4}
print("Keys with even values:")
print_even_keys(sample_dict)
