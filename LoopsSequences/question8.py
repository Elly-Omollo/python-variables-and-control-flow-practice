# Write a function that takes a dictionary and an integer n as input and
#  returns a list of keys from the dictionary where the value is greater than n. 
# For example, for the dictionary {'a': 5, 'b': 12, 'c': 3} and n = 4, the function should return ['a', 'b'].


def keys_greater_than_n(d, n):
    result = []
    for key, value in d.items():
        if value > n:
            result.append(key)
    return result


sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print("Keys with values greater than", n, "are", keys_greater_than_n(sample_dict, n))
