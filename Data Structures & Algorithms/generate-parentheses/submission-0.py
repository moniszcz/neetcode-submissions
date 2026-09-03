class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def generate(open_num = 0, close_num = 0):
            if close_num == open_num == n:
                result.append("".join(stack))
                return

            if open_num < n:
                stack.append("(")
                generate(open_num + 1, close_num)
                stack.pop()
            if close_num < open_num:
                stack.append(")")
                generate(open_num, close_num + 1)
                stack.pop()

        generate(0, 0)
        return result