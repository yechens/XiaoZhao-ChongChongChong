'''
题目描述:
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路:
快排+两个字符串大小的比较 int(str(x)+str(y))和int(str(y)+str(x))


'''



class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def compare(x,y):
            if int(str(x)+str(y))<int(str(y)+str(x)):
                return False
            else:
                return True

        def qsorted(num,left,right):
            if left>=right:return num
            #left=0
            #right=len(num)-1
            prenum=num[left]
            num[left]=None
            #挖坑
            while left!=right:
                if num[left] is None:
                    #看右边
                    if compare(nums[right],prenum):
                        right-=1
                        continue
                    else:
                        nums[left],nums[right]=nums[right],None
                        left+=1
                        continue
                if num[right] is None:
                    #看左边
                    if compare(nums[left],prenum):
                        nums[left],nums[right]=None,nums[left]
                        right-=1
                        continue
                    else:
                        left+=1
                        continue
            num[left]=prenum
            return left,num
        def sort(nums,i,j):
            if i>=j:return nums
            mid,nums=qsorted(nums,i,j)
            nums=sort(nums,i,mid-1)
            nums=sort(nums,mid+1,j)
            return nums
        nums=sort(nums,0,len(nums)-1)
        res=''
        for inum in nums:
            res+=str(inum)
        return res
