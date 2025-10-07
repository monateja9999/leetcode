class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            prerequisite[course].append(pre)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if prerequisite[course] == []:
                return True     
            visited.add(course)
            for each in prerequisite[course]:
                if dfs(each) == False:
                    return False
            visited.remove(course)
            prerequisite[course] = []
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
