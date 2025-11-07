class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course : [] for course in range(numCourses)}
        visited = set()
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            if not graph[course]:
                return True
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}
        q = collections.deque()
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        completed = 0
        while q:
            course = q.popleft()
            completed += 1
            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return completed == numCourses