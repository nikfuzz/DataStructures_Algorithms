'''
Repeated Subtraction

You are given 2 numbers P and Q.
An operation on these 2 numbers is defined as follows: Take the smaller number of the 2 numbers and subtract it from the bigger number. 
Keep performing this operation till either of the following criterion is met:
Both numbers become equal.
Either of the number becomes 0.
Find the sum of the final values of P and Q.

constraints:
 0 <= P,Q <= 1e9

input: 
    P : 5 
    Q : 15

 output: 10
'''
class Solution:
    def getFinal(self, a, b):
        # safety case
        if a == 0 or b==0:
            return (a or b)
        
        # if a is div by b then after performing repeated subtraction we will get a == b
        if a%b == 0 or b%a == 0:
            if a > b:
                return 2*b
            return 2*a
        # keep subtracting until you reach 0 or a==b
        while a>0 and b>0:
            if a == b:
                return a+b
            
            elif a>b:
                a = a-b
            elif b>=a:
                b = b-a
        
        return (a or b)