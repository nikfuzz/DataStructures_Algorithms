'''
Longest Balanced Substring

Given a string A made up of multiple brackets of type "[]" , "()" and "{}" find the length of the longest substring which forms a balanced string .
Conditions for a string to be balanced :
Blank string is balanced ( However blank string will not be provided as a test case ).
If B is balanced : (B) , [B] and {B} are also balanced.
If B1 and B2 are balanced then B1B2 i.e the string formed by concatenating B1 and B2 is also balanced.

Problem Constraints
0 <= |A| <= 10^6

Example Input
Input 1:

 A = "[()]"
Input 2:

 A = "[(])"


Example Output
Output 1:

 4
Output 2:

 0
'''
# make a dp arr which will tell us the max balanced substring uptill i
# if s[i] == ')' and s[i-1] == '(' then that means dp[i] will have ans till dp[i-2] plus 2 chars for i-1 and i
# if s[i-1] and s[i] == ')' then we need to add its counter opening bracket at i-dp[i-1]-2th position and add the number of 
# balanced substrings till dp[i-1] 
# max(dp) will give the final ans
# generalize the approach for all types of brackets
class Solution:
    def LBSlength(self, s):
        if s == '':
            return 0
        dp = [0]*len(s)
        for i in range(1,len(s)):
            if (s[i] == ')' and s[i-1] == '(') or (s[i] == ']' and s[i-1] == '[') or (s[i] == '}' and s[i-1] == '{'):
                dp[i] = dp[i-2] + 2
            elif (s[i] == ')' and (s[i-1] == ')' or s[i-1] == ']' or s[i-1] == '}')):
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >=0 else 0)
                    
                    
            elif (s[i] == ']' and (s[i-1] == ')' or s[i-1] == ']' or s[i-1] == '}')):
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '[':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >=0 else 0)
                    
                    
            elif (s[i] == '}' and (s[i-1] == ')' or s[i-1] == ']' or s[i-1] == '}')):
                if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '{':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >=0 else 0)
                    
        return max(dp)
# TC O(n)
# SC O(n)