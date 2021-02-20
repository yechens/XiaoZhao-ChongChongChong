# K近邻算法哪家强？KDTree、Annoy、HNSW原理和使用方法介绍

![K近邻算法哪家强？KDTree、Annoy、HNSW原理和使用方法介绍](https://pic2.zhimg.com/v2-d26fb5e193119cdac40a021ad8caf569_1440w.jpg?source=172ae18b)

> 作者：Giant
>
> 来源：*https://zhuanlan.zhihu.com/p/152522906*

## 1、什么是K近邻算法

K近邻算法（KNN）是一种常用的分类和回归方法，它的基本思想是从训练集中寻找和输入样本最相似的k个样本，如果这k个样本中的大多数属于某一个类别，则输入的样本也属于这个类别。

关于KNN算法，一个核心问题是：**如何快速从数据集中找到和目标样本最接近的K个样本？**

本文将从这个角度切入，介绍常用的K近邻算法的实现方法。具体将从原理、使用方法、时间开销和准确率对比等方面进行分析和实验。

## 2、距离度量

在介绍具体算法之前，我们先简单回顾一下KNN算法的三要素：**距离度量、k值的选择和分类决策规则**。

其中机器学习领域常用的距离度量方法，有欧式距离、余弦距离、曼哈顿距离、dot内积等

![img](https://pic3.zhimg.com/80/v2-51a21909a31d79b1fea02563f2d09fee_720w.jpg)

主流的近邻算法都支持上述不同的距离度量。其中n维特征空间的a、b向量的**欧式距离 ![[公式]](https://www.zhihu.com/equation?tex=d%7Bab%7D%3D%5Csqrt%7B%28x%7B1%7D-y%7B1%7D%29%5E%7B2%7D%2B%28x%7B2%7D-y%7B2%7D%29%5E%7B2%7D%2B...%2B%28x%7Bn%7D-y%7Bn%7D%29%5E%7B2%7D%7D) 体现数值上的绝对差异，而余弦距离基于余弦相似度（两个向量间夹角的余弦值），体现方向上的相对差异。**如果对向量做归一化处理，二者的结果基本是等价的。

实际应用中，需要根据业务目标来选择合适的度量方法。

## 3、K近邻算法的实现方法

K近邻的实现方式多达数十种，笔者从中挑选了几种常用、经典的方法作为分析案例。

首先最直观的想法（暴力法），是线性扫描法。将待预测样本和候选样本逐一比对，最终挑选出距离最接近的k个样本即可，时间复杂度O(n)。对于样本数量较少的情况，这种方法简单稳定，已经能有不错的效果。但是数据规模较大时，时间开销严重无法接受。

所以实际应用中，往往会寻找其他类型的数据结构来保存特征，以降低搜索的时间复杂度。

常用的存储结构可以分为树和图两大类。树结构的代表是KDTree，以及改进版BallTree和Annoy等；基于图结构的搜索算法有HNSW等。

## 4、KDTree和BallTree

### KDTree

kd 树是一种对k维特征空间中的实例点进行存储以便对其快速检索的树形数据结构。

**kd树是二叉树，核心思想是对 k 维特征空间不断切分（假设特征维度是768，对于(0,1,2,...,767)中的每一个维度，以中值递归切分）构造的树，每一个节点是一个超矩形**，小于结点的样本划分到左子树，大于结点的样本划分到右子树。

树构造完毕后，最终检索时（1）**从根结点出发，递归地向下访问kd树**。若目标点 ![[公式]](https://www.zhihu.com/equation?tex=x) **当前维**的坐标小于切分点的坐标，移动到左子树，否则移动到右子树，直至到达叶结点；（2）以此叶结点为“最近点”，**递归地向上回退，查找该结点的兄弟结点中是否存在更近的点**，若存在则更新“最近点”，否则回退；未到达根结点时继续执行（2）；（3）**回退到根结点时，搜索结束。**

kd树在维数小于20时效率最高，一般适用于训练实例数远大于空间维数时的k近邻搜索；当空间维数接近训练实例数时，它的效率会迅速下降，几乎接近线形扫描。

### BallTree

为了解决kd树在样本特征维度很高时效率低下的问题，研究人员提出了“球树“**[BallTree](https://link.zhihu.com/?target=http%3A//citeseer.ist.psu.edu/viewdoc/download%3Bjsessionid%3D1CB3038E97E8FC43825ABAADC0D3F8CC%3Fdoi%3D10.1.1.91.8209%26rep%3Drep1%26type%3Dpdf)**。KD 树沿坐标轴分割数据，**BallTree将在一系列嵌套的超球面上分割数据，即使用超球面而不是超矩形划分区域。**

具体而言，BallTree 将数据递归地划分到由质心 C 和 半径 r 定义的节点上，以使得节点内的每个点都位于由质心C和半径 r 定义的超球面内。通过使用三角不等式 ![[公式]](https://www.zhihu.com/equation?tex=%7CX%2BY%7C+%3C%3D+%7CX%7C+%2B+%7CY%7C) 减少近邻搜索的候选点数。

### coding 实验

以下实验均在CLUE下的[今日头条短文本分类数据集上](https://link.zhihu.com/?target=https%3A//github.com/CLUEbenchmark/CLUE%232tnews-%E4%BB%8A%E6%97%A5%E5%A4%B4%E6%9D%A1%E4%B8%AD%E6%96%87%E6%96%B0%E9%97%BB%E7%9F%AD%E6%96%87%E6%9C%AC%E5%88%86%E7%B1%BB-short-text-classificaiton-for-news)进行，训练集规模：53360条短文本。

**实验环境：Ubuntu 16.04.6，CPU: 126G/20核，python 3.6**

**requirement：scikit-learn、annoy、hnswlib**

实验中我使用了bert-as-service服务将文本统一编码为768维度的特征向量，作为近邻搜索算法的输入特征。

![img](https://pic2.zhimg.com/80/v2-ec7c0b67b20e7f667c4328703717392d_720w.jpg)

工具包sklearn提供了统一的kdtree和balltree使用接口，可以用一行代码传入特征集合、距离度量方式。

![img](https://pic3.zhimg.com/80/v2-b5c9832a6295e358d83e7698237d819a_720w.jpg)

为了减少推理时间，我这里仅选取验证集中前**200条**文本作为演示。

![img](https://pic2.zhimg.com/80/v2-a4d6342647fa9f15344b68902859a5c9_720w.jpg)

![img](https://pic3.zhimg.com/80/v2-a6de998f8059813e339975d17266ab46_720w.jpg)

观察实验发现，以**欧式距离**为度量标准，从5w条知识库中查找和输入文本最接近的**top3**，200条验证集中kd树和球树均正确检索出153条，但是kd树检索200条花费了37秒（185ms/条），球树花费15秒（75ms/条），**balltree的检索时间比kdtree快了1倍以上。**

## 5、Annoy

annoy全称“Approximate Nearest Neighbors Oh Yeah”，是一种适合实际应用的快速相似查找算法。Annoy 同样通过建立一个二叉树来使得每个点查找时间复杂度是O(log n)，和kd树不同的是，annoy没有对k维特征进行切分。

**annoy的每一次空间划分，可以看作聚类数为2的KMeans过程**。收敛后在产生的两个聚类中心连线之间建立一条垂线（图中的黑线），把数据空间划分为两部分。

![img](https://pic1.zhimg.com/80/v2-ba10b23ed9ab5e9d662877d4049df038_720w.jpg)

在划分的子空间内不停的递归迭代继续划分，直到每个子空间最多只剩下K个数据节点，划分结束。

![img](https://pic3.zhimg.com/80/v2-8abef4dc8a99ceb45fefc0026097d116_720w.jpg)

最终生成的二叉树具有如下类似结构，二叉树底层是叶子节点记录原始数据节点，其他中间节点记录的是分割超平面的信息。

![img](https://pic2.zhimg.com/80/v2-de75fee1b6aab31c367c71ae31230005_720w.jpg)

查询过程和kd树类似，先从根向叶子结点递归查找，再向上回溯即可，完整构建、查找过程可以参考[快速计算距离Annoy算法](https://link.zhihu.com/?target=https%3A//blog.csdn.net/m0_37850187/article/details/92712490)。

### coding 实验

annoy包封装了算法调用的python接口，底层经C++优化实现。继续使用头条文本数据集，调用方法如下：

![img](https://pic3.zhimg.com/80/v2-afc4f10caac2119772562c8125aa40fe_720w.jpg)

首先构建一个“AnnoyIndex”索引对象，需指定特征维度和距离度量标准（支持多种距离度量方式），并将所有数据集样本特征顺序添加到索引对象中。

之后需要在 build(n_trees) 接口中指定棵数。annoy通过构建一个森林（类似随机森林的思想）来提高查询的精准度，减少方差。构建完成后，我们可以将annoy索引文件保存到本地，之后使用时可以直接载入。（完整说明文档参考annoy的github仓库）

最后，我们对输入的200条文本依次查找top3近邻。

![img](https://pic2.zhimg.com/80/v2-c3105ef1befbf8192198d875104c8c35_720w.jpg)

我们发现，正确查找的样本数和之前相差不大（153 -> 149），但是**查找速度从之前的15秒（75ms/条）降到了0.08秒（0.4ms/条），提升了100倍以上**，达到了实际开发中的延时要求。

最后提一点，annoy接口中一般需要调整的参数有两个：**查找返回的topk近邻和树的个数**。一般树越多，精准率越高但是对内存的开销也越大，需要权衡取舍（tradeoff）。

## 6、HNSW

和前几种算法不同，HNSW（Hierarchcal Navigable Small World graphs）是**基于图存储**的数据结构。

### 图查找的朴素思想

![img](https://pic3.zhimg.com/80/v2-a6f6e4b8ba56b09fb762fac15d85f762_720w.jpg)

> 假设我们现在有13个2维数据向量，我们把这些向量放在了一个平面直角坐标系内，隐去坐标系刻度，它们的位置关系如上图所示。
> 朴素查找法：不少人脑子里都冒出过这样的朴素想法，把某些点和点之间连上线，构成一个查找图，存储备用；当我想查找与粉色点最近的一点时，我从任意一个黑色点出发，计算它和粉色点的距离，与这个任意黑色点有连接关系的点我们称之为“友点”（直译），然后我要计算这个黑色点的所有“友点”与粉色点的距离，从所有“友点”中选出与粉色点最近的一个点，把这个点作为下一个进入点，继续按照上面的步骤查找下去。如果当前黑色点对粉色点的距离比所有“友点”都近，终止查找，这个黑色点就是我们要找的离粉色点最近的点。

HNSW算法就是对上述朴素思想的改进和优化。为了达到快速搜索的目标，hnsw算法在构建图时还至少要满足如下要求：**1）图中每个点都有“友点”；2）相近的点都互为“友点”；3）图中所有连线的数量最少；4）配有高速公路机制的构图法。**

HNSW低配版NSW论文中配了这样一张图，短黑线是近邻点连线，长红线是“高速公路机制”，如此可以大幅减少平均搜索的路径长度。

![img](https://pic3.zhimg.com/80/v2-b33f8a02943361c4d0d4785525564c5e_720w.jpg)

在NSW基础之上，HNSW加入了**跳表结构**做了进一步优化。最底层是所有数据点，每一个点都有50%概率进入上一层的有序链表。这样可以保证**表层是“高速通道”，底层是精细查找**。通过层状结构，将边按特征半径进行分层，使每个顶点在所有层中平均度数变为常数，从而将NSW的计算复杂度由多重对数复杂度降到了对数复杂度。

![img](https://pic1.zhimg.com/80/v2-e817bcc8fbd7c66b5106fb13b40e9f00_720w.jpg)

关于HNSW的详细内容可以参考原论文[Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/1603.09320)和博客[HNSW算法理论的来龙去脉](https://link.zhihu.com/?target=https%3A//blog.csdn.net/u011233351/article/details/85116719)。

### coding 实验

通过 hnswlib 库，可以方便地调用hnsw算法。

![img](https://pic4.zhimg.com/80/v2-837524a4e0da35de1c89f637f8e40c8f_720w.jpg)

同样，首先将输入特征载入索引模型并保存到本地，下一次可以直接载入内容。具体测试实验：

![img](https://pic1.zhimg.com/80/v2-e9e5bc7afa87a9ce05aeb568ab68ec88_720w.jpg)

最终，**预测200条样本耗时0.05秒（0.25ms/条）**，速度优于annoy。

![img](https://pic4.zhimg.com/80/v2-e70f7b0f940e07f8257062a63d959b57_720w.jpg)

此外，同样的53360条特征向量（768维度），保存为静态索引文件后 ann 索引的大小是227MB，hnsw索引是171MB，从这一点看hnsw也略胜一筹，可以节约部分内存。

参数设置中，ef表示最近邻动态列表的大小（需要大于查找的topk），M表示每个结点的“友点”数，是平衡时间/准确率的超参数。可以根据服务器资源和查找的召回率等，做相应调整。

## 7、小结

本文介绍了几种常用的k近邻查找算法，kdtree是KNN的一种基本实现算法；考虑到并发、延时等要素，annoy、hnsw是可以在实际业务中落地的算法，其中**bert/sentence-bert+hnsw**的组合会有不错的召回效果。

除此之外，还有众多近邻算法。感兴趣的同学可以阅读相关论文做进一步研究。

![img](https://pic1.zhimg.com/80/v2-df7903afecf64800b2f54dbda56f9bcc_720w.jpg)



## **深度学习资源下载**

**在公众号「NLP情报局」后台回复“三件套”，即可获取深度学习三件套：**

**《PyTorch深度学习》，《Hands-on Machine Learning》，《Python深度学习》**

![img](https://mmbiz.qpic.cn/mmbiz_png/V23nFVyYSrAyUicfJ9dDvyqXqjysKXkAlWt1ROwXHmFn0cqcicpY0JVDeibIJwNjPWiaYF3pOzPehyvvHxZa2mFoIg/640?wx_fmt=png)



## Reference：

1.[Annoy - Github](https://link.zhihu.com/?target=https%3A//github.com/spotify/annoy)

2.[HNSW - Github](https://link.zhihu.com/?target=https%3A//github.com/nmslib/hnswlib)

3.[Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://link.zhihu.com/?target=https%3A//arxiv.org/abs/1603.09320)

4.[Five Balltree Construction Algorithms](https://link.zhihu.com/?target=http%3A//citeseer.ist.psu.edu/viewdoc/download%3Bjsessionid%3D1CB3038E97E8FC43825ABAADC0D3F8CC%3Fdoi%3D10.1.1.91.8209%26rep%3Drep1%26type%3Dpdf)

5.李航 《统计学习方法》P53-P57: K近邻法的实现: kd树

6.[快速计算距离Annoy算法原理及Python使用](https://link.zhihu.com/?target=https%3A//blog.csdn.net/m0_37850187/article/details/92712490)

7.[HNSW算法理论的来龙去脉](https://link.zhihu.com/?target=https%3A//blog.csdn.net/u011233351/article/details/85116719)

8.[高维空间最近邻逼近搜索算法评测](https://zhuanlan.zhihu.com/p/37381294)