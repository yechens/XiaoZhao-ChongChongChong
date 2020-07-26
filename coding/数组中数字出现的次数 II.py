'''
题目描述:
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1

解题思路：
根据（二进制）位的和判断

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #判断位的状态，是不是3的倍数
        bit_num=[0]*31
        for inum in nums:
            index=0
            while inum:#本质上是转为二进制
                if inum%2:bit_num[index]+=1
                inum//=2
                index+=1
        fin_bit_num=[]
        res=0
        index=0
        for ibit_num in bit_num:
            #fin_bit_num.append(ibit_num%3)
            res+=(ibit_num%3)*2**index
            index+=1
        return res
