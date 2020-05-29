'''
题目描述：
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

解题思路：
1.二分法（推荐）
易错点：找左边和右边的位置时，也要遍历left位置，不然无法更新start/end

2.遍历一遍
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #O(logn) 二分法========>省不少时间！！！！！！！
        if not len(nums):return[-1,-1]
        start=-1
        end=-1
        left=0
        right=len(nums)-1
        while right-left>1:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid
            if nums[mid]<target:
                left=mid
            if nums[mid]==target:
                left=mid
                right=mid
                break
        #使用left存储等于target数的位置
        if nums[right]==target:
            left=right
        else:
            if nums[left]==target:
                pass
            else:
                return[start,end]
        #寻找等于target位置的左边和右边
        #易错点：找左边和右边的位置时，也要遍历left位置，不然无法更新start/end
        for i_index in range(left+1):
            i_index=left-i_index
            if nums[i_index]==target:
                start=i_index
        for i_index in range(left,len(nums),1):
            if nums[i_index]==target:
                end=i_index
        return[start,end]
        

        #O(n)
        start=-1
        end=-1
        for i_index,inum in enumerate(nums):
            if inum==target and start==-1:
                start=i_index
            if inum==target and start!=-1:
                end=i_index
        return[start,end]
            

            
