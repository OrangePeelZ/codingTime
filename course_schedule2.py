from collections import deque


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = {i: 0 for i in range(numCourses)}
        course_graph = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            indegree[course] += 1
            course_graph[prereq].append(course)

        # bfs to sort courses
        ret = []
        queue = deque([i for i in indegree.keys() if indegree.get(i) == 0])
        while queue:
            node = queue.popleft()
            for i in course_graph.get(node):
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            ret.append(node)

        return ret if len(ret) == numCourses else []


