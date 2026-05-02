class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for ch in s:
            if ch not in d1:
                d1[ch] = 0
            else:
                d1[ch] += 1
        
        for ch in t:
            if ch not in d2:
                d2[ch] = 0
            else:
                d2[ch] += 1
        
        if len(d1.keys()) != len(d2.keys()):
            return False

        for ch, count in d1.items():
            if ch not in d2 or d2[ch] != count:
                return False
        return True