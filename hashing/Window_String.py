'''
Window String

Given a string A and a string B, find the window with minimum length in A which will contain all the characters in B in linear time complexity.
Note that when the count of a character c in B is x, then the count of c in minimum window in A should be at least x.
Note:
If there is no such window in A that covers all characters in B, return the empty string.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index )

Problem Constraints
1 <= size(A), size(B) <= 106

Example Input
Input 1:
 A = "ADOBECODEBANC"
 B = "ABC"

Input 2:
 A = "Aa91b"
 B = "ab"


Example Output
Output 1:
 "BANC"

Output 2:
 "a91b"
'''
class Solution:
    # we will use two pointer approach and hash map
    # map all the b elements with their frequency
	def minWindow(self, a, b):
	    if len(a)<len(b):
	        return ""
	    map = {}
	    for i in range(len(b)):
	        if b[i] not in map:
	            map[b[i]] = 1
	        else:
	            map[b[i]] += 1
	    i = 0
	    j = 0
	    start = 0
	    ans = float('inf')
	    count = 0
        # we keep inc j until count != len(b)
        # once we have all the elements of b in our window, we will try to min the size of the window by inc i
        # we will inc i only if inc will not kick any b char from the window. But if we have a space of that char, map[a[i]]<0,
        # then we can inc i
	    while j<len(a) and i<len(a):
	        if a[j] not in map:
	            j += 1
	            continue
	        map[a[j]] -= 1
	        if map[a[j]] >= 0:
	            count += 1
	        if count == len(b):
	            while (a[i] not in map) or map[a[i]] < 0:
	                if a[i] in map:
	                    map[a[i]] += 1
	                i += 1
	            if ans > (j-i+1):
	                ans = (j-i+1)
	                start = i
	        j += 1
	    if ans == float('inf'):
	        return ""
	    return a[start:(ans+start)]
	        


