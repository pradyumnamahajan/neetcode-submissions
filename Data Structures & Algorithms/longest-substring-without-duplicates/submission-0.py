class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        max_length = 0
        l, r = 0, 0
        while r < len(s):
            char = s[r]
            count[char] += 1

            # shrink
            while count[char] > 1:
                count[s[l]] -= 1
                l += 1

            max_length = max(r-l+1, max_length)
            # grow
            r += 1
        return max_length
            
            

        
"""
abczpqrzabcd
"""