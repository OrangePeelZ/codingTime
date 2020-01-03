# binary search
# https://leetcode.com/problems/find-k-closest-elements/submissions/
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 1. OOOXXX Find first element that greater and equal than x, with index = ind
        # 2. compare (ind+1) with （ind - 1）
        # handle edge cases
        if arr is None:
            raise ValueError("Invalid Array")
        if (len(arr) == 0) | (k == 0):
            return []
        if len(arr) == 1:
            return arr

        ind, start, end = -1, 0, len(arr) - 1
        while (start + 1) < end:
            mid = start + (end - start)//2
            if arr[mid]< x:
                start = mid
            else:
                end = mid
        ind = start if arr[start] >= x else end
        return self.find_k_closest_elem(arr, k, ind, x)

    def find_k_closest_elem(self, arr, k, ind, x):
        # [2,3,4,5], k=4, x=3

        cnt = 0
        right = ind
        left = (ind - 1)
        while cnt < k:
            if right == len(arr):
                left -= 1
            elif left == -1:
                right += 1
            else:
                if (x - arr[left]) <= (arr[right] - x):
                    left -= 1
                else:
                    right += 1
            cnt +=1
            print "right:{0}, left:{1}".format(right, left)
        return arr[(left+1): right]

# A much cooler solution
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # just search for the starting point of K-length array
        # the first point that make array[start] closer to x than array[x+k]
        lo, hi = 0, len(arr)-k
        while lo<hi:
            mid = (lo + hi)//2
            if x-arr[mid]>arr[mid+k]-x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]