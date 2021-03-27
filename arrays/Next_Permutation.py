'''
Next Permutation

Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N.
If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order.

Constraints:
1 <= N <= 5 * 105
1 <= A[i] <= 109

input: [1, 2, 3]
output: [1, 3, 2]

input: [3, 2, 1]
output: [1, 2, 3]
'''

def nextPermutation(a):
    n = len(a)

    # if len <= 2 then we either have a asc order arr or desc. either way we return reverse(a)
    if len(a) <= 2:
        return a.reverse()

    # find where the desc slope from the back ends  
    i = n-2
    while i >= 0 and a[i] >= a[i+1]:
        i -= 1
        
    # if the whole arr is in dec order 
    if i == -1:
        return a.reverse()
    
    # swap just greater number than a[i] from the dec order and reverse the right side
    for j in range(n-1, i, -1):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]
            break
    a[i+1:] = reversed(a[i+1:])
    
    return a