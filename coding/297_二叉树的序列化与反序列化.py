'''
题目描述：
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

解题思路：
方法-：DFS（序列化时，需要添加None标示子节点为空，反序列化时，每次都需要pop)
方法二：前序中序遍历
    (易错点：node的val可能有相同的值，所以使用node的地址作为唯一的标识;
    易忘点：
            #前序遍历和中序遍历中，子树的长度一样
            #前序遍历中是【根，左子树，右子树】
            #中序遍历中是【左子树，根，右子树】
            #其中两种遍历中的隐含条件是：左子树的长度一至)
方法三：层序遍历（超时）


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS
class Codec:

    def serialize(self, root):
        val_list=[]
        #直接保留node的地址
        def DFS(root):
            if not root:return val_list.append(None)
            val_list.append(root)
            (DFS(root.left))
            (DFS(root.right))
            return 
        DFS(root)
        #print(val_list)
        return val_list
    def deserialize(self, data):
        def deDFS(val_list):
            #每次都要pop
            if not val_list[0]:
                
                val_list.pop(0)
                return None
            root=val_list.pop(0)
            root.left=deDFS(val_list)
            root.right=deDFS(val_list)
            return root
        return deDFS(data)
            
            



#前序中序遍历
class Codec___:

    def serialize(self, root):
        #前序中序遍历
        pre_sequence=[]
        mid_sequence=[]
        def pre_traverse(root):
            if not root:return
            #易错点：node的val可能有相同的值，所以使用node的地址作为唯一的标识
            pre_sequence.append(root)
            pre_traverse(root.left)
            pre_traverse(root.right)
        pre_traverse(root)
        def mid_traverse(root):
            if not root:return
            
            mid_traverse(root.left)
            mid_sequence.append(root)
            mid_traverse(root.right)
        mid_traverse(root)
        #print(pre_sequence,mid_sequence)
        return[pre_sequence,mid_sequence]
    def deserialize(self, data):
        pre_sequence=data[0]
        mid_sequence=data[1]
        #print(pre_sequence,mid_sequence)
        def deser(pre_sequence,mid_sequence):
            #递归终止条件
            if len(pre_sequence)==0:
                return None
            root=(pre_sequence[0])
            #易忘点：
            #前序遍历和中序遍历中，子树的长度一样
            #前序遍历中是【根，左子树，右子树】
            #中序遍历中是【左子树，根，右子树】
            #其中两种遍历中的隐含条件是：左子树的长度一至
            root_index=mid_sequence.index(pre_sequence[0])
            left_len=root_index
            right_len=len(pre_sequence)-root_index-1
            
            root.left=deser(pre_sequence[1:left_len+1],mid_sequence[:root_index])
            
            root.right=deser(pre_sequence[left_len+1:],mid_sequence[root_index+1:])
            return root
        return deser(pre_sequence,mid_sequence)


            



        

#层序遍历超时
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:return None
        val_list=[]
        queue=[root]
        layers_count=0
        while queue:
            layers_count+=1
            tmpel=len(queue)
            tmp_val=[]
            tmp_queue=[]
            none_count=0
            for i in range(tmpel):
                tmpnode=queue.pop(0)
                if not tmpnode:
                    tmp_val.append(None)
                    none_count+=1
                    tmp_queue.append(None)
                    tmp_queue.append(None)
                    continue
                tmp_val.append(tmpnode.val)
                if tmpnode.left:
                    tmp_queue.append(tmpnode.left)
                else:
                    tmp_queue.append(None)
                    
                if tmpnode.right:
                    tmp_queue.append(tmpnode.right)
                else:
                    tmp_queue.append(None)
                    
            #终止
            if none_count==tmpel:
                break
            else:
                queue=tmp_queue
                val_list.extend(tmp_val)
        #print(val_list)


        return val_list
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:return None
        val_list=data
        for inode in range(len(val_list)):
            inode+=1
            if inode==1:
                val_list[inode-1]=TreeNode(val_list[inode-1])
                continue
            else:
                father_node=val_list[inode//2-1]
                if not father_node:
                    continue
                #左节点
                if inode%2==0:
                    #易错点：节点中有0，要判断是不是None
                    if val_list[inode-1]!=None:
                        left_node=TreeNode(val_list[inode-1])
                        father_node.left=left_node
                        val_list[inode-1]=left_node
                    else:
                        father_node.left=None
                #右节点
                else:
                    #易错点：节点中有0，要判断是不是None
                    if val_list[inode-1]!=None:
                        right_node=TreeNode(val_list[inode-1])
                        father_node.right=right_node
                        val_list[inode-1]=right_node
                    else:
                        father_node.right=None
        return val_list[0]
'''





        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
