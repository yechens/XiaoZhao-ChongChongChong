git add .
cd ..
git add .
git commit -m '0524'
git pull
git pull
git pull
git add .
git commit -m '0525'
git push
git add .
git commit -m '0525'
git push
git add .
git commit -m '0525'
git push
cd ../../gitlab/sentence-similarity/
ls
mkdir FastText
cd FastText/
ls
ls
cd ..
git add .
git commit -m 'update fasttext'
git push
git push
git add .
git commit -m 'update fasttext'
git push origin master
git add .
git push origin master
git commit -m 'update fasttext'
git push origin master
ls
cd FastText/
ls
cd ..
git add .
git commit -m 'update fasttext'
git push origin master
cd ..
git clone git@gitlab.yiwise.local:liyunliang/data_aug.git
ls
cd data_aug/
ls
ls -a
ls
git add .
git commit -m 'new readme'
git push
cd ../../github/QiuZhao-ChongChongChong/
git pull
git pull origin master
git pull origin master
git add .
git commit -m '0526'
git push origin master
git pull origin master
git add .
git commit -m '0527'
git push origin master
git pull
git pull origin master
git add .
git commit -m '0528'
git pull origin master
git add .
git push origin master
git commit -m '0529'
git push
git add .
git commit -m '0529'
git push origin master
cd ~/gitlab
rm -r data_aug/
git clone git@gitlab.yiwise.local:liyunliang/few-shot-learning.git
ls
cd few-shot-learning/
ls
cd papers/
ls
mv A\ Survey\ on\ Few-Shot\ Learning.pdf a-surver-on-fsl.pdf
ls
cd ..
git add .
git commit -m 'update readme'
git push
git add .
git commit -m 'update readme'
git push
cd ~/github/QiuZhao-ChongChongChong
ls
git pull origin master
git pull origin master
git add .
git commit -m '0531'
git push origin master
git pull origin master
git add .
git commit -m '儿童节快乐'
git push origin master
git pull origin master
git status
git add .
git commit -m '儿童节快乐'
git push origin master
ls
ls -a
rm .#README.org 
ls
git add .
git commit -m '儿童节快乐'
git push origin master
git pull origin master
git status
git add .
git commit -m '0601'
git pull origin master
git push origin master
git pull origin master
git add .
git commit -m '0602'
git pull origin master
git push origin master
git add .
git commit -m '0602'
git push origin master
"""
题目：
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例：
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

思路：
拓扑排序问题，从入度为0的节点开始删除它们的出度以及出度的节点的入度，然后把新的入度为0的节点加入套餐，做DFS遍历，直到没有入度为0的节点出现，此时如果节点都遍历过，即为True。
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for i in range(numCourses)]
        rejoin_list = [[] for i in range(numCourses)]
        for require in prerequisites:
            indegree[require[0]] += 1
            rejoin_list[require[1]].append(require[0])
        queue = []
        for i, d in enumerate(indegree):
            if d == 0:
                queue.append(i) 
        while queue:
            cur = queue.pop()
            for node in rejoin_list[cur]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
            numCourses -= 1
        return not numCourses
