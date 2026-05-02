class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = d.get(num, [])
            d[num].append(i)
        
        for num in nums:
            num_to_search = target - num
            if num_to_search in d:
                if num_to_search == num:
                    if len(d[num]) < 2:
                        continue
                    else:
                        return [d[num][0], d[num][1]]

                return [d[num][0], d[num_to_search][0]]
        return 