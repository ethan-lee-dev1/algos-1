# Two Sum

# Write a function, two_sum, that takes in a list and a target sum as arguments. 
# The function should return a tuple containing a two of indices whose elements sum to the given target. 
# The indices returned must be unique.
# Be sure to return the indices, not the elements themselves.
# There is guaranteed to be one such two that sums to the target.


def two_sum(numbers, target_sum):
    hash = {}
    for i, num in enumerate(numbers):
        complement = target_sum - num
    # print(hash)
        if complement in hash:
            return (hash[complement], i)
        else:
            hash[num] = i
# TEST CASES
print(two_sum([3, 2, 5, 4, 1], 8)) # -> (0, 2)
print(two_sum([4, 7, 9, 2, 5, 1], 5)) # -> (0, 5)
print(two_sum([4, 7, 9, 2, 5, 1], 3)) # -> (3, 5)
print(two_sum([1, 6, 7, 2], 13)) # -> (1, 2)
print(two_sum([9, 9], 18)) # -> (0, 1)
print(two_sum([6, 4, 2, 8 ], 12)) # -> (1, 3)
