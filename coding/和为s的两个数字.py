'''
题目描述:
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]

解题思路:
对撞指针
字典
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #对撞双指针
        i,j=0,len(nums)-1
        while True:
            if nums[i]+nums[j]>target:
                j-=1
            if nums[i]+nums[j]<target:
                i+=1
            if nums[i]+nums[j]==target:
                return [nums[i],nums[j]]
        #字典！！！
        mapdict={}
        for inum in nums:
            if mapdict.get(target-inum,0)==1:
                return [inum,target-inum]
            else:
                mapdict[inum]=1
