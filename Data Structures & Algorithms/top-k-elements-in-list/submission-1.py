class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = defaultdict(int)
        for val in nums:
            freq_arr[val] += 1

        min_heap = []

        for val, freq in freq_arr.items():
            heapq.heappush(min_heap, (freq, val,))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        answer = []
        for _ in range(k):
            answer.append(heapq.heappop(min_heap)[1])

        return answer