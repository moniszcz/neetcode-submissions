class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        result = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for i in s:
                pos = ord(i) - ord('a')
                freq[pos] += 1
            
            result[tuple(freq)].append(s)
        return list(result.values())
        
        