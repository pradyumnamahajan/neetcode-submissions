class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [0] * len(nums)
        suffix_arr = [0] * len(nums)
        answer = [0] * len(nums)

        prefix_arr[0] = 1
        for i in range(1, len(nums)):
            prefix_arr[i] = nums[i-1] * prefix_arr[i-1]

        suffix_arr[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix_arr[i] = nums[i+1] * suffix_arr[i+1]

        
        for i in range(len(nums)):
            answer[i] = prefix_arr[i] * suffix_arr[i]
        return answer

        