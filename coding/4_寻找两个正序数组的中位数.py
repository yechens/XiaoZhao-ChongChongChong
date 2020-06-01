"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5

解题思路：
若想达到 O(log(m + n)) 的时间复杂度，需要使用二分查找算法来寻找中位数。
题目要求两个正序数组的中位数，可以转换为两个数组中第 k 小的数
为了避免讨论两个数组长度之和为奇数/偶数的问题，可以设置：
k1 = (len(nums1) + len(nums2) + 1) // 2
k2 = (len(nums1) + len(nums2) + 2) // 2
最终计算 (k1 + k2) / 2. 即可

具体应用二分查找时，由于数列是有序的，其实我们完全可以一半儿一半儿的排除。假设我们要找第 k 小数，我们可以每次循环排除掉 k/2 个数。
我们分别计算两个数组的第 k//2 个位置的值（假设存在），哪个小，就表明该数组的前 k/2 个数字都不是第 k 小数字，所以可以排除；
如果某个数组长度 < k//2，该数组可以全部排除！
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        left, right = (m + n + 1) // 2, (m + n + 2) // 2
        print(left, right)

        def getKth(nums1, i, nums2, j, k):
            if i >= len(nums1): # nums1 为空
                return nums2[j + k -1]
            if j >= len(nums2): # nums2 为空
                return nums1[i + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])

            if i + k//2 - 1 < len(nums1): 
                midv1 = nums1[i + k//2 -1]
            else: # nums1 中 k//2 不存在
                midv1 = float('inf') # inf 表示 nums1 可以全部被排序

            if j + k//2 -1 < len(nums2):
                midv2 = nums2[j + k//2 -1]
            else: # nums2 中 k//2 不存在
                midv2 = float('inf')
            
            if midv1 < midv2:
                return getKth(nums1, i + k//2, nums2, j, k - k//2)
            else:
                return getKth(nums1, i, nums2, j + k//2, k - k//2)

        # 将偶数和奇数的情况合并，如果是奇数，会求两次同样的 k 
        return (getKth(nums1, 0, nums2, 0, left) + getKth(nums1, 0, nums2, 0, right)) / 2.
