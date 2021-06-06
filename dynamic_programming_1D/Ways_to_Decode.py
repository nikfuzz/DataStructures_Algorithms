'''
Ways to Decode

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message denoted by string A containing digits, determine the total number of ways to decode it modulo 10^9 + 7.

Problem Constraints
1 <= length(A) <= 10^5

Example Input
Input 1:

 A = "12"
Input 2:

 A = "8"


Example Output
Output 1:

 2
Output 2:

 1
'''
# make 4 cases based on i-1th digit and ith digit and store it in an arr, dp:
# 1. i-1 == 0 and i == 0: in this case at our curr index ans = 0 
# 2. i-1 != 0 and i == 0: in this case only int(s[i-1]+s[i]) will contribute to the ans else 0
# 3. i-1 == 0 and i != 0: in this case we can only append ith digit char
# 4. i-1 != 0 and i != 0: in this case we take the previous dp[i-1]'s value. If int(s[i-1]+s[i]) <= 26 
# then we add dp[i-2]'s val
class Solution:
    def numDecodings(self, s):
        dp = [None]*len(s)
        dp[0] = 1 if s[0] != '0' else 0
        for i in range(1,len(s)):
            if s[i-1] == '0' and s[i] == '0':
                dp[i] = 0
            elif s[i-1] != '0' and s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2] if i>=2 else 1
                else:
                    dp[i] = 0
            elif s[i-1] == '0' and s[i] != '0':
                dp[i] = dp[i-1]
            else:
                if int(s[i-1]+s[i]) <= 26:
                    dp[i] = dp[i-1] + (dp[i-2] if i>=2 else 1)
                else:
                    dp[i] = dp[i-1]
        return dp[-1] % (10**9 + 7)
# TC O(n)
# SC O(n)