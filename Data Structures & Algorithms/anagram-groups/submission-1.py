class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            hashset = [0] * 26
            for char in word:
                hashset[ord(char) - ord('a')] += 1
            anagrams[tuple(hashset)].append(word)
        return list(anagrams.values())