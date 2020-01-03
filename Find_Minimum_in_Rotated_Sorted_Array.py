# binary search
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the first element that smaller than nums[(len(nums)-1)]
        # handle edge case
        if (nums is None) | (len(nums) == 0):
            raise ValueError("Invalid Array!")

        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] > nums[(len(nums)-1)]:
                start = mid
            else:
                end = mid
        return nums[start] if nums[start] < nums[(len(nums)-1)] else nums[end]

    # if there are duplilcated elements, it wont gurantee to solve in logN time