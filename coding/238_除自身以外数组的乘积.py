'''
题目描述：
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

 

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
 

提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

解题思路：
DP：
遍历两次：每次遍历保存该位置数左右其中一边的所有数的乘积
    从左边遍历DP[i]表示当前位置i的数，左边所有数的乘积
    从右边遍历DP[i]表示当前位置i的数，右边所有数的乘积
最后某一位置左右两边乘积的乘积，即为最后的结果


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #优化空间-两次遍历：每次遍历保存该位置数左右其中一边的所有数的乘积
        #从前往后
        output=[]
        for i_index,inum in enumerate(nums):
            if i_index==0:
                output.append(1)
            else:
                output.append(nums[i_index-1]*output[i_index-1])
        #从后往前
        tmp_product=1
        for i_index,inum in enumerate(nums):
            i_index=len(nums)-1-i_index
            if i_index==len(nums)-1:
                output[i_index]=(output[i_index])
                tmp_product=1
            else:
                output[i_index]=(output[i_index]*nums[i_index+1]*tmp_product)
                tmp_product=nums[i_index+1]*tmp_product
        return output



        #两次遍历：每次遍历保存该位置数左右其中一边的所有数的乘积
        #从前往后
        output=[]
        for i_index,inum in enumerate(nums):
            if i_index==0:
                output.append(1)
            else:
                output.append(nums[i_index-1]*output[i_index-1])
        #从后往前
        out_put_2=[]
        nums.reverse()
        for i_index,inum in enumerate(nums):
            if i_index==0:
                out_put_2.append(1)
            else:
                out_put_2.append(nums[i_index-1]*out_put_2[i_index-1])
        res=[]
        out_put_2.reverse()
        for ipre,ibh in zip(output,out_put_2):
            res.append(ipre*ibh)
        return res
