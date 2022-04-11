class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        res = [[0]*n for i in range(m)]
        
        def getSingleListVal(r, c):
            return (r*n + c)
        
        def getMatrixVal(val):
            return (val // n, val % n)
        
        for r in range(m):
            for c in range(n):
                listVal = getSingleListVal(r, c) + k
                listVal = listVal % (m*n)
                new_r, new_c = getMatrixVal(listVal)
                res[new_r][new_c] = grid[r][c]
        
        return res
            
# time O(n*m)
# space O(n*m) and O(1) aux space
