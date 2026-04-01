class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        nums_heap = []

        for key, val in freq.items():
            heapq.heappush(nums_heap, (-val,key))
        
        topk = heapq.nsmallest(k, nums_heap)

        for key, val in topk:
            res.append(val)
        
        return res
