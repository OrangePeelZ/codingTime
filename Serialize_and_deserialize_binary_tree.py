# 1) be care about the corner case []
# 2) be careful about the out of boundry index when we add on it
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# be care about the corner case []
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        queue = deque([root])
        visited = [str(root.val)]
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                visited.append(str(node.left.val))
            else:
                visited.append("#")

            if node.right:
                queue.append(node.right)
                visited.append(str(node.right.val))
            else:
                visited.append("#")
        return ','.join(self.purge(visited))

    def purge(self, l):
        pointer = len(l) - 1
        while pointer >= 0:
            if l[pointer] == '#':
                pointer -= 1
            else:
                break
        return l[:(pointer + 1)]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return []
        elems = data.split(',')
        # construct the tree nodes
        # elem_list = [TreeNode(int(i)) if i != '#' else None for i in elems]

        root = TreeNode(elems[0])
        queue = deque([root])
        index = 1
        while (len(queue) > 0) & (index < len(elems)):
            node = queue.popleft()
            if elems[index] != '#':
                node.left = TreeNode(int(elems[index]))
                queue.append(node.left)
            index += 1
            if index >= len(elems):
                break

            if elems[index] != '#':
                node.right = TreeNode(int(elems[index]))
                queue.append(node.right)
            index += 1
        return root


        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))
