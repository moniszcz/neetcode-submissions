class Solution:
    def isValid(self, s: str) -> bool:
        close_to_start_parentheses = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for c in s:
            if c in close_to_start_parentheses:
                if not stack:
                    return False
                last_char_in_stack = stack.pop(-1)
                if last_char_in_stack != close_to_start_parentheses[c]:
                    return False    
            else:
                stack.append(c)
        if stack:
            return False
        return True