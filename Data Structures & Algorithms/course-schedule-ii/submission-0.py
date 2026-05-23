class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.seen = set()
        self.subs = []
        adjList = self.convertToAdjList(prerequisites)
        self.bfs(adjList, numCourses)

        
        if len(self.seen) != numCourses:
            return []
        else:
            return self.subs

    def convertToAdjList(self, prerequisites):
        D = defaultdict(list)
        self.indegrees = {}

        for u, v in prerequisites:
            D[v].append(u)
            if u not in self.indegrees:
                self.indegrees[u] = 1
            else:
                self.indegrees[u] += 1

        return D

    def bfs(self, adjList, numCourses):
        q = deque()

        # add any v with indegrees = 0
        for sub in range(0, numCourses):
            if sub not in self.indegrees:
                q.append(sub)

        while q:
            print(q)
            v = q.popleft()
            self.seen.add(v)
            self.subs.append(v)
            numCourses -= 1
            # visit its neighbours
            for nei in adjList[v]:
                if nei not in self.seen:
                    self.indegrees[nei] -= 1
                    if self.indegrees[nei] == 0:
                        q.append(nei)
