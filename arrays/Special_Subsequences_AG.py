'''
Special Subsequences "AG"

You have given a string A having Uppercase English letters.
You have to find that how many times subsequence "AG" is there in the given string.
NOTE: Return the answer modulo 109 + 7 as the answer can be very large.

Constraints:
1 <= length(A) <= 105

input: "ABCGAG"
output: 3

input: "GAB"
output: 0
'''

def solve(a):
    # count all A and add it to the final sum when you reach G
    count_a = 0
    count = 0
    for i in range(len(a)):
        if a[i] == 'A':
            count_a += 1
        elif a[i] == 'G':
            count += count_a
    return count % (10**9 + 7)