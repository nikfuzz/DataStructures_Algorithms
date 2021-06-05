'''
Fibonacci Number

Given a positive integer N, write a program to find the Ath Fibonacci number.
In a Fibonacci series, each term is the sum of the previous two terms and the first two terms of the series are 0 and 1. i.e. f(0) = 0 and f(1) = 1. Hence, f(2) = 1, f(3) = 2, f(4) = 3 and so on.
NOTE: 0th term is 0. 1th term is 1 and so on.

Problem Constraints
0 <= N <= 44

Example Input
Input 1:

 N = 4
Input 2:

 N = 6

Example Output
Output 1:
 3
Output 2:
 8
'''
# store fib of calculated values in an array called dp
# check the arr if you already have the val you need to avoid recomputation
def fibonacci(n, dp):
    if n <= 0:
        return 0
    if dp[n]:
        return dp[n]
    dp[n] = fibonacci(n-1, dp) + fibonacci(n-2, dp)
    return dp[n]


def main():
    n = int(input())
    dp = [None]*(n+1)
    dp[0] = 0
    if n > 0:
        dp[1] = 1
    print(fibonacci(n, dp))
    return 

if __name__ == '__main__':
    main()

# TC O(n)
# SC O(n)