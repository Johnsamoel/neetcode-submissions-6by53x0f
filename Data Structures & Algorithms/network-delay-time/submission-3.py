class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [ (0, k)]
        graph = self.convertToAdjList(times)
        dis = {vertex: float('inf') for vertex in range(1, n + 1)}
        dis[k] = 0

        
        while heap:
            cur_time, u = heapq.heappop(heap)

            if cur_time > dis[u]:
                continue

            for nei , time in graph[u]:
                new_time = time + cur_time

                if new_time < dis[nei]:
                    dis[nei] = new_time
                    heapq.heappush(heap, (new_time, nei))
        min_time = 0
        for key, val in dis.items():
            if val == float('inf'):
                return -1
            min_time = max(min_time, val)

        return min_time

    def convertToAdjList(self, times: List[List[int]]):
        D = defaultdict(list)

        for src, target, cost in times:
            D[src].append((target, cost))

        return D       
                