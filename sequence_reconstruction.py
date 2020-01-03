from collections import deque


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """


        if org is None:
            return False

        if (org == []) and (reduce(lambda x, y: x+y, seqs, []) == []):
            return True

        if (len(org) > 0) and (len(reduce(lambda x, y: x+y, seqs, [])) == 0):
            return False

        for i in reduce(lambda x, y: x+y, seqs, []):
            if i not in org:
                return False

        if reduce(lambda x, y: max(x, len(y)), seqs, 0) > len(org):
            return False

        indegree = {i: 0 for i in org}
        edges = {i: [] for i in org}

        self.sequence_to_indegree(seqs, indegree)
        self.sequence_to_edges(seqs, edges)

        queue = deque([i for i, j in indegree.items() if j == 0])
        ret = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            for i in edges[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            ret.append(node)

        return True if ret == org else False


    def sequence_to_indegree(self, seqs, indegree):
        # [[1,2,3],[3,4],[2,4]] ---> {1:0, 2:1, 3:1, 4:2}
        for seq in seqs:
            if len(seq) < 2:
                continue
            for i in range(1, len(seq)):
                indegree[seq[i]] += 1

    def sequence_to_edges(self, seqs, sequence_to_edges):
        # [[1,2,3],[3,4],[2,4]] ---> {1:[2], 2:[3,4], 3:[4], 4:[]}
        for seq in seqs:
            if len(seq) < 2:
                continue
            for i in range(0, (len(seq) - 1)):
                sequence_to_edges[seq[i]].append(seq[i+1])



from collections import defaultdict


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # handle edge cases
        # [1] [[]]
        # [1], [[1,1]]

        # [1,2]
        # [[1,2],[2,1]]

        # [1,2,3]
        # [[1,2],[1,3],[2,3]]

        adjacent = defaultdict(list)
        incoming_nodes = defaultdict(int)
        nodes = set()
        # just traverse once
        for arr in seqs:
            nodes.update(set(arr))
            for i in xrange(len(arr)):
                if i == 0:
                    # make sure this element in the incoming nodes, otherwise it needs to initiate separately
                    incoming_nodes[arr[i]] += 0

                if i < len(arr) - 1:
                    adjacent[arr[i]].append(arr[i + 1])
                    incoming_nodes[arr[i + 1]] += 1
        cur = [k for k in incoming_nodes if incoming_nodes[k] == 0] # initiate the queue
        res = []
        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            for node in adjacent[cur_node]:
                incoming_nodes[node] -= 1
                if incoming_nodes[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        return len(res) == len(nodes) and res == org




