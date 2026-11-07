class Solution(object):
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_orange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_orange += 1
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        minutes = 0
        while queue and fresh_orange > 0:
            minutes += 1
            for i in range(len(queue)):
                r,c = queue.popleft()
                for x,y in direction:
                    nr, nc = r+x, c+y  
                    if 0 <=  nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh_orange -= 1
        if fresh_orange == 0:
            return minutes
        else:
            return -1
               

