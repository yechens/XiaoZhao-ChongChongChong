"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

解题思路：
先对数组排序，然后内部使用双指针不断查找最接近的三个数的和。
因为假定每组输入只存在唯一答案，所以不需要对结果去重。
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if len(nums) == 3: return sum(nums)

        # 先排序，内部使用双指针
        nums.sort()
        mmin = sum(nums[:3]) # 初始化
        n = len(nums)
        for i in range(n):
            j, k = i+1, n-1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if abs(tmp - target) < abs(mmin - target): # 更新最小的和
                    mmin = tmp
                if tmp == target: # 特例
                    return target
                elif tmp > target:
                    k -= 1 # 因为假定每组输入只存在唯一答案，所以不需要去重
                else:
                    j += 1
        return mmin
