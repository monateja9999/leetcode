class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite = {i : [ ] for i in range(num_courses)}
        visited = set()

        for course, prereq in prerequisites:
            prerequisite[course].append(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            if prerequisite[course] == []:
                return True
            
            visited.add(course)

            for pre in prerequisite[course]:
                if dfs(pre) == False:
                    return False
            
            visited.remove(course)
            prerequisite[course] = []
        
        for course in prerequisite:
            if course not in visited:
                if dfs(course) == False:
                    return False
        return True