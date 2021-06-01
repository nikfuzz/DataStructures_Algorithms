'''
Assign Mice to Holes

There are N Mice and N holes that are placed in a straight line. Each hole can accomodate only 1 mouse.
The positions of Mice are denoted by array A and the position of holes are denoted by array B.
A mouse can stay at his position, move one step right from x to x + 1, or move one step left from x to x − 1. Any of these moves consumes 1 minute.
Assign mice to holes so that the time when the last mouse gets inside a hole is minimized.

Problem Constraints
1 <= N <= 10^5
-10^9 <= A[i], B[i] <= 10^9

Example Input
Input 1:

 A = [-4, 2, 3]
 B = [0, -2, 4]
Input 2:

 A = [-2]
 B = [-6]


Example Output
Output 1:

 2
Output 2:

 4
'''
# we need to put ith mouse in the closest hole so
# sort the mice pos arr and the hole arr
# ans = max(ans, abs(b[i]-a[i])), will give the max time
class Solution:
    def mice(self, a, b):
        a.sort()
        b.sort()
        ans = float('-inf')
        for i in range(len(a)):
            ans = max(ans, abs(b[i]-a[i]))
        return ans
# TC O(n*log n)
# SC O(1)
