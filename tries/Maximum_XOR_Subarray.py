'''
Maximum XOR Subarray

Given an array A of integers of size N. Find the subarray AL, AL+1, AL+2, ... AR with 1<=L<=R<=N which has maximum XOR value.
NOTE: If there are multiple subarrays with same maximum value, return the subarray with minimum length. If length is same, return the subarray with minimum starting index.

Problem Constraints
1 <= N <= 100000
0 <= A[i] <= 109

Example Input
Input 1:

 A = [1, 4, 3]
Input 2:

 A = [8]

Example Output
Output 1:

 [2, 3]
Output 2:

 [1, 1]
'''

# Trie node properties
class TrieNode:
    def __init__(self, bit):
        self.bit = bit
        self.children = {}
# trie operations
class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    def add_num(self, num):
        curr = self.root
        for dig in num:
            if dig not in curr.children:
                curr.children[dig] = TrieNode(dig)
            curr = curr.children[dig]
    def search_num(self, num):
        curr = self.root
        xor = ''
        for dig in num:
            if dig == '0' and '1' in curr.children:
                curr = curr.children['1']
            elif dig == '1' and '0' in curr.children:
                curr = curr.children['0']
            else:
                if dig in curr.children:
                    curr = curr.children[dig]
            xor += curr.bit
        return xor

# First create a prefix xor arr
# find the maximum xor in the pref array with the help of a Trie
# prefix[r] ^ max_xor = prefix[l-1] for prefix array
# use a map to find prefix[r] ^ max_xor, this will give us l-1, which is a possible ans candidate
# choose an ans which has min len of subarray
class Solution:
    def solve(self, a):
        trie = Trie()
        pref = []
        pref.append(0)
        trie.add_num('{:032b}'.format(pref[-1]))
        max_xor = 0
        for i in range(len(a)):
            pref.append(pref[-1]^a[i])
        for i in pref:
            trie.add_num('{:032b}'.format(i))
        for i in pref:
            xor_num = trie.search_num('{:032b}'.format(i))
            max_xor = max(int(xor_num,2)^i,max_xor)
        map = {}
        ans = []
        for i in range(len(pref)):
            if pref[i]^max_xor not in map:
                map[pref[i]] = i
            elif pref[i] ^ max_xor in map:
                if (ans and (ans[1]-ans[0]) > (i - map[pref[i] ^ max_xor])) or not ans:
                    ans = [map[pref[i] ^ max_xor]+1, i]
        return ans
# TC O(N * 31) => O(N)
# SC O(N * 31) => O(N)
                
