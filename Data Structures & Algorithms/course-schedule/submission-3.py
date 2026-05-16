class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 1 or len(prerequisites) == 0:
            return True
        
        # 1 = yellow "in the current stack"
        # 2 = grey "visited and done"
        self.seen = {} # 1, 2
        adj = self.convertToAdjList(prerequisites)
        
        for u , v in prerequisites:
            if v not in self.seen:
                if self.hasCycle(v, adj):
                    return False
        
        return True

    def convertToAdjList(self, edges):
        D = defaultdict(list)
        
        for u, v in edges:
            D[v].append(u)

        return D 
    
    def hasCycle(self, vertex, adj) -> bool:
        self.seen[vertex] = 1
        isCyclic = False
        for nei in adj[vertex]:
            if nei not in self.seen:
                if self.hasCycle(nei, adj):
                    return True
            elif self.seen[nei] == 1:
                return True

        self.seen[vertex] = 2
        return isCyclic