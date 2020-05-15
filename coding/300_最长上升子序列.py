  
"""
题目描述:
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
。
解题思路：
方法一：原始DP-->O(n*n)
    总体思路：求到每个位置时，最长子序列的长度。最终，最长子序列的长度等于整个数组中每个位置最长子序列长度的最大值。
    符号表示：dp：每个位置的最长子序列长度的list；nums表示数组;idp_num表示dp中位置i的数值;i_rn表示当前位置。
    转移方程：dp[i_rn]=max([dp[i]+1 if nums[i]<nums[i_rn] else 1 for i in len(dp[:i_rn-1])]),即求位置i的最长子序列时，通过比较当前位置和nums之前位置值的数值大小，获得当前位置所有可能的最长序列长度，最后取最大值。
方法二：DP+二分法             
    总体思路：使用新的数组tail，tail位置i的值表示i+1长度的子序列中最大数的最小值。
    每次更新不同长度子序列中最大数的最小值，最终tail的长度即为最长子序列的长度           
    详细解析参考链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/


    
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp+二分 O(nlogn)
        if not len(nums):return 0
        pernum_count=[1]
        tail=[]
        #保存能够构成不同长度子序列的最小的序列最大值
        tail.append(nums[0])
        #二分法查找
        def get_right_pos(inum,nums,i_from,t_to):
            start=i_from
            end=t_to
            while end-start>1:
                mid=(start+end)//2
                if nums[mid]>=inum:
                    end=mid
                if nums[mid]<inum:
                    start=mid
            #易错点：end和start差值为1时不能保证nums[start]<inum
            if nums[start]>=inum:
                return start
            return end
        for inum in (nums[1:]):
            if inum>tail[-1]:
                tail.append(inum)
            else: 
                if inum==tail[-1]:
                    continue
                #二分法查找第一个大于等于inum的值
                imax_index=get_right_pos(inum,tail,0,len(tail)-1)
                if tail[imax_index]>inum:
                    tail[imax_index]=inum
        return len(tail)


        #dp O(n*n)
        if not len(nums):return 0
        pernum_count=[1]
        for i_index,inum in enumerate(nums[1:]):
            i_index+=1
            perinum_max_count=1
            for s_index,s_inum in enumerate(nums[:i_index]):
                if inum>s_inum and pernum_count[s_index]+1>perinum_max_count:
                    perinum_max_count=pernum_count[s_index]+1
            pernum_count.append(perinum_max_count)
        return max(pernum_count)
