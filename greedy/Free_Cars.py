'''
Free Cars

Given two arrays A and B of size N. A[i] represents the time by which you can buy ith car without paying any money.
B[i] represents the profit you can earn by buying ith car. It takes 1 minute to buy a car so, you can only buy the ith car when the current time <= A[i] - 1.
Your task is to find maximum profit one can earn by buying cars considering that you can only buy one car at a time.
NOTE:
You can stary buying from time = 0.
Return you answer modulo 109 + 7.

Problem Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^9
0 <= B[i] <= 10^9

Example Input
Input 1:

 A = [1, 3, 2, 3, 3]
 B = [5, 6, 1, 3, 9]
Input 2:

 A = [3, 8, 7, 5]
 B = [3, 1, 7, 19]


Example Output
Output 1:

 20
Output 2:

 30
'''
# Sort on the basis of time
# add all the profit one by one for all t<a[i] and add them in a min heap too
# if we come across an i for which b[i] > heap[0] but t >= a[i], then we pop the min profit from the heap and profit
# and add the new b[i]
import heapq as heap
class Solution:
    def solve(self, a, b):
        cars = []
        for i in range(len(a)):
            cars.append((a[i], b[i]))
        cars = sorted(cars, key=lambda x:x[0])
        h = []
        profit = 0
        t = 0
        for i in range(len(cars)):
            if t < cars[i][0]:
                heap.heappush(h, cars[i][1])
                t += 1
                profit += cars[i][1]
            elif cars[i][1] > h[0]:
                profit -= heap.heappop(h)
                profit += cars[i][1]
                heap.heappush(h, cars[i][1])
        return profit % (10**9 + 7)
# TC O(n * log n)
# SC O(n)