'''
Count of divisors

Given an array of integers A, find and return the count of divisors of each element of the array.
NOTE: Order of the resultant array should be same as the input array.

Constraints:
1 <= length of the array <= 100000
1 <= A[i] <= 106

input: [2, 3, 4, 5]
output: [2, 2, 3, 2]

input: [8, 9, 10]
output: [4, 3, 4]
'''

class Solution:
    primes = [0 for i in range(10**6+1)]
    # sieve of eratosthenes to calculate largest prime for a number
    def sieve(self):
        self.primes[1] = 1
        
        for i in range(2,10**6+1):
            if self.primes[i] == 0:
                for j in range(i,10**6+1,i):
                    self.primes[j] = i
    
    def solve(self, a):
        self.sieve()
        res = []
        # we need to find the number of times each prime factor our given number has
        for i in range(len(a)):
            n = a[i]
            ans = 1
            # this will give us the frequency of a prime factor in a given number
            while n > 1:
                count = 0
                lp = self.primes[n]
                while n%lp == 0:
                    count += 1
                    n //= lp
                
                # multiple frequency+1 of each prime factor
                ans *= (count+1)
            res.append(ans)
                
        return res