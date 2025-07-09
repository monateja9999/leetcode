class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        check = []
        for i in range(len(position)):
            check.append([position[i], speed[i]])
        final = sorted(check, key=lambda x:x[0], reverse = True)
        stack = []
        for i in range(len(final)):
            time = (target - final[i][0]) / final[i][1]
            if not stack: 
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)