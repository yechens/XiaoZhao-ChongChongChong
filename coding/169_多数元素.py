"""
题目描述：
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3
示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2

解题思路：
用字典存储遍历过程中每个元素的次数，最后在字典找到value超过floor(len(nums)/2)
"""
class Solution:
    def majorityElement(self, nums):
        num_dict = {}
        l = len(nums)
        for n in nums:
            if n not in num_dict.keys():
                num_dict[n] = 0
            num_dict[n] += 1
        for key in num_dict.keys():
            if num_dict[key] > math.floor(l/2):
                return key
