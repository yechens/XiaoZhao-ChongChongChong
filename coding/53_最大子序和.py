"""
题目描述：
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例：
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

解题思路：
计算“到”每个位置时的连续和的最大值，最后取所有位置的最大值，即为结果
符号表示：
   - max_num_list(type:list)表示“到”该位置的连续和的最大值
   - inum表示当前位置的num的数值
转移方程：max_num_list[i]=max(max_num_list[i-1]+inum,inum)
      
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp
        max_num_list=[nums[0]]
        rn_maxnum=nums[0]
        for iindex,inum in enumerate(nums[1:]):
            max_num_list.append(max(inum,inum+max_num_list[iindex]))
        return max(max_num_list)
        
        #1st stage
        presum=nums[0]
        res=nums[0]
        for inum in nums[1:]:
            if presum<0:
                presum=inum
            else:
                presum+=inum
            res=max(presum,res)
        return res
