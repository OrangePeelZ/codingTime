# binary search
# https://leetcode.com/problems/find-peak-element/
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # handle edge case
        if (nums is None) | (len(nums) == 0):
            return None

        # find a element that is larger than its neighbor
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid + 1
        if (nums[start] >= nums[end]):
            return start
        if (nums[end] > nums[start]):
            return end