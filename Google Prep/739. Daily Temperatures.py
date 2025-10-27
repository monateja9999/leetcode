class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for idx, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                req = stack.pop()
                ans[req] = idx - req
            stack.append(idx)
        return ans