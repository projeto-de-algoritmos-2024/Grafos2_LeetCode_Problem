import heapq 
 
class Solution: 
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, k: int) -> int: 
        graph = {i: [] for i in range(n)} 
        for u, v, price in flights: 
            graph[u].append((v, price)) 
         
        pq = [(0, src, 0)]  
        dp = [[float('inf')] * (k + 2) for _ in range(n)]  
        dp[src][0] = 0 
         
        while pq: 
            cost, u, stops = heapq.heappop(pq) 
             
            if stops > k: 
                continue 
             
            for v, price in graph[u]: 
                new_cost = cost + price 
                if new_cost < dp[v][stops + 1]:  
                    dp[v][stops + 1] = new_cost 
                    heapq.heappush(pq, (new_cost, v, stops + 1)) 
         
        answer = min(dp[dst][:k+2]) 
         
        return answer if answer != float('inf') else -1