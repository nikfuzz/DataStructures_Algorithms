'''
Replicating Substring

Given a string B, find if it is possible to re-order the characters of the string B so that it can be represented as a concatenation of A similar strings.
Eg: B = aabb and A = 2, then it is possible to re-arrange the string as "abab" which is a concatenation of 2 similar strings "ab".
If it is possible, return 1, else return -1.

Problem Constraints
1 <= Length of string B <= 1000
1 <= A <= 1000
All the alphabets of S are lower case (a - z)

Example Input
Input 1:
 A = 2
 B = "bbaabb"

Input 2:
 A = 1
 B = "bc"


Example Output
Output 1:
 1

Output 2:
 1
'''

# if we need to divide B equally into A parts then we need
# equal no of a char in all A parts
# make a frequency hashmap of all chars in B and 
# check if the frequency of all chars is divisible by a
class Solution:
    def solve(self, a, b):
        if len(b)%a != 0:
            return -1
        map = {}
        for i in range(len(b)):
            if b[i] not in map:
                map[b[i]] = 1
            else:
                map[b[i]] += 1
        for i in map:
            if map[i] % a != 0:
                return -1
        return 1
# TC O(n)
# SC O(n)