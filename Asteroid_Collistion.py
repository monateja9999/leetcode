class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if -asteroid == stack[-1]:
                    stack.pop()
                    break
                elif -asteroid > stack[-1]:
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroid)
        return stack