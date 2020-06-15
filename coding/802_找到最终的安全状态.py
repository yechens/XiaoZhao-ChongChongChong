'''
题目描述：
在有向图中, 我们从某个节点和每个转向处开始, 沿着图的有向边走。 如果我们到达的节点是终点 (即它没有连出的有向边), 我们停止。

现在, 如果我们最后能走到终点，那么我们的起始节点是最终安全的。 更具体地说, 存在一个自然数 K,  无论选择从哪里开始行走, 我们走了不到 K 步后必能停止在一个终点。

哪些节点最终是安全的？ 结果返回一个有序的数组。

该有向图有 N 个节点，标签为 0, 1, ..., N-1, 其中 N 是 graph 的节点数.  图以以下的形式给出: graph[i] 是节点 j 的一个列表，满足 (i, j) 是图的一条有向边。

示例：
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]
这里是上图的示意图。



提示：

graph 节点数不超过 10000.
图的边数不会超过 32000.
每个 graph[i] 被排序为不同的整数列表， 在区间 [0, graph.length - 1] 中选取。

解题思路：
关键点：只有节点出度<=1的才可能是安全节点
比如例子加上一个节点-1 [[0],[1,2],[2,3],[5],[0],[5],[],[]],此时-1并不是安全的，因为会到闭环

1.拓扑排序

    所有边方向改变,构成反向图rgraph找到入度为0的节点，改成入度只是为了找边的头节点，不然在原图中，找到指向出度为0的点需要遍历
    比如：2->5 4->5 ，首先可以找到出度为0的点5，但是只根据原图找头节点的话需要遍历整个图，rgraph可以直接找到
    易错点：移除节点后相应的边也要移除
2.DFS
设置3中节点类型
grey=1：正在遍历的节点
white=0：没有遍历的
black=2：安全节点

重要的几点：灰遇到黑，继续遍历；灰遇到灰，截止确定存在闭环；灰遇到白递归遍历。

TODO：
DFS优化，理解再加深！


'''


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #只有节点出度《=1的才可能是！！！

        #DFS 找到不在环且能到终点的节点
        grey=1
        white=0
        black=2
        node_list=[0]*len(graph)
        res=[]
        print(len(graph))
        def dfs_helper(root):#递归
            if node_list[root]!=white:
                return node_list[root]==black
            #置灰色
            node_list[root]=grey
            for ivnode in graph[root]:
                #遇到black不一定，比如例题中的 1-》2
                if node_list[ivnode]==black:
                    continue
                else:
                    if node_list[ivnode]==grey or not dfs_helper(ivnode):
                        return False
            node_list[root]=black
            return True
        res=[]
        for root in range(len(graph)):
            if dfs_helper(root):
                res.append(root)
        return res

        #拓扑排序
        #改成入度只是为了找边的头节点
        #反向边，改成入边,找到入度为0的节点
        rgraph=[[] for _ in range(len(graph))]
        for i in range(len(graph)):
            right_now_v=i
            out_v=graph[i]
            #反向，添加节点
            for io_v in out_v:
                rgraph[io_v].append(i)
        #每次output 入度为0的节点(即原graph出度为0的节点)
        queue=[]
        for i in range(len(graph)):
            if len(graph[i])==0:
                queue.append(i)
        res=[]
        #print(queue)
        while queue:
            tmp_l=len(queue)
            for i in range(tmp_l):
                #反向图找到下一波节点
                tmp_node=queue.pop(0)
                res.append(tmp_node)
                inodelist=rgraph[tmp_node]
                for i_index in inodelist:
                    #检查是否入度为0
                    if len(graph[i_index])-1==0:
                        queue.append(i_index)
                    #移除边
                    graph[i_index].remove(tmp_node)
        return sorted(res)
