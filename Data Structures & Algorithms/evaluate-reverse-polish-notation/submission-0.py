class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                token = int(stack.pop()) + int(stack.pop())
            elif token == "*":
                token = int(stack.pop()) * int(stack.pop())
            elif token == "-":
                first_digit = int(stack.pop())
                second_digit = int(stack.pop())
                token = second_digit - first_digit
            elif token == "/":
                first_digit = int(stack.pop())
                second_digit = int(stack.pop())
                token = int(second_digit / first_digit)
            stack.append(int(token))
        return stack.pop()

        