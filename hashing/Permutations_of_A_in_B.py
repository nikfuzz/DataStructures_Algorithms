'''
Permutations of A in B

You are given two strings A and B of size N and M respectively.
You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase letters.

Problem Constraints
1 <= N < M <= 105

Example Input
Input 1:
 A = "abc"
 B = "abcbacabc"

Input 2:
 A = "aca"
 B = "acaa"


Example Output
Output 1:
 5

Output 2:
 2
'''
# we will maintain two frequency hashmaps
# one map will have the pattern string and another will be the search window of the main string
# the window will be from i to j
# for each window check if the window hashmap is equal to the pattern map
class Solution:
    # comparing maps
    def cmp(self,win,map):
        for key in map:
            if key not in win or win[key] != map[key]:
                return 0
        return 1
    
    
    def solve(self, a, b):
        map = {}
        window = {}
        for i in range(len(a)):
            if a[i] not in map:
                map[a[i]] = 1
            else:
                map[a[i]] += 1
        
        # initial window
        for i in range(len(a)):
            if b[i] not in window:
                window[b[i]] = 1
            else:
                window[b[i]] += 1
        
        i=0
        j=len(a)
        count = 0
        if self.cmp(window,map) == 1:
            count += 1
        # create window from i to j of size len(a)
        while j<len(b) and i<len(b):
            if b[j] not in window:
                window[b[j]] = 1
            else:
                window[b[j]] += 1
            window[b[i]] -= 1
            j += 1
            i += 1
            
            if self.cmp(window,map) == 1:
                count += 1
        return count
# TC O(m), m is the len(b) 
# SC O(m), m is the len(b) 