class Solution(object):
    def createGrid(self,m,n):
        grid = [["#"] * n for _ in range(m)]
        r, c = 0, 0
        grid[r][c] = '.'
        while r < m - 1 or c < n - 1:
            if c < n - 1:
                c += 1
                grid[r][c] = '.'
            if r < m - 1:
                r += 1
                grid[r][c] = '.'
        return ["".join(row) for row in grid]

        