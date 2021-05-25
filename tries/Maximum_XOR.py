'''
Maximum XOR

Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.

Problem Constraints
1 <= length of the array <= 100000
0 <= A[i] <= 109

Example Input
Input 1:

 A = [1, 2, 3, 4, 5]
Input 2:

 A = [5, 17, 100, 11]


Example Output
Output 1:

 7
Output 2:

 117
'''
# for properties of node
class TrieNode:
    def __init__(self, digit):
        self.bit = digit
        self.children = {}
        self.is_end = False
# for operations on the trie
class Trie:
    def __init__(self):
        self.root = TrieNode('*')
        
    def add_digit(self, num):
        curr = self.root
        for dig in num:
            if dig not in curr.children:
                curr.children[dig] = TrieNode(dig)
            curr = curr.children[dig]
        curr.is_end = True
        
    def find_max_xor(self, num):
        curr = self.root
        xor = ''
        for dig in num:
            if dig == '0' and '1' in curr.children:
                curr = curr.children['1']
            elif dig == '1' and '0' in curr.children:
                curr = curr.children['0']
            else:
                curr = curr.children[dig]
            xor += curr.bit
        return xor

# For each number traverse a branch which has maximum opp bits
# That branch will give us the number which can give maximum xor with our selected number
# Take xor with the returned number and finally return the max
class Solution:
    def solve(self, a):
        trie = Trie()
        for i in a:
            trie.add_digit('{:032b}'.format(i))
        max_xor = float('-inf')
        for i in a:
            xor_num = trie.find_max_xor('{:032b}'.format(i))
            max_xor = max(int(xor_num,2)^i,max_xor)
        return max_xor
# TC O(N * 31) => O(N)
# SC O(N * 31) => O(N)
