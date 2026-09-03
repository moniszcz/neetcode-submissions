class Solution:
    def isValid(self, s: str) -> bool:
        close_to_start_parentheses = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for c in s:
            if c in close_to_start_parentheses:
                if not stack or stack[-1] != close_to_start_parentheses[c]:
                    return False
                stack.pop(-1)   
            else:
                stack.append(c)
        return False if stack else True
