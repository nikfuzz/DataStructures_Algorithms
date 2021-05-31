'''
Distribute Candy

There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Problem Constraints
1 <= N <= 105
-109 <= A[i] <= 109

Example Input
Input 1:

 A = [1, 2]
Input 2:

 A = [1, 5, 2, 1]


Example Output
Output 1:

 3
Output 2:

 7
'''
# First go left to right and compare a[i] with a[i-1], if a[i] > then store it in an arr, left, as a[i-1] + 1. Else store 1
# Follow the same and make a right arr where you compare a[i+1], so go from right to left
# The ans arr will have res[i] = max(left[i], right[i])
class Solution:
    def candy(self, a):
        left = []
        right = [1] * len(a)
        
        for i in range(len(a)):
            if i-1 < 0:
                left.append(1)
            elif a[i-1] < a[i]:
                left.append(left[-1]+1)
            else:
                left.append(1)

        for i in range(len(a)-1, -1, -1):
            if i+1 == len(a):
                right[i] = 1
            elif a[i+1] < a[i]:
                right[i] = right[i+1]+1
            else:
                right[i] = 1
                
        for i in range(len(a)):
            right[i] = max(left[i], right[i])
            
        return sum(right)
# TC O(n)
# SC O(n)
