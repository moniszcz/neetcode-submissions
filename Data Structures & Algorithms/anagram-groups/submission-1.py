class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for string in strs:
            sorted_letters = str(sorted(string))
            letters_to_words[sorted_letters].append(string)

        return letters_to_words.values()
        