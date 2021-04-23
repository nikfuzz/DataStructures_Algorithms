'''
Sort Array in given Order

Given two array of integers A and B, Sort A in such a way that the relative order among the elements will be the same as those are in B. For the elements not present in B, append them at last in sorted order.
Return the array A after sorting from the above method.
NOTE: Elements of B are unique.

Problem Constraints
1 <= length of the array A <= 100000
1 <= length of the array B <= 100000
-10^9 <= A[i] <= 10^9

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = [5, 4, 2]

Input 2:
A = [5, 17, 100, 11]
B = [1, 100]

Example Output
Output 1:
[5, 4, 2, 1, 3]

Output 2:
[100, 5, 11, 17]
'''
class Solution:
    # map elements of arr a with their frequency
    def solve(self, a, b):
        map = {}
        for i in range(len(a)):
            if a[i] in map:
                map[a[i]] += 1
            else:
                map[a[i]] = 1
        
        res = []
        # for each element in b that is present in a, add the element in res
        # subtract the frequency from the map
        for i in range(len(b)):
            if b[i] in map:
                while map[b[i]] > 0:
                    res.append(b[i])
                    map[b[i]] -= 1
        # for all elements in map having frequency more than 0, need to be added in a temp arr
        # this will give us remaining a elements
        temp = []
        for i in range(len(a)):
            while map[a[i]] > 0:
                temp.append(a[i])
                map[a[i]] -= 1
        temp.sort()
        for i in range(len(temp)):
            res.append(temp[i])
        return res
# TC O(max(len(a),len(b)))
# SC O(len(a))
        
