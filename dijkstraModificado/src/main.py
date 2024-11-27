import heapq 
 
class Solution: 
    def findCheapestPrice(self, n: int, flights: [[int]], src: int, dst: int, k: int) -> int: 
        # Construir o grafo de voos 
        graph = {i: [] for i in range(n)} 
        for u, v, price in flights: 
            graph[u].append((v, price)) 
         
        # Fila de prioridade (custo acumulado, cidade atual, número de escalas) 
        pq = [(0, src, 0)]  # Começa com custo 0, cidade src e 0 escalas 
        # dp[cidade][escala] = custo mínimo para chegar à cidade com até 'escala' escalas 
        dp = [[float('inf')] * (k + 2) for _ in range(n)]  # k+2 porque queremos até k escalas + 1 
        dp[src][0] = 0 
         
        # Algoritmo de Dijkstra modificado 
        while pq: 
            cost, u, stops = heapq.heappop(pq) 
             
            # Se já ultrapassamos o número máximo de escalas, não podemos continuar 
            if stops > k: 
                continue 
             
            # Explorar todos os voos a partir de u 
            for v, price in graph[u]: 
                new_cost = cost + price 
                if new_cost < dp[v][stops + 1]:  # Se encontramos um caminho mais barato para v 
                    dp[v][stops + 1] = new_cost 
                    heapq.heappush(pq, (new_cost, v, stops + 1)) 
         
        # Encontrar o custo mínimo para chegar em dst com no máximo k escalas 
        answer = min(dp[dst][:k+2]) 
         
        # Se o custo mínimo ainda for infinito, significa que não há caminho possível 
        return answer if answer != float('inf') else -1