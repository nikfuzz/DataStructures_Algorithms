'''
Add One To Number

Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.

Constraints:
1 <= size of the array <= 1000000

input: [1, 2, 3]
output: [1, 2, 4]
'''

def plusOne(a):
    # convert list to a int and add 1
    s = "".join(str(i) for i in a)
    s = str(int(s) + 1)
    # strip all 0s from left
    s = s.lstrip("0") or '0'
    
    a = [int(x) for x in s]
    return a