class Solution: 
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]: 
        class UnionFind: 
            def __init__(self, n): 
                self.parent = list(range(n)) 
                self.rank = [0] * n 
 
            def find(self, x): 
                if self.parent[x] != x: 
                    self.parent[x] = self.find(self.parent[x])   
                return self.parent[x] 
 
            def union(self, x, y): 
                rootX = self.find(x) 
                rootY = self.find(y) 
                if rootX != rootY: 
                    if self.rank[rootX] > self.rank[rootY]: 
                        self.parent[rootY] = rootX 
                    elif self.rank[rootX] < self.rank[rootY]: 
                        self.parent[rootX] = rootY 
                    else: 
                        self.parent[rootY] = rootX 
                        self.rank[rootX] += 1 
                    return True 
                return False 
 
        indexed_edges = [(a, b, weight, idx) for idx, (a, b, weight) in enumerate(edges)] 
        indexed_edges.sort(key=lambda x: x[2])  
 
        # Função Kruskal 
        def kruskal(edges, n, exclude=-1, include=-1): 
            uf = UnionFind(n) 
            mst_weight = 0 
            edge_count = 0 
 
            if include != -1: 
                a, b, weight, _ = indexed_edges[include] 
                if uf.union(a, b): 
                    mst_weight += weight 
                    edge_count += 1 
 
            for i, (a, b, weight, idx) in enumerate(edges): 
                if i == exclude: 
                    continue 
                if uf.union(a, b): 
                    mst_weight += weight 
                    edge_count += 1 
                    if edge_count == n - 1: 
                        break 
 
            return mst_weight if edge_count == n - 1 else float('inf') 
 
        base_weight = kruskal(indexed_edges, n) 
 
        critical = [] 
        pseudo_critical = [] 
 
        for i, (a, b, weight, idx) in enumerate(indexed_edges): 
            if kruskal(indexed_edges, n, exclude=i) > base_weight: 
                critical.append(idx) 
            elif kruskal(indexed_edges, n, include=i) == base_weight: 
                pseudo_critical.append(idx) 
 
        return [critical, pseudo_critical]