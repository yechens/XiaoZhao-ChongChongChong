"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

解题思路：
参考了 leetcode-imageslr 的思路：https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
（1）我们希望下一个数比当前数大，这样才满足“下一个排列”的定义。因此只需要将后面的「大数」与前面的「小数」交换，就能得到一个更大的数。比如 123456，将 5 和 6 交换就能得到一个更大的数 123465。
（2）我们还希望下一个数增加的幅度尽可能的小，这样才满足“下一个排列与当前排列紧邻“的要求。为了满足这个要求，我们需要：
1. 在尽可能靠右的低位进行交换，需要从后向前查找
2. 将一个 尽可能小的「大数」 与前面的「小数」交换。比如 123465，下一个排列应该把 5 和 4 交换而不是把 6 和 4 交换
3. 将「大数」换到前面后，需要将「大数」后面的所有数重置为升序，升序排列就是最小的排列。以 123465 为例：首先按照上一步，交换 5 和 4，得到 123564；然后需要将 5 之后的数重置为升序，得到 123546。显然 123546 比 123564 更小，123546 就是 123465 的下一个排列

"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 先判断一些处于边界的 badcase
        tmp = nums
        if len(nums) <= 1:
            return
        if sorted(nums, reverse=True) == tmp: # 已经是从大到小排序
            nums.sort()
            return 
        elif sorted(nums) == tmp: # 已经是从从小到大排序
            tmp = nums[-2]
            nums[-2] = nums[-1]
            nums[-1] = tmp
            return

        # 从后向前遍历，找到第一个降序的拐点
        n = len(nums)
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                break
        k1 = i-1 # 第一个拐点
        # 从后向前遍历，找到第一个大于 num[k] 的数，一定是大于 nums[k] 的数中最小的哪个那个数
        for i in range(n-1, k1, -1):
            if nums[i] > nums[k1]:
                break
        k2 = i
        nums[k1], nums[k2] = nums[k2], nums[k1]
        # 这种写法不属于原地修改
        # nums = nums[:k1+1] + sorted(nums[k1+1:])
        tmp = sorted(nums[k1+1:])
        # 以下属于原地修改
        for i in range(k1+1, n):
            nums[i] = tmp[i - k1 -1]
        return 
