"""
题目：
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

思路：
为了剔除重复的元素，可以先排序，然后用双指针寻找合适的三个元素
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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
        ans = []
        for k in range(0, len(nums)-2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i, j = k+1, len(nums)-1
            while i < j:
                sum = nums[k] + nums[i] + nums[j]
                if sum < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                elif sum > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    ans.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return ans
