'''
Coin Sum Infinite

You are given a set of coins A. In how many ways can you make sum B assuming you have infinite amount of each coin in the set.
NOTE:
Coins in set A will be unique. Expected space complexity of this problem is O(B).
The answer can overflow. So, return the answer % (106 + 7).

Problem Constraints
1 <= A <= 500
1 <= A[i] <= 1000
1 <= B <= 50000

Example Input
Input 1:

 A = [1, 2, 3]
 B = 4
Input 2:

 A = [10]
 B = 10


Example Output
Output 1:

 4
Output 2:

 1
'''
# since order does not matter we will pick each coin and check no of ways to make n with it
# make an arr of b+1 length which will store number of ways to make dp[i] with each coin
# add no of ways to make (value-coin) for each value from a[i] to n
# dp[b] will give the final answer
class Solution:
    def coinchange2(self, a, b):
        dp = [0 for j in range(b+1)]
        dp[0] = 1
        for i in range(len(a)):
            for j in range(a[i],b+1):
                dp[j] += dp[j-a[i]]
        return dp[-1]%(10**6 +7)
# TC O(b*n), n is the length of a
# SC O(b)