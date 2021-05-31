'''
Seats

There is a row of seats represented by string A. Assume that it contains N seats adjacent to each other. There is a group of people who are already seated in that row randomly. i.e. some are sitting together & some are scattered.
An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
Now your target is to make the whole group sit together i.e. next to each other, without having any vacant seat between them in such a way that the total number of hops or jumps to move them should be minimum.
In one jump a person can move to the adjacent seat (if available).
NOTE: 1. Return your answer modulo 10^7 + 3.

Problem Constraints
1 <= N <= 1000000
A[i] = 'x' or '.'

Example Input
Input 1:

 A = "....x..xx...x.."
Input 2:

 A = "....xxx"


Example Output
Output 1:

 5
Output 2:

 0
'''
# get all posiitons of seated people
# the mid seated person is the person we want to aggregate everybody to since it will give us min jumps from left and right
# a person's start is given by pos[i]
# and his final seat is given by (seat no of the center person - half of total people + i which gives us total people placed)
# abs(start-end) will give the number of jumps for a person
class Solution:
    def seats(self, s):
        pos = []
        for i in range(len(s)):
            if s[i] == 'x':
                pos.append(i)
        if len(pos) == len(s) or len(pos) == 0:
            return 0
        ans = 0
        mid = len(pos)//2
        cp = pos[mid]
        for i in range(len(pos)):
            start = pos[i]
            end = cp-mid+i
            ans = ans + abs(start-end)
        return ans%(10**7 + 3)
# TC O(n)
# SC O(n)
            