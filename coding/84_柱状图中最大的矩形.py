'''
题目描述:
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 



以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 



图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10

解题思路：

使用递增栈（入栈元素为位置序号i,新入栈元素大于栈顶则直接入栈位置值，小于则pop，并求pop出的位置的s，直到最后新入栈元素能够入栈）

对每个位置i,求当前位置左边第一个小于位置i高度的位置left,求当前位置右边第一个小于位置i高度的位置right,
以该位置为围成矩形的柱子中，高度最小柱子的面积si=(right-left-1)*nums[i]
最大面积为所有si的最大值



'''


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #递增栈
        stack=[]
        heights=[0]+heights+[0]
        res=0
        for i in range(len(heights)):
            #找到左边小于当前位置的位置，和右边小于当前位置的位置
            while stack and heights[i]<heights[stack[-1]]:
                tmpi=stack.pop()
                res=max(res,(i-stack[-1]-1)*heights[tmpi])
            stack.append(i)
        return res

        #dp===>超时
        if not heights:return 0
        min_height_list=[]
        max_area=[]
        for inum in heights:
            if not max_area and not min_height_list:
                min_height_list.append(inum)
                max_area.append(inum)
            else:
                tmp_max_height=inum
                min_height_list.append(inum)
                for i_index,i_min_height_list in enumerate(min_height_list):
                    #当前位置（最右边位置）不用比较
                    if i_index==0:
                        continue
                    #更新从右往左，inum位置到起始位置的最小高度
                    #从右往左
                    new_index=len(min_height_list)-1-i_index
                    
                    min_height_list[new_index]=min(min_height_list[new_index],\
                    min_height_list[new_index+1])
                    #更新最大面积
                    tmp_max_height=\
                    max(tmp_max_height,(i_index+1)*min_height_list[new_index])
                max_area.append(tmp_max_height)
        return max(max_area)

