class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack.pop() if stack else ""