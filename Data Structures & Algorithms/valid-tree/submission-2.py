class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False

        self.seen = set()
        self.adjList = self.convertToAdjList(edges)

        if self.hasAcycle(0, -1):
            return False

        return len(self.seen) == n


    def convertToAdjList(self, edges):
        D = defaultdict(list)

        for v, u in edges:
            D[v].append(u)
            D[u].append(v)

        return D

    def hasAcycle(self, v: int, p: int) -> bool:
        self.seen.add(v)

        for nei_v in self.adjList[v]:
            if nei_v not in self.seen:
                if self.hasAcycle(nei_v, v):
                    return True 
            elif nei_v in self.seen and nei_v != p:
                return True
        

        return False
                 

