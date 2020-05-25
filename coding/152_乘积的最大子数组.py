'''
题目描述：
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

解题思路：
存储上一个位置的最大连乘值和最小连乘值（如果当前数是负数的化，则乘与最小连乘值，能得到当前位置的最大连乘值）
同时时刻更新以上两个值，因为题目要求连续
对每个位置值：
imax_num=max(inum*pre_min_num,max(inum,inum*pre_max_num))(包含当前位置值)
imin_num=max(inum*pre_max_num,max(inum,inum*pre_min_num))(包含当前位置值)


'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num=nums[0]
        min_num=nums[0]
        final_max_num=nums[0]
        for inum in nums[1:]:
            #根据上一个位置的最大值和最小值更新当前位置的最大值和最小值
            tmp_max_num=max(inum*min_num,max(inum,inum*max_num))
            tmp_min_num=min(inum*max_num,min(inum,inum*min_num))
            #因为是连乘的最大值，所以必须时刻更新上一个位置的max_num和min_num
            max_num=tmp_max_num
            min_num=tmp_min_num
            if max_num>final_max_num:
                final_max_num=max_num
        return final_max_num
