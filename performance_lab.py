# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    from collections import Counter
    freq = Counter(numbers) 
    return max(freq, key=freq.get) if numbers else None

print('Problem 1')
print(most_frequent([1, 2, 2, 5, 7, 2, 3])) 
print(most_frequent([5, 5, 6, 6, 6]))        
print(most_frequent([]))    
"""
Time and Space Analysis for problem 1:
- Best-case: O(n) (must scan entire list at least once)
- Worst-case: O(n) (still one scan + dictionary ops)
- Average-case: O(n)
- Space complexity: O(k), k = number of unique elements
- Why this approach? Counter is efficient and optimized for frequency analysis
- Could it be optimized If only one pass is allowed, the prgram allows to use manual dictionary count
"""

# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

print('Problem 2')
print(remove_duplicates([2, 3, 3, 7, 10, 7])) 
print(remove_duplicates([3, 3, 1, 1]))     
print(remove_duplicates([]))                  

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) (set and result list)
- Why this approach? Set provides O(1) membership check, preserving order with list
- Could it be optimized? Not really, no major improvement for Python.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        comp = target - num
        if comp in seen:
            pairs.add(tuple(sorted((num, comp))))
        seen.add(num)
    return list(pairs)
print('Problem 3')
print(find_pairs([1, 10, -3, 6], 7)) 
print(find_pairs([0, 9, 4, 5], 9))  
print(find_pairs([], 5)) 
"""
Time and Space Analysis for problem 3:
- Best-case: O(n) 
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for seen + O(p) for pairs
- Why this approach? Hash lookup makes complement check efficient
- Could it be optimized?  O(n log n) also works, but hash-based is faster for unsorted input
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    arr = [None] * capacity
    size = 0
    for i in range(n):
        if size == capacity:  
            print(f"Resizing from {capacity} to {capacity*2}")
            capacity *= 2
            new_arr = [None] * capacity
            for j in range(size):
                new_arr[j] = arr[j]
            arr = new_arr
        arr[size] = i
        size += 1
    return arr[:size]

print('Problem 4')
print(add_n_items(8))
"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizes happen when size == capacity
- What is the worst-case for a single append? O(n) (copy all items during resize)
- What is the amortized time per append overall? O(1), because doubling spreads cost
- Space complexity: O(n) for the array
- Why does doubling reduce the cost overall? number of copies per element is logarithmic in n, so cost spreads evenly
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    running_sum = 0
    for num in nums:
        running_sum += num
        result.append(running_sum)
    return result

print('Problem 5')
print(running_total([1, 2, 3, 4, 5, 6])) 
print(running_total([5, -4, 6, -2]))    
print(running_total([]))    
"""
Time and Space Analysis for problem 5:
- Best-case: O(n) 
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) 
- Why this approach? Efficient single-pass accumulation
- Could it be optimized? In-place update is possible if overwriting input is acceptable
"""
