'''
题目描述:
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

解题思路：
方法1:枚举
取数组i到j 的位置 累加 一个一个判断
方法2：前缀和
判断 presum-k是否存在于设定的字典中（不是很理解）
TODO：理解


'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #前缀和--不理解
        sum_map={0:1}
        pre_sum=0
        count=0
        for inum in nums:
            pre_sum+=inum
            if pre_sum-k in sum_map.keys():
                count+=sum_map[pre_sum-k]
            sum_map[pre_sum]=sum_map.get(pre_sum,0)+1
        return count

        #枚举------最基本的方法
        res=0
        for start in range(len(nums)):
            sums_e=0
            #end -start子数组的和
            for end in range(start,-1,-1):
                sums_e+=nums[end]
                if sums_e==k:
                    res+=1
        return res
