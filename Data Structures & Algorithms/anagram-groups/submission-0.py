class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = {}
        for string in strs:
            sorted_letters = str(sorted(string))
            if sorted_letters in letters_to_words:
                letters_to_words[sorted_letters].append(string)
            else:
                letters_to_words[sorted_letters] = [string]
        return letters_to_words.values()
        