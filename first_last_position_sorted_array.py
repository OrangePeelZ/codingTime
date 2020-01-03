# Binary Seach
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# search it separately
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if (nums is None) | (len(nums) == 0):
            return [-1,-1]

        # search for the first target
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            low_bound_index = start
        elif nums[end] == target:
            low_bound_index = end
        else:
            low_bound_index = -1

        # search for the last target
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            upper_bound_index = end
        elif nums[start] == target:
            upper_bound_index = start
        else:
            upper_bound_index = -1

        return [low_bound_index, upper_bound_index]

# binary search them together

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if (nums is None) | (len(nums) == 0):
            return [-1, -1]

        # search for the first target
        find_one, start, end = -1, 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end-start)//2
            if nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                find_one = mid



        if nums[start] == target:
            low_bound_index = start
        elif nums[end] == target:
            low_bound_index = end
        else:
            low_bound_index = -1
