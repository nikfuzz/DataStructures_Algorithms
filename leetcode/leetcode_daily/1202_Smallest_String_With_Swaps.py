'''
1202. Smallest String With Swaps

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] 
indicates 2 indices(0-indexed) of the string.
You can swap the characters at any pair of indices in the given pairs any number of times.
Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:
1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
'''

# make parent union of all the indexes
# you should get an arr p where each index has its parent as element
# create a dict like 0-> 0,3 where 0 is the parent of the list in its value
# then for each key of the dict sort the corresponding characters in its value list
# then swap the s[ind] with the sorted list of the character

from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        p = [i for i in range(len(s))]
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
                
            return p[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            
            if px != py:
                p[py] = px
                
        for x, y in pairs:
            union(x,y)
            
        dic = defaultdict(list)
        res = list(s)
        
        for ind, ele in enumerate(p):
            dic[find(ele)].append(ind)
            
        for key in dic.keys():
            ind_list = dic[key]
            char_list = [s[i] for i in ind_list]
            char_list.sort()
            
            for ind, char in zip(ind_list, char_list):
                res[ind] = char
                
        return "".join(res)

# time (n log n)
# space O(n)