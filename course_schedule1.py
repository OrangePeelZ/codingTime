from collections import deque


class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        course_graph = self.list_to_graph(prerequisites, numCourses)
        queue = deque()
        for i, j in course_graph.items():
            if len(j) == 0:
                queue.append(i)
                course_graph.pop(i)

        while queue:
            node = queue.popleft()
            for k, v in course_graph.items():
                if node in v:
                    v.remove(node)
                if len(v) == 0:
                    queue.append(k)
                    course_graph.pop(k)
        return True if len(course_graph) == 0 else False

    def list_to_graph(self, prerequisites, numCourses):
        # {0: {1,2,3}, 1: {}, ...}
        # if no preprequeists then fill it will {} an empty set
        course_dictionary = {i: set() for i in range(numCourses)}
        for [course, prereq] in prerequisites:
            course_dictionary.get(course).add(prereq)
        return course_dictionary
