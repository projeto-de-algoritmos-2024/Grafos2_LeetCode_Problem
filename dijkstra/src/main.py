import heapq

class Solution:
    def minCost(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        direction_map = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        heap = [(0, 0, 0)]  
        cost = [[float('inf')] * n for _ in range(m)]  
        cost[0][0] = 0  

        while heap:
            current_cost, x, y = heapq.heappop(heap)

            if x == m - 1 and y == n - 1:
                return current_cost

            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if (dx, dy) == direction_map[grid[x][y]]:
                        new_cost = current_cost
                    else:
                        new_cost = current_cost + 1

                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))

        return -1  
