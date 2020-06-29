'''
题目描述:
给定一组 N 人（编号为 1, 2, ..., N）， 我们想把每个人分进任意大小的两组。

每个人都可能不喜欢其他人，那么他们不应该属于同一组。

形式上，如果 dislikes[i] = [a, b]，表示不允许将编号为 a 和 b 的人归入同一组。

当可以用这种方法将每个人分进两组时，返回 true；否则返回 false。

 

示例 1：

输入：N = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]
示例 2：

输入：N = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false
示例 3：

输入：N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false
 

提示：

1 <= N <= 2000
0 <= dislikes.length <= 10000
dislikes[i].length == 2
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
对于dislikes[i] == dislikes[j] 不存在 i != j

解题思路：
考虑给一个边的两个节点上色，若存在所有边的两个顶点颜色都可以不同，则True，否则False
易忘点：可能存在多个子图
'''

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        #BFS
        #易忘点：----->可能有多个图
        #总体步骤
        #构建每个节点邻接的列表，图
        node_edge=[[] for _ in range(N+1)]
        for v1,v2 in dislikes:
            node_edge[v1].append(v2)
            node_edge[v2].append(v1)
        print(node_edge)
        #创建list保存节点的状态
        state=[0]*(N+1)
        #遍历整个图，出现一条边的两个顶点是同一颜色/状态的话return False
        def BFS(state,node_edge,use_node_count):
            if use_node_count==0:
                queue=[(1,1)]
                state[1]=1
                use_node_count+=1
            else:
                #找到另一个子图的起始点
                for i in range(1,N+1):
                    if state[i]==0:
                        queue=[(i,1)]
                        state[i]=1
                        use_node_count+=1
                        break
            while queue:
                tmpl=len(queue)
                for i_index in range(tmpl):
                    tmp_node,tmp_state=queue.pop(0)
                    #找到邻接的节点
                    for i_adj_node in node_edge[tmp_node]:
                        #print(tmp_node,i_adj_node)
                        if tmp_state==state[i_adj_node]:
                            return False,use_node_count
                        else:
                            # 防止重复遍历
                            if state[i_adj_node]==0:
                                if tmp_state==1:
                                    state[i_adj_node]=2
                                    queue.append((i_adj_node,2))
                                    use_node_count+=1
                                else:
                                    state[i_adj_node]=1
                                    queue.append((i_adj_node,1))
                                    use_node_count+=1
            return True,use_node_count
        node_count=0
        for i in range(10000):
            res,node_count=BFS(state,node_edge,node_count)
            if res==False:
                return False
            else:
                if node_count==N:
                    return True
