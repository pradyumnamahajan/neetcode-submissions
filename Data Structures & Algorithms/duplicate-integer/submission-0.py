class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for key, value in d.items():
            if value > 1:
                return True
        
        return False