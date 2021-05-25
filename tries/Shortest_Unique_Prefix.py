'''
Shortest Unique Prefix

Given a list of N words. Find shortest unique prefix to represent each word in the list.
NOTE: Assume that no word is prefix of another. In other words, the representation is always possible

Problem Constraints
1 <= Sum of length of all words <= 106

Example Input
Input 1:

 A = ["zebra", "dog", "duck", "dove"]
Input 2:

A = ["apple", "ball", "cat"]


Example Output
Output 1:

 ["z", "dog", "du", "dov"]
Output 2:

 ["a", "b", "c"]
'''
# Trie node class which will store all properties of trie
class TriNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.words = 0
        self.is_end = False
# trie class which will run all member functions
class Trie:
    def __init__(self):
        self.root = TriNode("*")
        
    def add_word(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TriNode(letter)
            curr = curr.children[letter]
            curr.words += 1
        curr.is_end = True
        
    def getUniquePrefix(self, word):
        if word == "":
            return True
        curr = self.root
        s = ''
        for letter in word:
            curr = curr.children[letter]
            s += letter
            if curr.words == 1:
                return s
        return s
# We need to add all the words in trie
# Also, we need to mark how many words can be found from a node, at every node
# Traverse the trie and find all the words in it, stop when the words aggregator, i.e, no of words from that node is 1
# return the letters traversed, this will give us the unique prefix for a word
class Solution:
    def prefix(self, a):
        trie = Trie()
        for i in a:
            trie.add_word(i)
        res = []
        for i in a:
            res.append(trie.getUniquePrefix(i))
        return res
# TC O(N*L) , L is the length of an average word in the list
# SC O(N*M), M is the length of the longest word