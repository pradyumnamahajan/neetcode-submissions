class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        max_area = -1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(area, max_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area
        
"""
1, 7, 2, 5, 4, 7, 3, 6

1, 6 -> 7 * 1 = 7
7, 6 -> 6 * 6 = 36
7, 3 -> 6 * 3 = 15
7, 7 -> 5 * 7 = 35
...
7, 2 -> 1 * 2 = 2

"""