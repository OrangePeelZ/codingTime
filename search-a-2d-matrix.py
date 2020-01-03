# binary search
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # first find in which row logM
        # then find in which col logN
        # handle edge cases
        if (not matrix) | (len(matrix) == 0) | (len(matrix[0]) == 0):
            return False

        first_col = [i[0] for i in matrix]
        target_row = self.last_smaller_target_index(first_col, target)
        if target_row == -1:
            return False

        target_col = self.last_smaller_target_index(matrix[target_row], target)
        if target_col == -1:
            return False

        if matrix[target_row][target_col] == target:
            return True

        if (target_col +1) < len(matrix[0]):
            return True if matrix[target_row][target_col + 1] == target else False

    def last_smaller_target_index(self, arr, target):
        start, end = 0, len(arr) - 1
        while start + 1 < end:
            mid = start + (end-start)/2
            if arr[mid] > target:
                end = mid
            else:
                start = mid
        if arr[end] <= target:
            return end
        if arr[start] <= target:
            return start
        return -1




