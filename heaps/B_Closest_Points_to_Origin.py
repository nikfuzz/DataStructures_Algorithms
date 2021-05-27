'''
B Closest Points to Origin

We have a list A, of points(x,y) on the plane. Find the B closest points to the origin (0, 0).
Here, the distance between two points on a plane is the Euclidean distance.
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)
NOTE: Euclidean distance between two points P1(x1,y1) and P2(x2,y2) is sqrt( (x1-x2)2 + (y1-y2)2 ).

Problem Constraints
1 <= B <= length of the list A <= 100000
-100000 <= A[i][0] <= 100000
-100000 <= A[i][1] <= 100000

Example Input
Input 1:

 A = [ 
       [1, 3],
       [-2, 2] 
     ]
 B = 1
Input 2:

 A = [
       [1, -1],
       [2, -1]
     ] 
 B = 1


Example Output
Output 1:

 [ [-2, 2] ]
Output 2:

 [ [1, -1] ]
'''

# make a min heap of tuple(distance, index)
# this heap will sort itself on the bases of distance
# pop b elements from the heap and append a[index] for it to get the points
import heapq as heap
class Solution:
    def solve(self, a, b):
        map = {}
        h = []
        for i in range(len(a)):
            dis = a[i][0]**2 + a[i][1]**2
            h.append((dis,i))
        heap.heapify(h)
        res = []
        for i in range(b):
            val = heap.heappop(h)
            res.append(a[val[1]])
        return res
# TC O(n + b*log n) , n is the no of elements in a
# SC O(n)