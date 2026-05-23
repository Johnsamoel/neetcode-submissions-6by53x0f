class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.seen = set()
        self.components = 0

        adj = self.convertToAdjList(edges, n)

        for v in range(n):
            if v not in self.seen:
                self.components += 1
                self.dfs(adj, v)

        return self.components

    def convertToAdjList(self, edges, n):
        D = defaultdict(list)

        for u, v in edges:
            D[v].append(u)
            D[u].append(v)

        return D 

    def dfs(self, adj, v):
        self.seen.add(v)

        for u in adj[v]:
            if u not in self.seen:
                self.dfs(adj, u)