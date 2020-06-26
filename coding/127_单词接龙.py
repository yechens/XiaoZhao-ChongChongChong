'''
题目描述:
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

解题思路：
方法1:递归-超时
每次寻找“不同char为1”的word的list，并将剩余word递归 

方法2BFS:
构建同种形式的字典--->减少查找时间
例如：
dog 和log 都可以用 *og表示

注意：记录已经查找过的word

'''




from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #BFS
        import copy

       
        if endWord not in wordList:
            return 0
        #关键点——————————存储每种简化形式对应的词（不同词可能存在相同的简化形式，即 只有一个char不同）
        search_dict=defaultdict(list)
        for iword in wordList:
            for i in range(len(beginWord)):
                ikey=iword[:i]+'*'+iword[i+1:]
                search_dict[ikey].append(iword)
        #广度优先遍历,同时保存路径的长度
        queue=[(beginWord,1)]
        #记录已经遍历的节点
        tag={beginWord:True}
        while queue:
            tmpl=len(queue)
            for i in range(tmpl):
                tmp_word,res=queue.pop(0)
                #查找其改变一个字母形成的word
                for ilen in range(len(tmp_word)):
                    ikey=tmp_word[:ilen]+'*'+tmp_word[ilen+1:]
                    tmp_1_word_list=search_dict[ikey]
                    for i_tmp1word in tmp_1_word_list:
                        if i_tmp1word==endWord:
                            return res+1
                        #未查找过
                        if i_tmp1word not in tag.keys():
                            queue.append((i_tmp1word,res+1))
                            tag[i_tmp1word]=True
        return 0
                        



                    
        


        
        
        #递归--超时
        import copy
        if endWord not in wordList:
            return 0
        #记录不同word之间的不同字符的个数
        memory={}
        def get_diff_num(word1,word2):
            num=0
            for  ic1,ic2 in zip(word1,word2):
                if ic1!=ic2:
                    num+=1
            return num
        self.res=float('inf')
        def get_res(beginWord,endWord,word_list,icount):
            if beginWord==endWord:
                self.res=min(self.res,icount)

                return
            #找到只差一个单词的词
            new_find_list=[]
            #拷贝内存！！！！
            new_copy=copy.deepcopy(word_list)
            if beginWord in new_copy:
                new_copy.remove(beginWord)
            for iword in word_list:
                if get_diff_num(beginWord,iword)==1:
                    #去掉词防止重复查找
                    new_copy.remove(iword)
                    new_find_list.append(iword)
           
            print(new_find_list)
            for inewword in new_find_list:
                get_res(inewword,endWord,new_copy,icount+1)
        get_res(beginWord,endWord,wordList,1)
        if self.res==float('inf'):
            return 0
        return self.res
        





        
        
        #暴力法-超时
        if endWord not in wordList:
            return 0
        #记录不同word之间的不同字符的个数
        memory={}
        def get_diff_num(word1,word2):
            num=0
            for  ic1,ic2 in zip(word1,word2):
                if ic1!=ic2:
                    num+=1
            return num
        #不能加进去
        wordList.extend([beginWord,endWord])
        for i_index,iword in enumerate(wordList):
            for iword2 in wordList[i_index+1:]:
                if iword+'_'+iword2 not in memory.keys():
                    memory[iword+'_'+iword2]=get_diff_num(iword,iword2)
                    memory[iword2+'_'+iword]=get_diff_num(iword,iword2)
        self.res=float('inf')
        def get_change_times(word1,word2,memory,icount,change_path):
            if word1==word2:
                self.res=min(self.res,icount)
                print(change_path)
                return
            #找到只有一个不同的字符串
            only_onechardiff_word=[]
            for istr,inum in memory.items():
                if word1 in istr :
                    two_words=istr.split('_')
                    the_other_word=two_words[1]if two_words[0]==word1 else two_words[0]
                    if get_diff_num(word1,the_other_word)==1:
                        only_onechardiff_word.append(the_other_word)
            #set
            import copy
            only_onechardiff_word=set(only_onechardiff_word)
            if len(only_onechardiff_word):
                for iword_new in only_onechardiff_word:
                    new_memory=copy.deepcopy(memory)
                    new_change_path=copy.deepcopy(change_path)
                    del new_memory[iword_new+'_'+word1]
                    del new_memory[word1+'_'+iword_new]
                    new_change_path.append(iword_new)
                    get_change_times(iword_new,word2,new_memory,icount+1,new_change_path)
        get_change_times(beginWord,endWord,memory,0,list())
        if self.res==float('inf'):
            return 0
        return self.res+1
