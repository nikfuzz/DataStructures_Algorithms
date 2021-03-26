'''
Merge Intervals

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Constraints:
1 <= |intervals| <= 105

Input: Given intervals [1, 3], [6, 9] insert and merge [2, 5]
Output: [ [1, 5], [6, 9] ]

Input: Given intervals [1, 3], [6, 9] insert and merge [2, 6]
Output: [ [1, 9] ]

'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insert(intervals, newInterval):
    n = len(intervals)
    # if we get an interval where start < end we will convert it to start > end
    if newInterval.start > newInterval.end:
        newInterval.start, newInterval.end = newInterval.end, newInterval.start
        
    a = Interval()
    res = []
    
    # adding the incoming interval with the existing list
    for i in range(n):
        if intervals[i].start > newInterval.start:
            intervals.insert(i,newInterval)
            break
    
    if newInterval not in intervals:
        intervals.append(newInterval)
    
    ans = Interval(float('-inf'),float('-inf'))
    
    n = len(intervals)
    
    # we need to find the largest (ans.start, ans.end), i.e, min(ans.start) and max(ans.end) 
    # that can be merged with the previous interval and append it
    for i in range(n):
        a = intervals[i]
        if a.start > ans.end:
            if i != 0:
                res.append(Interval(ans.start, ans.end))
            ans.end = a.end
            ans.start = a.start
        elif a.end >= ans.end:
            ans.end = a.end
    
    # if all the intervals can be merged
    if ans.end != float('-inf') and ans not in res:
        res.append(ans)
    
    return res
                
