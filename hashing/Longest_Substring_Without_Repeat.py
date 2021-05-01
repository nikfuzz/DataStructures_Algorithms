'''
Longest Substring Without Repeat

Given a string A, find the length of the longest substring without repeating characters.
Note: Users are expected to solve in O(N) time complexity.

Problem Constraints
1 <= size(A) <= 106
String consists of lowerCase,upperCase characters and digits are also present in the string A.

Example Input
Input 1:

 A = "abcabcbb"
Input 2:
 A = "AaaA"


Example Output
Output 1:
 3

Output 2:
 2
'''

class Solution:
    # two pointers - i and j
    # keep adding elements until you reach an element which is already in set, inc j and update ans
    # if the element is present in set then inc i and keep removing a[i] from set until a[j] is not present in the set
	def lengthOfLongestSubstring(self, a):
	    sett = set()
	    i = 0
	    j = 0
	    
	    ans = 0
	    
	    while i<len(a) and j<len(a):
	        if a[j] not in sett:
	            sett.add(a[j])
	            ans = max(ans,(j-i+1))
	            j += 1
	        else:
	            while a[j] in sett:
	                if a[i] in sett:
	                    sett.remove(a[i])
	                i += 1
	    return ans
# TC O(n)
# SC O(n)
