from typing import (
    List,
)

class Solution:
    """
    @param heights: An integer array
    @return: Indexs of buildings with sea view
    """
    def find_buildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)):
            if stack:
                while stack and heights[stack[-1]] <= heights[i]:
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        return stack