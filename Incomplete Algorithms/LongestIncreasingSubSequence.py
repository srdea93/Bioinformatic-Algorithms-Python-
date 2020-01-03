# given an array, find the longest increasing subsequence
def longest_increasing_subsequence(sequence):
    j = 0
    i = 1
    count = 1
    longestArr = [1 for x in sequence]



sequence = [3, 4, -1, 0, 6, 2, 3]
print(longest_increasing_subsequence(sequence))