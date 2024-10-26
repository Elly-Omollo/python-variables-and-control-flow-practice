# Write a function that takes a list of tuples as input, 
# where each tuple contains two elements: a string and an integer (e.g., ("apple", 5)).
#The function should return a dictionary where the strings are the keys and the integers are the values.


def list_to_dict(tuples_list):
    result = {}
    for item in tuples_list:
        key, value = item
        result[key] = value
    return result


tuples = [("apple", 5), ("banana", 3), ("cherry", 7)]
print("Dictionary:", list_to_dict(tuples))
