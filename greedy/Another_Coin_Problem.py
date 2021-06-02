'''
Another Coin Problem

The monetary system in DarkLand is really simple and systematic. The locals only use coins. The coins come in different values. The values used are:

 1, 5, 25, 125, 625, 3125, 15625, ...
Formally, for each K >= 0 there are coins worth 5K.
Given an integer A denoting the cost of an item, find and return the smallest number of coins necessary to 
pay exactly the cost of the item (assuming you have a sufficient supply of coins of each of the types you will need).

Problem Constraints
1 <= A <= 2*10^9

Example Input
Input 1:

 A = 47
Input 2:

 A = 9


Example Output
Output 1:

 7
Output 2:

 5
'''
# find the highest power of 5 we can subtract fron n
# add 1 to the ans and subtract 5^p from n
# repeat above 2 steps until n > 0
import math
class Solution:
    def solve(self, n):
        ans = 0
        while n>0:
            p = int(math.log(n,5))
            val = math.pow(5,p)
            ans += 1
            n -= val
        return ans
# TC O(n)
# SC O(1)