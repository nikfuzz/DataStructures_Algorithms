'''
Finish Maximum Jobs

There are N jobs to be done but you can do only one job at a time.
Given an array A denoting the start time of the jobs and an array B denoting the finish time of the jobs.
Your aim is to select jobs in such a way so that you can finish maximum number of jobs. Return the maximum number of jobs you can finish.

Problem Constraints
1 <= N <= 105
1 <= A[i] < B[i] <= 109

Example Input
Input 1:

 A = [1, 5, 7, 1]
 B = [7, 8, 8, 8]
Input 2:

 A = [3, 2, 6]
 B = [9, 8, 9]


Example Output
Output 1:

 2
Output 2:

 1
'''

class Solution:
    # sort based on end time of jobs
    # keep adding count if the next job in the sorted order starts at the end of prev job's end time
    def solve(self, a, b):
        jobs = []
        for i in range(len(a)):
            jobs.append((a[i],b[i]))
        jobs = sorted(jobs, key=lambda x: x[1])
        
        count = 0
        prev_end = None
        for i in range(len(jobs)):
            if prev_end and prev_end <= jobs[i][0]:
                count += 1
                prev_end = jobs[i][1]
            elif not prev_end:
                count += 1
                prev_end = jobs[i][1]
        return count
# TC O(n)
# SC O(n)