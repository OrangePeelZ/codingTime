from collections import deque


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        indegree = {}
        edges = {}
        if (words is None) | words == []:
            return ""
        if len(words) < 2:
            return words[0]

        for i in xrange(len(words)):
            indegree.update({l: 0 for l in words[i].split() if i not in indegree.keys()})
            edges.update({l: [] for l in words[i].split() if i not in indegree.keys()})
            if i > 0:
                self.compare(words[i-1], words[i], indegree, edges)

