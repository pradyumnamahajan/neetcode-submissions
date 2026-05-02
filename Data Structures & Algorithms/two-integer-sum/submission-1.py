class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            num_to_search = target - num
            if num_to_search in indices:
                return [indices[num_to_search], i]
            indices[num] = i
        return []