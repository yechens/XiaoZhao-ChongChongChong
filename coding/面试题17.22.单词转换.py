'''
题目描述：
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。

编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

解题思路：
构建只有单个不同char的词典！！！+DFS
'''

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        #转化为DFS
        if endWord not in wordList:
            return []
        #构建只有单个不同char的词典
        worddict={}
        wordList+=[beginWord]
        for iword in wordList:
            wlen=len(iword)
            for i in range(wlen):
                if iword[:i]+'*'+iword[i+1:] not in worddict.keys():
                    worddict[iword[:i]+'*'+iword[i+1:]]=set()
                worddict[iword[:i]+'*'+iword[i+1:]].add(iword)
        #存储访问过的节点
        self.res=[]
        state={iword:1 for id_,iword in enumerate(wordList)}
        word2id={iword:id_ for id_,iword in enumerate(wordList)}
        import copy
        #print(worddict)
        def DFS(beginWord,save_list):
            print(beginWord)
            if state.get(beginWord,0)==2:
                return 
            if not self.res and beginWord ==endWord:
                print(save_list+[endWord])
                self.res=copy.deepcopy(save_list+[endWord])
                return 
            #找到相差一个char的词
            state[beginWord]=2
            all_nextword=[]
            wlen=len(beginWord)
            for i in range(wlen):
                all_nextword.extend(worddict[beginWord[:i]+'*'+beginWord[i+1:]])
            (all_nextword)=set(all_nextword)
            
            for iword in all_nextword:
                DFS(iword,save_list+[beginWord])
        DFS(beginWord,[])
        return self.res
