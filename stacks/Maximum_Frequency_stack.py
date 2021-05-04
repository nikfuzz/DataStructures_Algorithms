'''
Maximum Frequency stack

You are given a matrix A which represent operations of size N x 2. Assume initially you have a stack-like data structure you have to perform operations on it.
Operations are of two types:
1 x: push an integer x onto the stack and return -1
2 0: remove and return the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the top of the stack is removed and returned.
A[i][0] describes the type of operation to be performed. A[i][1] describe the element x or 0 corresponding to the operation performed.

Problem Constraints
1 <= N <= 100000
1 <= A[i][0] <= 2
0 <= A[i][1] <= 109

Example Input
Input 1:
A = [
            [1, 5]
            [1, 7]
            [1, 5]
            [1, 7]
            [1, 4]
            [1, 5]
            [2, 0]
            [2, 0]
            [2, 0]
            [2, 0]  ]

Input 2:
 A =  [   
        [1, 5]
        [2 0]
        [1 4]   ]


Example Output
Output 1:
 [-1, -1, -1, -1, -1, -1, 5, 7, 5, 4]

Output 2:
 [-1, 5, -1]
'''
# we need two hashmaps
# map1 => element -> frquency
# map2 => frequency -> elements stack
# we will store the max frequncy of any element till i in max_freq
# when a pop op is called then we find the max_freq index in map2 and return the last element of the stack
from collections import deque

class Solution:
    def solve(self, a):
        map = {}
        freq_stack = {}
        
        res = []
        
        max_freq = 0
        
        for i in range(len(a)):
            stack = deque()
            if a[i][0] == 1:
                if a[i][1] not in map:
                    map[a[i][1]] = 1
                else:
                    map[a[i][1]] += 1
                max_freq = max(map[a[i][1]],max_freq)
                if map[a[i][1]] not in freq_stack:
                    stack.append(a[i][1])
                    freq_stack[map[a[i][1]]] = stack
                else:
                    freq_stack[map[a[i][1]]].append(a[i][1])
                res.append(-1)
            elif a[i][0] == 2:
                if freq_stack:
                    val = freq_stack[max_freq][-1]
                    freq_stack[max_freq].pop()
                    map[val] -= 1
                    res.append(val)
                    if not freq_stack[max_freq]:
                        max_freq -= 1
                else:
                    res.append(-1)
        return res
# TC O(n)
# SC O(n^2)