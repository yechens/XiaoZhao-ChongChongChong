# 天池NLP赛道top指南

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/V23nFVyYSrBUAiapSCy0AicBsXKjYPXFmydQGXj5eO6wb6LtCo8AIl2bwsfOCw269pIfbBbiag5G8qKOSM4NMq2iag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

*大家好，我是Giant，这是我的第****1****篇文章。*

2020年初，新冠疫情席卷全球。除了“待在家，不乱跑”，我想还能从哪为抗击疫情出点微薄之力呢？

碰巧室友推送了一个阿里天池“[新冠疫情相似句对判定大赛](https://link.zhihu.com/?target=https%3A//tianchi.aliyun.com/competition/entrance/231776/introduction)”链接，于是秉持“重在参与”的心态参加了比赛。经过半个月的努力，最终结果勉强不错（第6），收获了证书和一台Kindle。

![img](https://pic4.zhimg.com/80/v2-b2bb122d33ded750139e5fe63c94b063_720w.jpg)

2021年1月，疫情形势依然严峻，幸运的是国家不仅及时稳住了疫情，还研发出有效的疫苗。借助疫情主题的比赛，我希望帮助更多读者，入门自然语言处理的基本任务——**文本相似匹配**。

**开源代码：**

*[https://github.com/yechens/COVID-19-sentence-pair](https://link.zhihu.com/?target=https%3A//github.com/yechens/COVID-19-sentence-pair)*

## 一、数据分析

任务背景非常直观，主办方给定了“肺炎”、“支气管炎”、“上呼吸道感染”等医疗背景下的用户真实提问，要求选手通过算法识别任意2个问题，是否想表达同一个意思。举例：

```python3
问题1: “轻微感冒需不需要吃药？”
问题2: “轻微感冒需要吃什么药？”
```

问题1关心“是否得吃药”，问题2关心“该吃什么药”，侧重点不同所以意思不同，用label=0表示句子不相似。

数据集样本都是三元组(query1, query2, label)。为了降低难度，每一个问题的长度被控制在20字以内。

![img](https://pic3.zhimg.com/80/v2-a1e3f2a156e7beba3d84998ba42e2c26_720w.jpg)

比赛的训练集、验证集分别包含8746、2001条三元组。我们从dev中随机保留了800条样本作为最终dev，其余均加入训练。

### 数据增强

拿到数据简单分析后，我发现数据集已经过清洗，竟然异常的干净整齐（没有杂乱的符号、不通顺的句子），label分布几乎也接近1 : 1。

再观察数据，相同的query1总是按顺序排列在一起，随后跟着不同的query2。这种分布很容易想到一种数据增强策略：**相似传递性**。

![img](https://pic1.zhimg.com/80/v2-3fa4ec1cbd82b35526a19c195a075d6c_720w.jpg)相同query1总是相邻排列

```text
A <-> B 相似 and A <-> C 相似 => B <-> C 相似
```

最终我额外获得了**5000**条高质量的数据，比赛准确率因此提升了**0.5%**。

### 实体替换

此外，我们也尝试了训练一个NER模型挖掘文本中的**医疗实体**，如“胸膜炎”、“肺气肿”，再通过word2vec查找最接近的实体进行替换。

但这种方式并没有提升最终结果。我觉得原因有2个：

- 1W条样本规模偏小，NER模型识别误差较大
- 词向量没有针对医疗场景训练，包含的医疗实体很少

## 二、匹配方法实现

文本匹配有非常多简单又实用的方法，例如：

- 基于**字符统计**：字符串匹配、编辑距离、Jaccards距离
- 基于**语言模型**：word2vec/glove词向量、BERT
- 基于**神经网络**：孪生网络、TextCNN、DSSM、ESIM、FastText等

由于比赛需要尽可能获得高分，这里主要介绍基于神经网络和BERT的文本匹配算法。

BERT[1]是一种预训练语言模型，通过海量文本、Transformer架构和MLM训练任务在众多NLP任务上取得了优异成果。对BERT不了解的读者，可以参考我之前的文章：[从BERT、XLNet到MPNet，细看NLP预训练模型发展变迁史](https://zhuanlan.zhihu.com/p/166013414)

比赛中我们测试了5-6种不同的神经网络方法，并最终选择了3种在dev上表现最好的模型加权融合。具体可以参考代码中的 ![[公式]](https://www.zhihu.com/equation?tex=code%2Fmodel.py) 文件。

### 文本CNN（TextCNN）

TextCNN是Yoon Kim[2]在2014年提出的用于句子分类的卷积神经网络。文本匹配任务本质上可以理解成二分类任务（0:不相似，1:相似），所以一般的分类模型也能满足匹配需求。

![img](https://pic4.zhimg.com/80/v2-08590c01b52c447b12c02a5afe788233_720w.jpg)TextCNN

与图像中的二维卷积不同，**TextCNN采用的是一维卷积**，每个卷积核的大小为 ![[公式]](https://www.zhihu.com/equation?tex=h%5Ctimes+k) (h为卷积核窗口，k为词向量维度)。文中采用了不同尺寸的卷积核，来提取不同文本长度的特征。

然后，作者对卷积核的输出进行**最大池化操作**，只保留最重要的特征。各个卷积核输出经MaxPooling后拼接形成一个新向量，最后输出到全连接层分类器(Dropout + Linear + Softmax)实现分类。

我们知道，文本中的**关键词**对于判断2个句子是否相似有很大影响，而CNN局部卷积的特效能很好的捕捉这种关键特征。同时TextCNN还具有参数量小，训练稳定等优点。

### 文本RNN（TextRCNN）

相比TextCNN，TextRCNN的模型结构看起来复杂一些。

![img](https://pic2.zhimg.com/80/v2-153142903a3ad12e8322bf29635d0c41_720w.jpg)

简单浏览论文后，会发现它的思路其实简单，粗暴。

首先通过词向量获得字符编码 ![[公式]](https://www.zhihu.com/equation?tex=e%28w_%7Bi%7D%29) ，随后将其通过**双向RNN**学习上下文特征，编码得到 ![[公式]](https://www.zhihu.com/equation?tex=c_l%28w_%7Bi%7D%29) 、 ![[公式]](https://www.zhihu.com/equation?tex=c_r%28w_%7Bi%7D%29) 。

再将词向量 ![[公式]](https://www.zhihu.com/equation?tex=e%28w_%7Bi%7D%29) 和 ![[公式]](https://www.zhihu.com/equation?tex=c_l%28w_%7Bi%7D%29) 、 ![[公式]](https://www.zhihu.com/equation?tex=c_r%28w_%7Bi%7D%29) **拼接**得到新向量，输入经tanh函数激活的全连接网络。最后，将网络的输出**最大池化**，并输入另一个全连接分类器完成分类。

RNN模型对于长文本有较好的上下文“记忆”能力，更适合处理文本这种包含时间序列的信息。

### BERT + MLP （fine-tune）

最后一种方法，直接用语言模型BERT最后一层Transformer的输出，接一层Dense实现文本匹配。

![img](https://pic1.zhimg.com/80/v2-e3546ecaee19fb4d2a932169e8b43c5c_720w.jpg)

实验中我们发现，对最终输出的每个token特征取平均（**MeanPooling**）效果好于直接使用首字符“[CLS]”的特征。

模型权重上，崔一鸣等人[4]发布的中文roberta_wwm_ext_large模型效果要好于BERT_large。

![img](https://pic2.zhimg.com/80/v2-4ecdec47bb372a51149575f543fca359_720w.jpg)

最后，我们根据这三种模型在dev上的准确率设置了不同比重，通过**自动搜索**找到最优权重组合，在线上测试集取得了**96.26%**的准确率。

读者可以在公众号“**NLP情报局**”后台回复“**文本匹配**”直接下载模型论文。

## 三、涨分trick

做一个深度学习主导的算法比赛，除了分析数据与模型，一些**trick**也是获得高分的重要因素。这里罗列了一些常用策略。

- 数据增强[5]
- 标签平滑
- 自蒸馏
- 文本对抗训练[6]
- 模型融合
- 特征筛选
- 使用多个学习率[7]

针对这次文本匹配任务，数据增强、标签平滑、模型融合、多学习率都被证明是有效的。

## 四、总结

过去将近1年的天池“新冠疫情相似句对判定大赛”，任务并不复杂，是入门NLP项目实战，提升编程能力的很好锻炼机会。

![img](https://pic2.zhimg.com/80/v2-f0c89e7e3a42fa915e98c985842f0d19_720w.jpg)

比赛虽然结束了，疫情犹在。愿每位读者出门多加防护，一定要保护好自己哦！

------

关注公众号**「NLP情报局」**，第一时间阅读自然语言处理、机器学习算法精选干货～

## Reference：

[1] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.

[2] Convolutional Neural Networks for Sentence Classification.

[3] Recurrent Convolutional Neural Networks for Text Classification.

[4][崔一鸣：Chinese-BERT-wwm](https://link.zhihu.com/?target=https%3A//github.com/ymcui/Chinese-BERT-wwm)

[5] [简枫：一文了解NLP中的数据增强方法](https://zhuanlan.zhihu.com/p/145521255)

[6] [Nicolas：【炼丹技巧】功守道：NLP中的对抗训练 + PyTorch实现](https://zhuanlan.zhihu.com/p/91269728)

[7] [量子位：称霸Kaggle的十大深度学习技巧](https://zhuanlan.zhihu.com/p/41379279)