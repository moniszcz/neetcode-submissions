class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        split_string = s.split(" ")
        string_without_whitelines = "".join(split_string)
        alphanum_chars = ''.join(filter(str.isalnum, string_without_whitelines)).lower()

        pointer_i = 0
        pointer_j = len(alphanum_chars) - 1

        stop_index = len(alphanum_chars)//2
        while pointer_i != stop_index:
            if alphanum_chars[pointer_i] != alphanum_chars[pointer_j]:
                return False
            pointer_i += 1
            pointer_j -= 1
        return True



        
        