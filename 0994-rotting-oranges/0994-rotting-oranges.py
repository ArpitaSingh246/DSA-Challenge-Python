class Solution(object):
    def orangesRotting(self, grid):
        
        count_fresh = 0
        queue = deque()
        minutes = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count_fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue and count_fresh > 0:
            for i in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in directions:
                    nx = x +dx
                    ny = y + dy
                    if (0<= nx < len(grid) and 0<= ny < len(grid[0]) and grid[nx][ny] == 1):
                        grid[nx][ny] = 2
                        count_fresh -= 1
                        queue.append((nx,ny))
                        
            minutes += 1
        if count_fresh == 0:
            return minutes
        return -1

