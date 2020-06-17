'''
题目描述:
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

解体思路：
递推创建节点，关键点是终止位置标示！！
class node:
    def __init__(self):
        #是否为终止位置，及相关指示
        self.isend=False
        self.char_list=[0]*26



'''


class node:
    def __init__(self):
        #是否为终止位置，及相关指示
        self.isend=False
        self.char_list=[0]*26

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.char_list={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        #创建相应的节点
        pre_head=self.char_list
        if word[0] not in self.char_list.keys():
            self.char_list[word[0]]=node()
        start_node=self.char_list[word[0]]
        for ichar in word[1:]:
            if start_node.char_list[ord(ichar)-ord('a')]==0:
                start_node.char_list[ord(ichar)-ord('a')]=node()
            start_node=start_node.char_list[ord(ichar)-ord('a')]
        start_node.isend=True
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word[0] not in self.char_list.keys():
            return False
        start_node=self.char_list[word[0]]
        for ichar in word[1:]:
            if start_node.char_list[ord(ichar)-ord('a')]==0:
                return False
            start_node=start_node.char_list[ord(ichar)-ord('a')]
        return start_node.isend==True
        
       


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        word=prefix
        if word[0] not in self.char_list.keys():
            return False
        start_node=self.char_list[word[0]]
        for ichar in word[1:]:
            if start_node.char_list[ord(ichar)-ord('a')]==0:
                return False
            start_node=start_node.char_list[ord(ichar)-ord('a')]
        return True




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
