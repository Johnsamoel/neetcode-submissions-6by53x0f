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

        # build the adjList and count indegrees of each vertex
        for u, v in prerequisites:
            D[v].append(u)
            if u not in self.indegrees:
                self.indegrees[u] = 1
            else:
                self.indegrees[u] += 1

        return D

    def bfs(self, adjList, numCourses):
        q = deque()

        # add any v with indegrees = 0 or no indegrees
        for sub in range(0, numCourses):
            if sub not in self.indegrees:
                q.append(sub)

        while q:
            v = q.popleft()
            self.seen.add(v)
            self.subs.append(v)
            
            # visit its neighbours
            for nei in adjList[v]:
                if nei not in self.seen:
                    # sub the indegrees or the vertex by one
                    self.indegrees[nei] -= 1
                    if self.indegrees[nei] == 0:
                        q.append(nei)
