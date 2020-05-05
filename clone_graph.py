from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        root = node
        if root is None:
            return None

        nodes = self.find_all_nodes(node)
        # start copy
        mapping = {}
        # first copy all the nodes
        for node in nodes:
            mapping.update({node: Node(val=node.val, neighbors=[])})

        # then copy all the neighbors
        for node in nodes:
            neighbors = node.neighbors
            for i in neighbors:
                mapping[node].neighbors.append(mapping[i])
        return mapping[root]

    def find_all_nodes(self, node):
        queue = deque([node])
        visited = {node}

        while queue:
            new_node = queue.popleft()
            for i in new_node.neighbors:
                if i in visited:
                    continue
                visited.add(i)
                queue.append(i)

        return visited



