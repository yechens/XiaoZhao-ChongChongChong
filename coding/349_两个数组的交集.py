'''
题目描述：
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]
说明:

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

解题思路:
字典存储，哈希表

'''



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_dict={}
        res=[]
        for inum1 in nums1:
            if inum1 not in num1_dict.keys():
                num1_dict[inum1]=1
        for inum2 in nums2:
            if inum2  in num1_dict.keys():
                res.append(inum2)
        return set(res)
