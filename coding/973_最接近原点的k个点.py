"""
题目：
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。

示例：
输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）

思路：
按照point[0]**2 + point[1]**2的大小进行排序，选取前k个元素
"""
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = sorted(points, key = lambda x: sqrt(x[0]**2 + x[1]**2))
        return points[:K]
