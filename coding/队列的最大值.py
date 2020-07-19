'''
题目描述：
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]

解题思路：
双端队列！！！


'''

import queue
class MaxQueue:
    #双端队列
    def __init__(self):
        self.seq=queue.Queue()
        self.deque=queue.deque()


    def max_value(self) -> int:
        if self.deque:

            return self.deque[0] 
        else:
             return -1

    def push_back(self, value: int) -> None:
        #queue 没有 append
        self.seq.put(value)
        while self.deque and self.deque[-1]<value:
            self.deque.pop()
        self.deque.append(value)


    def pop_front(self) -> int:
        if not self.deque:return -1
        ans=self.seq.get(0)
        if ans==self.deque[0]:
            #popleft
            self.deque.popleft()
        return ans



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
