'''
题目描述:
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

解题思路:
构建某个位置左边及右边的乘积，3遍遍历
'''

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left=[1]*len(a)
        right=[1]*len(a)
        tmp=1
        #左边
        for i_index,i in enumerate(a):
            if i_index==0:
                continue
            left[i_index]=left[i_index-1]*a[i_index-1]
        #右边
        tmp=1
        for i_index in range(len(a)-1,-1,-1):
            if i_index==len(a)-1:
                continue
            right[i_index]=right[i_index+1]*a[i_index+1]
        res=[]
        for ileft,iright in zip(left,right):
            res.append(ileft*iright)
        return res
