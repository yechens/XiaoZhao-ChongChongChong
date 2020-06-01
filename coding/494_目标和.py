"""
题目：
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例：
输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3

思路：
1）DP递归-未通过时间测试：nums和为S的方法数目=nums[:-1]和为S+nums[-1]或者S-nums[-1]的方法数目之和，以此递推，可以通过递归获得答案，虽然会超时。
"""
#递归
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.helper(nums, S)
        
    def helper(self, nums, S):
        if len(nums)==1 and nums[0]==S and nums[0]==-S:
            return 2
        elif len(nums)==1 and (nums[0]==S or nums[0]==-S):
            return 1
        elif len(nums)==1:
            return 0
        a, b = S - nums[-1], S + nums[-1]
        return self.helper(nums[:-1], a) + self.helper(nums[:-1], b)
