class Solution(object):
    import numpy as np
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xl = []
        yl = []
        while (x > 0):
            x1.append(x%2)
            x = x/2
        while (y > 0):
            y1.append(y%2)
            y = y/2
        base_x = [0]*max(len(x1, y1))
        base_y = [0]*max(len(x1, y1))
        base_x[-len(xl):] = xl
        base_y[-len(yl):] = yl
        return np.sum(np.abs(np.array(base_x) - np.array(base_y)))



