import heapq

class Solution:
    def shortestPathAllKeys(self, grid):
        m, n = len(grid), len(grid[0])
        all_keys = 0  # Máscara para todas as chaves
        start_x = start_y = 0
        
        # Inicializar as variáveis
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start_x, start_y = i, j
                elif 'a' <= grid[i][j] <= 'f':  # É uma chave
                    all_keys |= (1 << (ord(grid[i][j]) - ord('a')))

        # Fila de prioridade 
        pq = []
        heapq.heappush(pq, (0, start_x, start_y, 0))  
        visited = set()  # Evitar revisitar estados

        # Movimentos possíveis (cima, baixo, esquerda, direita)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            cost, x, y, keys = heapq.heappop(pq)

            # Se já visitamos este estado, pular
            if (x, y, keys) in visited:
                continue
            visited.add((x, y, keys))

            # Se coletamos todas as chaves, retornar o custo
            if keys == all_keys:
                return cost

            # Explorar vizinhos
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:  # Dentro dos limites
                    cell = grid[nx][ny]

                    # Se for uma parede, pular
                    if cell == '#':
                        continue

                    # Se for uma porta, verificar se temos a chave
                    if 'A' <= cell <= 'F' and not (keys & (1 << (ord(cell) - ord('A')))):
                        continue

                    # Se for uma chave, coletar atualizando a máscara
                    new_keys = keys
                    if 'a' <= cell <= 'f':
                        new_keys |= (1 << (ord(cell) - ord('a')))

                    # Adicionar o novo estado à fila
                    heapq.heappush(pq, (cost + 1, nx, ny, new_keys))

        # Se não for possível coletar todas as chaves, retornar -1
        return -1
