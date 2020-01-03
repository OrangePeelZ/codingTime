from collections import deque
import numpy as np

class Solution(object):
    
   
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == [] or grid is None:
            return 0
        
        length,width = np.shape(grid)
        
        count = 0
        visited = set()
        for l in range(length):
            for w in range(width):
                if (l,w) in visited:
                    continue
                if grid[l][w] == "0":
                    continue
                else:
                    count += 1
                    visited = self.update_visited(grid, l, w, visited)
        return count
    
    def update_visited(self, grid, l, w, visited):
        queue = deque()
        queue.append((l,w))
        while queue:
            node = queue.popleft()
            visited.add(node)
            (current_l, current_w) = node 
            # check (x +- 1, y) and (x, y+-1)
            for i in [(current_l+1, current_w),(current_l-1, current_w),(current_l, current_w+1),(current_l, current_w-1)]:
                if (not self.checkInVisited(i, visited)) & self.checkInGrid(i,grid):
                    if grid[i[0]][i[1]] == "1":
                        queue.append(i)
                        
        return visited
    
    def checkInVisited(self, coordinates, visited):
        return coordinates in visited
    
    def checkInGrid(self, coordinates, grid):
        length,width = np.shape(grid)
        return (coordinates[0] < length) & (coordinates[0] >=0) & (coordinates[1]< width) & (coordinates[1] >= 0)