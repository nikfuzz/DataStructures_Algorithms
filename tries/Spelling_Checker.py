'''
Spelling Checker

Given an array of words A (dictionary) and another array B (which contain some words).
You have to return the binary array (of length |B|) as the answer where 1 denotes that the word is present in the dictionary and 0 denotes it is not present.
Formally, for each word in B, you need to return 1 if it is present in Dictionary and 0 if it is not.
Such problems can be seen in real life when we work on any online editor (like Google Documnet), if the word is not valid it is underlined by a red line.
NOTE: Try to do this in O(n) time complexity.

Problem Constraints
1 <= |A| <= 1000
1 <= sum of all strings in A <= 50000
1 <= |B| <= 1000

Example Input
Input 1:

A = [ "hat", "cat", "rat" ]
B = [ "cat", "ball" ]
Input 2:

A = [ "tape", "bcci" ]
B = [ "table", "cci" ]


Example Output
Output 1:

[1, 0]
Output 2:

[0, 0]
'''
# properties of trie
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end = False
# operations performed on trie
class Trie:
    def __init__(self):
        self.root = TrieNode('*')
        
    def add_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.is_end = True
            
    def search_word(self, word):
        if word == '':
            return 1
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return 0
            curr = curr.children[letter]
        if curr.is_end:
            return 1
        else:
            return 0

# Add all the words in a trie
# Search the words and return 1 only if all letters in arr b[i] are traversed and curr.is_end is true
class Solution:
    def solve(self, a, b):
        trie = Trie()
        for i in a:
            trie.add_word(i)
        res = []
        for i in b:
            res.append(trie.search_word(i))
        return res
# TC O(n + m), m is the length of arr b and n is the length of arr a
# SC O(k*m), k is the longest possible word, if we consider english words only then k is constant
        
