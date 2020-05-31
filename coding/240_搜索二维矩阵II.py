"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例:
现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。
给定 target = 20，返回 false。

解题思路：
左下角的元素是这一行中最小的元素，同时又是这一列中最大的元素。
如果 target 小于左下角元素，只可能往上一行查找；
如果 target 大于左下角元素，只可能往右一列查找
时间复杂度：O(m+n)
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 左下角的元素是这一行中最小的元素，同时又是这一列中最大的元素
        try:
            m, n = len(matrix), len(matrix[0])
        except:
            return False
        if not m or not n: return False
        i, j = m - 1, 0 # 定位行和列
        while i>=0 and j<n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False
