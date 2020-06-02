'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

解题思路：
3指针
left指针:left的左边全为0
right指针:right的右边全为2
curr指针:当前位置i的指针

i==0时，left和curr交换，left++,curr++
i==1时，curr++
i==2时，right和curr交换，right--(curr此时不用加，因为若curr对应还为2，则还需要交换)



'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0#left的左边全为0
        right=len(nums)-1#right的右边全为2
        curr=0
        while curr<=right:
            if nums[curr]==0:
                #交换
                tmp=nums[left]
                nums[left]=0
                nums[curr]=tmp
                left+=1
                curr+=1
                continue
            if nums[curr]==2:
                #交换
                tmp=nums[right]
                nums[right]=2
                nums[curr]=tmp
                right-=1
                continue
            if nums[curr]==1:
                curr+=1
                continue

            




