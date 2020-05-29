"""
题目：
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

解题思路：
先堆排序，再去[-k]的值
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #堆排序
        def build(nums, root, end):
            while True:
                child = 2*root + 1
                if child > end:
                    break
                if (child+1)<=end and nums[child+1] > nums[child]:
                    child += 1
                if nums[root] < nums[child]:
                    nums[root], nums[child] = nums[child], nums[root]
                    root = child
                else:
                    break

        def heapsort(nums):
            n = len(nums)
            first_root = n//2 -1
            for root in range(first_root, -1, -1):
                build(nums, root, n-1)
            for end in range(n-1, 0, -1):
                nums[0], nums[end] = nums[end], nums[0]
                build(nums, 0, end-1)

        heapsort(nums)
        return nums[-k]
