class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # findout the upper bound of the index using exponential backoff
        k = 0
        cnt = 0
        while reader.get(k) < target:
            k += 2**cnt
            cnt += 1

        start, end = 0, k

        while start + 1 < end:
            mid = start + (end-start)//2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) < target:
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end

        return -1