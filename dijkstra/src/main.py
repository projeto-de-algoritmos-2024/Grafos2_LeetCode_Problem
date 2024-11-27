import heapq

class Solution:
    def minCost(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Direções possíveis: [direita, esquerda, baixo, cima]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Mapear o valor das células para as direções esperadas
        # 1 -> direita, 2 -> esquerda, 3 -> baixo, 4 -> cima
        direction_map = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

        # Inicialização do grafo de custo
        # Usando uma fila de prioridade (min-heap)
        heap = [(0, 0, 0)]  # (custo, x, y), começa com custo 0 na célula (0, 0)
        cost = [[float('inf')] * n for _ in range(m)]  # Custo de cada célula
        cost[0][0] = 0  # O custo de começar na célula (0, 0) é 0

        while heap:
            current_cost, x, y = heapq.heappop(heap)

            # Se chegarmos à célula de destino (m-1, n-1), podemos retornar o custo
            if x == m - 1 and y == n - 1:
                return current_cost

            # Explorar as 4 direções possíveis
            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy

                # Verificar se a nova célula está dentro dos limites da grade
                if 0 <= nx < m and 0 <= ny < n:
                    # Se a direção estiver correta, o custo é 0
                    if (dx, dy) == direction_map[grid[x][y]]:
                        new_cost = current_cost
                    else:
                        # Caso contrário, é necessário modificar a direção (custo = 1)
                        new_cost = current_cost + 1

                    # Se o novo custo for melhor (menor), atualize o custo e adicione à fila
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heapq.heappush(heap, (new_cost, nx, ny))

        return -1  # Se não for possível chegar ao destino, retorna -1
