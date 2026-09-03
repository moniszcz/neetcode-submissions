class Solution:
    #Time complexity O(m*n*log(n))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_anagrams = defaultdict(list)
        for string in strs:
            sorted_chars = str(sorted(string))
            chars_to_anagrams[sorted_chars].append(string)

        return chars_to_anagrams.values()
        