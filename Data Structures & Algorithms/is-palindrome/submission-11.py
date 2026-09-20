class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
            
        right, left = len(s) - 1, 0
        s = s.lower()

        while left < right:
            if not s[right].isalnum():
                right -= 1
            if not s[left].isalnum():
                left += 1
            if s[right].isalnum() and s[left].isalnum():
                if s[right] == s[left]:
                    left += 1
                    right -= 1
                else:
                    return False
        
        return True
        