'''
Shaggy and distances

Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that array as a special pair if elements at that index in the array are equal.
Shaggy wants you to find a special pair such that distance between that pair is minimum. Distance between two indices is defined as |i-j|. If there is no special pair in the array then return -1.

Problem Constraints
1 <= |A| <= 105

Example Input
Input 1:
A = [7, 1, 3, 4, 1, 7]
Input 2:
A = [1, 1]


Example Output
Output 1:
 3
Output 2:
 1
'''

class Solution:
    # store num->index in map
    # If the number occurs more than once check the diff between the indexes
    def solve(self, a):
        map = {}
        ans = float('inf')
        for i in range(len(a)):
            if a[i] not in map:
                map[a[i]] = i
            else:
                ans = min(ans,abs(map[a[i]]-i))
                # update the number's index to latest
                map[a[i]] = i
        if ans == float('inf'):
            return -1
        return ans
# TC O(n)
# SC O(n)