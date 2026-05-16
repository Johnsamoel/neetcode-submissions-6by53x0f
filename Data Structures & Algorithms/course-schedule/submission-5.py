class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        # build the graph and indegree
        for dest, src in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finished = 0
        while q:
            pre = q.popleft()
            finished += 1

            for nei in adj[pre]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finished == numCourses

        

