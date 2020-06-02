"""
题目：
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49

思路：
维护一个全局ans记录全局最大的值，头尾2个指针向中间移动，知道i==j。移动策略为：height较小的那个移动，因为这样才可能遇到最大值。
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i, j = 0, len(height)-1
        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans
