'''
Solve sub-sequences and return OR

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. 
For example, the sequence {2, 3, 5} is a subsequence of {1, 2, 3, 4, 5} obtained after removal of elements {1, 4}.
Given is an array of integers A of size N. An array of size N can have (2^N - 1) number of non empty subsequences.
For the given function:
 solve (int subsequence[]) {
    int count[];    //array initialised to 0.
    for(int i = 0; i &amp;lt; subsequence.length; i++) {
        number = subsequence[i];
        for(int j = 2; j &amp;lt;= number; j++) {
            if(number % j == 0) {
                count[j]++;
                if(count[j] == subsequence.length)  return 0;
            }
        }
    }
    return 1;
}

If all the subsequences of the array A are passed in the above function. 
What will be the bitwise OR of all the returned values from the given function.

Constraints:
1 <= length of the array <= 100000
1 <= A[i] <= 109

input: [1, 2, 3]
output: 1

input: [2, 4, 6, 8]
output: 0
'''

# the function can be simplified to
# checking if gcd of the sub sequence is equal to the len of subseq or not
# can be further simplied to if the gcd of the arr is 1 or not (since gcd of one of the subs can make the whole gcd(arr) == 1)
class Solution:
    def gcd(self,x,y):
        if x == 0:
            return y
        else:
            return self.gcd(y%x, x)
    
    def solve(self, a):
        gc = 0
        for i in range(len(a)):
            gc = self.gcd(a[i], gc)
            if gc == 1:
                return 1
        
        return 0