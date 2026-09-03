class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def get_letters_frequency(text: str) -> dict:
            from collections import defaultdict
            freq = defaultdict(int)
            for el in text:
                freq[el] += 1
            return freq

        freq_s = get_letters_frequency(s)
        freq_t = get_letters_frequency(t)


        if freq_s != freq_t:
            return False
        return True       
        