'''
Count Subarrays

Misha likes finding all Subarrays of an Array. Now she gives you an array A of N elements and told you to find the number of subarrays of A, that have unique elements.
Since the number of subarrays could be large, return value % 109 +7.

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 106

Example Input
Input 1:
 A = [1, 1, 3]
Input 2:
 A = [2, 1, 2]


Example Output
Output 1:
 4
Output 1:
 5
'''

class Solution:
    # create a set for recurring elements
    # keep inc j and our unique subset uptil that j will be (j-i+1)
    # if you encounter a recurring element start inc i and remove a[i] from set until we have unique elements
    def solve(self, a):
        sett = set()
        i = 0
        j = 0
        
        count =0
        
        while j<len(a) and i<len(a):
            if a[j] not in sett:
                sett.add(a[j])
                count += (j-i+1)
                j += 1
            else:
                sett.remove(a[i])
                i += 1
        return count
# TC: O(n)
# SC: O(n) 