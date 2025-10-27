 stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                a, b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                elif token == "/":
                    if a != 0:
                        stack.append(int(b/a))
            else:
                stack.append(int(token))
        return stack[0]