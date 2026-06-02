class Solution:
    def trap(self, heights: List[int]) -> int:
        prefix_max = [0] * len(heights)
        suffix_max = [0] * len(heights)

        for i in range(1, len(heights)):
            prefix_max[i] = max(prefix_max[i-1], heights[i-1])
        
        for i in range(len(heights)-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], heights[i+1])

        water = 0
        for i, height in enumerate(heights):
            wall = min(prefix_max[i], suffix_max[i])
            if wall > height:
                water += wall - height

        return water



"""
[0,2,0,3,1,0,1,3,2,1]]
[0,0,2,2,3,3,3,3,3,3]
[3,3,3,3,3,3,3,2,1,0]
[0,0,2,0,2,3,2,0,0,0]
"""

            

            


"""
0, 0
"""


