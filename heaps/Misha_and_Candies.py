'''
Misha and Candies

Misha loves eating candies. She has given N boxes of Candies.
She decides, every time she will choose a box having the minimum number of candies, eat half of the candies and put the remaining candies in the other box that has the minimum number of candies.
Misha does not like a box if it has the number of candies greater than B so she won't eat from that box. Can you find how many candies she will eat?
NOTE 1: If a box has an odd number of candies then Misha will eat floor(odd/2).
NOTE 2: A same box will not be chosen again.

Problem Constraints
1 <= N <= 10**5
1 <= A[i] <= 10**5
1 <= B <= 10**6

Example Input
Input 1:

 A = [3, 2, 3]
 B = 4
Input 2:

 A = [1,2,1]
 B = 2


Example Output
Output 1:

 2
Output 2:

 1
'''
# min heapify arr
# take the root box. Add floor(box) to the ans and put the remaining chocolates in the next min box.
# push this new in the heap
import heapq as heap
class Solution:
    def solve(self, a, b):
        heap.heapify(a)
        tc = 0
        # if the boxes are finished or the min box is greater than b return ans
        while len(a) > 0 and a[0]<=b:
            box = heap.heappop(a)
            tc += box//2
            if not a:
                return tc
            next_box = heap.heappop(a)
            next_box += (box - box//2)
            heap.heappush(a,next_box)
        return tc
# TC O(n * log n)
# SC O(n)


