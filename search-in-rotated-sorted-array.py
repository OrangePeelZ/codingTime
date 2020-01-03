# binary search
# https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # handle edge cases
        if (nums is None) | (len(nums) == 0):
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[0]:
                if (target < nums[0]) | (target > nums[mid]):
                    start = mid
                else:
                    end = mid
            else:
                if (target > nums[mid]) & (target < nums[0]):
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        else:
            return -1




