class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        def is_alphanum(char: str) -> bool:
            return (ord('a') <= ord(char) <= ord('z') 
                    or ord('0') <= ord(char) <= ord('9'))
        
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            while left < right and not is_alphanum(s[left]):
                left += 1
            
            while right > left and not is_alphanum(s[right]):
                right -= 1
            
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        
        return True

        