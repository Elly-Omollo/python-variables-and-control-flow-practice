# Write a Python function that accepts a list of integers and a target sum. 
# The function should return True if there are two distinct numbers 
# in the list that add up to the target sum, 
# and False otherwise.


def has_pair_with_sum(nums, target_sum):
    seen = set()
    for num in nums:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False


numbers = [1, 2, 3, 4, 5]
target = 9
print(f"Has pair with target sum:", has_pair_with_sum(numbers, target))
