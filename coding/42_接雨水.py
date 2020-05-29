"""
题目：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

思路：
维持一个递减栈，用来做左边界，当遇到超过栈顶的元素时，即为右边界，此时弹出栈顶作为底部，取栈顶作为左边界，将容量添加到答案中
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)
        stk = []
        for current in range(size):
            while stk and height[current] > height[stk[-1]]:
                buttom = stk.pop()
                if stk:
                    distance = current - stk[-1] - 1
                    h = min(height[current], height[stk[-1]]) - height[buttom]
                    ans += h * distance
            stk.append(current)
        return ans
