import heapq

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        final_state = (1 << n) - 1  # Quando todos os nós forem visitados (111...1 em binário)

        # Priority queue for Dijkstra (distance, node, visited_mask)
        pq = []
        for i in range(n):
            # Inicializar a fila com cada nó como ponto de partida
            heapq.heappush(pq, (0, i, 1 << i))  # Distância inicial 0, nó atual i, máscara i visitada

        # Visited set to avoid revisiting the same state
        visited = set()

        while pq:
            dist, node, mask = heapq.heappop(pq)

            # Se este estado já foi visitado, ignore
            if (node, mask) in visited:
                continue
            visited.add((node, mask))

            # Se todos os nós foram visitados, retorne a distância
            if mask == final_state:
                return dist

            # Explorar vizinhos
            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                heapq.heappush(pq, (dist + 1, neighbor, new_mask))

        return -1  # No caso de erro (não deve acontecer, pois o grafo é sempre conectado)