def bfs(queue, grid, visited, oranges):
    maxDistance = float("-inf")
    while queue:

        item = queue.pop(0)

        x = item[0]
        y = item[1]
        d = item[2]
        if visited[x][y] == True:
            continue
        visited[x][y] = True
         
        maxDistance = max(maxDistance, d)
        
        if (x, y) in oranges:
            del oranges[(x,y)]
        
        # x + 1
        if arr(x + 1, y, grid) and visited[x+1][y] == False:
            queue.append((x+1, y, d + 1))
        # x - 1
        if arr(x - 1, y, grid) and visited[x-1][y] == False:
            queue.append((x-1, y, d + 1))
        # y + 1
        if arr(x, y + 1, grid) and visited[x][y+1] == False:
            queue.append((x, y + 1, d+1))
        # y - 1
        if arr(x, y - 1, grid) and visited[x][y-1] == False:
            queue.append((x, y-1, d + 1))
    return maxDistance


def arr(x, y, grid):
    if -1 < x < len(grid) and -1 < y < len(grid[0]):
        val = grid[x][y]
        if val == 1:
            return True
    return False;
    

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        jobs = []
        oranges = {}
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    jobs.append((x, y, 0))
                elif grid[x][y] == 1:
                    oranges[(x,y)] = True
        n = len(grid)
        m = len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]
        
        d = 0
        result = bfs(jobs, grid, visited, oranges)
        
        # ending conditions
        if oranges:
            return -1
        
        if result == float("-inf"):
            result = 0
        
        return result