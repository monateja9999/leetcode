class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","}":"{","]":"["}
        for token in s:
            if token == "(" or token == "{" or token == "[":
                stack.append(token)
            elif token in mapping:
                if not stack or stack.pop() != mapping[token]:
                    return False
        if not stack: return True