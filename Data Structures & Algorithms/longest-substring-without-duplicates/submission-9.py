class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        letters_set = set()
        max_l = 0

        while right <= len(s) - 1:
            if s[right] in letters_set:
                while s[left] != s[right]:
                    letters_set.remove(s[left])
                    left += 1
                letters_set.remove(s[left])
                left += 1
            letters_set.add(s[right])
            max_l = max(len(letters_set), max_l)
            right += 1

        return max_l
                        