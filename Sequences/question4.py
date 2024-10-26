# Write a function that accepts a list of strings and returns a new list where each string is reversed. 
# For example, for the input ["apple", "banana", "cherry"], the function should return ["elppa", "ananab", "yrrehc"].



def reverse_strings(strings):
    reversed_list = []
    for s in strings:
        reversed_list.append(s[::-1])
    return reversed_list


words = ["apple", "banana", "cherry"]
print("Reversed strings:", reverse_strings(words))
