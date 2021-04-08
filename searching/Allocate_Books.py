'''
Allocate Books

Given an array of integers A of size N and an integer B.
College library has N books,the ith book has A[i] number of pages.
You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.
A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.

Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 105

Example Input
A = [12, 34, 67, 90]
B = 2

Example Output
113
'''

class Solution:
	# We need to choose max how many pages each stud reads
    # If our condition satisfies for a value m then we need to search for a val less than
    def books(self, a, b):
        if b>len(a):
            return -1
        if b == len(a):
            return max(a)
        l = max(a)
        r = sum(a)

        while l<=r:
            s = 0
            studs = 1
            m = (l+r)//2
            for i in range(len(a)):
                s += a[i]
                if s > m:
                    studs += 1
                    s = a[i]
            # this is the condition we must satisfy
            if studs<=b:
                r = m-1
            else:
                l = m+1

        return l