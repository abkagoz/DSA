class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        
        for x, y in points:
            distance = sqrt(x ** 2 + y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1:])

        return res
        

