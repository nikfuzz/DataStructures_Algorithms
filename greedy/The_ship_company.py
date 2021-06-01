'''
The ship company

The local ship renting service has a special rate plan:

It is up to a passenger to choose a ship.
If the chosen ship has X (X > 0) vacant places at the given moment, then the ticket for such a ship costs X.
The passengers buy tickets in turn, the first person in the queue goes first, then goes the second one, and so on up to A-th person.

You need to tell the maximum and the minimum money that the ship company can earn if all A passengers buy tickets.

Problem Constraints
1 ≤ A ≤ 3000
1 ≤ B ≤ 1000
1 ≤ C[i] ≤ 1000
It is guaranteed that there are at least A empty seats in total.

Example Input
Input 1:

 A = 4
 B = 3
 C = [2, 1, 1]
Input 2:

 A = 4
 B = 3
 C = [2, 2, 2]


Example Output
Output 1:

 [5, 5]
Output 2:

[7, 6]
'''

# make a min heap and max heap for arr c
# to calculate the min value we need to keep checking the min val in the arr each time in the range a, since we want to 
# minimize the cost
# Reverse is true while calculating max value for the ship, we consider max ticket price at a given time
import heapq as heap
class Solution:
    def solve(self, a, b, c):
        mi_h = []
        ma_h = []
        
        for i in range(len(c)):
            heap.heappush(mi_h, c[i])
            heap.heappush(ma_h, -1 * c[i])
        mi = 0
        for i in range(a):
            val = heap.heappop(mi_h)
            mi += val
            if val-1 != 0:
                heap.heappush(mi_h, val-1)
        ma = 0
        for i in range(a):
            val = -1 * heap.heappop(ma_h)
            ma += val
            if val-1 != 0:
                heap.heappush(ma_h, -1 * (val-1))
        return [ma,mi]
# TC O(n)
# SC O(n)