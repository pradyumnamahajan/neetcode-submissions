class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        longest_consecutive_sequence = 0
        for num in nums:
            nums_set.add(num)
        
        for num in nums:
            is_parent = (num - 1 not in nums_set)
            if is_parent:
                sequence_length = 0
                val = num
                while val in nums_set:
                    sequence_length += 1
                    val += 1
                longest_consecutive_sequence = max(longest_consecutive_sequence, sequence_length)

        return longest_consecutive_sequence


        