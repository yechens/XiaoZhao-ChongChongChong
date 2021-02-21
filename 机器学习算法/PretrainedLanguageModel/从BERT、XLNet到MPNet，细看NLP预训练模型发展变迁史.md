# 从BERT、XLNet到MPNet，细看NLP预训练模型发展变迁史

![从BERT、XLNet到MPNet，细看NLP预训练模型发展变迁史](https://pic1.zhimg.com/v2-695eae2893a8401000e3355aef1fb8d4_1440w.jpg?source=172ae18b)

> 作者：Giant
>
> 原文链接：*https://zhuanlan.zhihu.com/p/166013414*

20世纪以来，自然语言处理（NLP）领域的发展涌现了许多创新和突破。NLP中许多之前机器不可能完成的任务，如阅读理解、人机对话、自动写新闻稿等，正逐渐成为现实，甚至超越了人类的表现。

如果总结过去20年里，无数先辈辛劳付出带来的璀璨成果，以下3个代表性工作列入NLP名人堂，应该实至名归：**1）2003年Bengio提出神经网络语言模型NNLM，**从此统一了NLP的特征形式——Embedding；**2）2013年Mikolov提出词向量Word2vec**，延续NNLM又引入了大规模预训练（Pretrain）的思路；**3）2017年Vaswani提出Transformer模型，**实现用一个模型处理多种NLP任务。

基于Transformer架构，2018年底开始出现一大批预训练语言模型，刷新众多NLP任务，形成新的里程碑事件。本文将跨越2018-2020，着眼于3个预训练代表性模型BERT、XLNet和MPNet，从以下4个章节介绍NLP预训练语言模型的发展变迁史：

```text
1.BERT 原理及 MLM 简述
2.XLNet 原理及 PLM 简述
3.MPNet 原理及创新点简述
4.NLP预训练模型趋势跟踪
附录：快速上手BERT的4大工具包
```

## 1.BERT 原理及 MLM 简述

![img](https://pic4.zhimg.com/80/v2-1948311b060b539afc844dcf70837d03_720w.jpg)

自谷歌2018年底开源BERT，NLP界的游戏规则某种程度上被“颠覆”了；一时间，这个芝麻街的可爱小黄人形象，成为众多NLPer及其他DL、ML研究者们的拥趸。

“BERT一把梭“，“遇事不决就BERT”，“BERT在手，天下我有”，表达了使用者们对BERT的心声。也因为BERT，NLP的准入门槛大幅下降，一些较浅层的NLP任务如文本分类、相似匹配、聚类某种程度上可以被认为是完全解决。

![img](https://pic3.zhimg.com/80/v2-fdad3308005f913f36bb88381c627fa6_720w.jpg)

BERT为什么会有如此引人注目的优良效果？下面我们再来回顾下BERT到底是什么。

### 1.1 Masked Language Model & Next Sentence Predict

BERT本质上是一个自编码（Auto Encoder）语言模型，为了能见多识广，BERT使用3亿多词语训练，采用12层双向Transformer架构。注意，BERT只使用了Transformer的编码器部分，可以理解为BERT旨在学习庞大文本的内部语义信息。

具体训练目标之一，是被称为掩码语言模型的MLM。即输入一句话，给其中15%的字打上“mask”标记，经过Embedding输入和12层Transformer深度理解，来预测“mask”标记的地方原本是哪个字。

```text
input:   欲把西[mask]比西子，淡[mask]浓抹总相宜
output:  欲把西[湖]比西子，淡[妆]浓抹总相宜
```

例如我们输入“**欲把西[mask]比西子，淡[mask]浓抹总相宜”给BERT**，它需要根据没有被“mask”的上下文，预测出掩盖的地方是“湖”和“妆”。

MLM任务的灵感来自于人类做完形填空。挖去文章中的某些片段，需要通过上下文理解来猜测这些被掩盖位置原先的内容。

训练目标之二，是预测输入的两句话之间是否为上下文（NSP）的二分类问题。继续输入“ 欲把西[湖]比西子，淡[妆]浓抹总相宜”，BERT将预测这两句话的组合是否合理（这个例子是“yes”）。（随后的研究者对预训练模型探索中证明，NSP任务过于简单，对语言模型的训练作用并不是很大）

通过这两个任务和大规模语料训练，BERT语言模型可以很好学习到文本之间的蕴含的关系。

### 1.2 Self-Attention

接下来简单介绍BERT以及XLNet、MPNet所使用Transformer的核心模块：自注意力机制。



![img](https://pic2.zhimg.com/80/v2-9b87d22d48a658a0b7149afdc3388a99_720w.jpg)Self-Attention

自注意力机制重点在于学习输入序列自身的内部信息。具体地，每个 ![[公式]](https://www.zhihu.com/equation?tex=token+) 可以观察到序列中其他所有 ![[公式]](https://www.zhihu.com/equation?tex=token+) 的信息，并通过”注意力“交互，其余的 ![[公式]](https://www.zhihu.com/equation?tex=token%27) 会产生不同大小地权重（整个过程类似加权）。上例中，“西子”和“西湖”关系紧密，因此它们之间的attention权重更大（大于“西子”和“淡妆”）。最终自注意力层的输出涵盖了序列所有 ![[公式]](https://www.zhihu.com/equation?tex=token+) 的语义信息，实现了双向编码上下文。

同时，这种双向性使得模型可以同时观测序列的所有位置，解决了RNN等递归模型无法高效并行的瓶颈。

### 1.3 Denoising Auto Encoder

由于架构采用12层双向Transformer且训练目标包含还原 ![[公式]](https://www.zhihu.com/equation?tex=mask) 位置的信息，BERT被称为去噪自编码语言模型（DAE）。

而在BERT之前，NLP领域的语言模型几乎是Auto Regression（自回归）类型，即当前位置的字符预测 ![[公式]](https://www.zhihu.com/equation?tex=T%7Bi%7D) 需要编码之前 ![[公式]](https://www.zhihu.com/equation?tex=T%7B%280%3Ai-1%29%7D) tokens的语义信息，使得模型训练/预测只能单向进行。

虽然ELMO采用了BiLSTM，但只是前向、后向两次输出的简单拼接，包含的全局语义信息依然较弱。

### 1.4 BERT缺点

虽然效果好，BERT的缺点也很明显。从建模本身来看，**随机选取15%的字符mask忽视了被mask字符之间可能存在语义关联的现象**，从而丢失了部分上下文信息。同时，微调阶段没有mask标记，导致预训练与微调的不一致。

## 2.XLNet 原理及 PLM 简述

和BERT不同，**XLNet本质上是用自回归语言模型来同时编码双向语义信息的思路**，可以克服BERT存在的依赖缺失和训练/微调不一致的问题。同时为了弥补自回归模型训练时无法同时看到上下文的缺陷，XLNet曲线救国地提出了PLM排列语言模型的训练方式。

### 2.1 排列语言模型 - Permutation Language Model

对于一个长度为N的序列，我们知道其存在 ![[公式]](https://www.zhihu.com/equation?tex=N%21) 种因式分解顺序，通过一次采样一种序列的因式分解组合，每个token总是能够在不同的序列中观察到其他所有token；同时模型参数对于所有的因式分解顺序共享，因此从期望的角度上看，XLNet模型能够双向地编码上下文。

![img](https://pic1.zhimg.com/80/v2-d36624745ba07415b3f010dcf586eaa0_720w.jpg)

例如，初始序列为 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B1%7D%2Cx%7B2%7D%2Cx%7B3%7D%2Cx%7B4%7D%29) ，这里的 ![[公式]](https://www.zhihu.com/equation?tex=x%7B3%7D) 只能关注到前面的 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B1%7D%2Cx%7B2%7D%29)，但在某种因式分解排列 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B4%7D%2Cx%7B2%7D%2Cx%7B1%7D%2Cx%7B3%7D%29) 中， ![[公式]](https://www.zhihu.com/equation?tex=x%7B3%7D) 具备了关注 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B4%7D%2Cx%7B2%7D%2Cx%7B1%7D%29) 的能力。另外，XLNet的原始输入和BERT相同，依然是正常排序的 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B1%7D%2Cx%7B2%7D%2Cx%7B3%7D%2Cx%7B4%7D%29) 。

### 2.2 双流自注意力

那XLNet是如何在保持输入顺序不变的同时，对序列进行乱序编码的呢？

简单而言，通过**Attention掩码机制**，将当前token及其之后的token（不该看到的部分）嵌入信息用attention-mask掩盖。具体实现上，使用了一种**双流自注意力机制**。

例如某个序列的因式分解顺序为 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B2%7D%2Cx%7B1%7D%2Cx%7B4%7D%2Cx%7B3%7D%29) 和 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B2%7D%2Cx%7B1%7D%2Cx%7B3%7D%2Cx%7B4%7D%29)，如果需要预测第三个位置的token，传统的自回归模型通过 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B2%7D%2Cx%7B1%7D%29) 的编码来预测后面的token，概率表达式为 ![[公式]](https://www.zhihu.com/equation?tex=P%28x%7Bt%7D%7C%28x%7B2%7D%2Cx%7B1%7D%29%29)。然而这样会带来一个问题：x2和x1的编码和需要预测的下一个token是无关的，xt既可以是x4也可以是x3，即P(x3|x2,x1) = P(x4|x2,x1)，这显然不合理（传统RNN是按正常的序列进行递归预测，位置是正确的，所以不存在这个问题）。因此XLNet需要引入待预测token的位置信息，例如 ![[公式]](https://www.zhihu.com/equation?tex=P%28x%7B4%7D%7C%28x%7B2%7D%2Cx%7B1%7D%2Cpos4%29%29)或 ![[公式]](https://www.zhihu.com/equation?tex=P%28x%7B3%7D%7C%28x%7B2%7D%2Cx%7B1%7D%2Cpos3%29%29) ，确保生成合理的结果。

然而这又带来了新的矛盾。对于某个因式分解顺序 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B2%7D%2Cx%7B1%7D%2Cx%7B4%7D%2Cx%7B3%7D%29)，在预测x4的时候，模型不能编码自身的token-embedding，只能编码前面的 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B2%7D%2Cx%7B1%7D%29)以及自身的position-embedding，否则训练就没有意义了；然而在预测x3的时候，又需要用到x4的完整的编码信息。如果继续沿用BERT的自注意力机制必然存在问题，因此XLNET将自注意力机制拆分为Query流和Content流。Query流中当前token只能关注到前面的token和自身的位置信息，Content流中当前token可以关注到自身。

**具体来看，XLNET将序列拆分为2部分，序列的后部分（约占句长的1/K，K为超参数）为需要预测的部分，前部分为已知上下文。已知的上下文不做预测，因此只计算content流注意力，每个token都编码之前token以及自身的完整信息。从预测部分开始，每个token同时计算Query流和Content流注意力：Query流的输出用于预训练做预测，Content流的输出提供给后续待预测token计算Query流，这就保证了当预测当前token时，它无法看到自身编码；当前token预测结束后，将其Content流作为上下文部分的编码提供给后续需要预测的token。预训练过程计算2种注意力，微调过程去除了Query流，只保留Content流，因为不需要对token进行词表空间的预测，而是需要编码整个上下文语义用于下游任务。**

![img](https://pic1.zhimg.com/80/v2-aad2021dda260ae88f21db509b366f1c_720w.jpg)

### 2.3 双向 AR Model

前面提到 Auto Regression 模型的缺点是只能单向编码，但它能够编码被预测的token之间的联系，即克服了BERT被mask字符间信息丢失的缺点。其次，通过上文的PLM模型弥补了自回归语言模型只能单向编码的缺点。AR模型在预训练和下游任务中都没有对输入序列进行损坏（遮盖部分token，引入噪声），消除了模型在预训练和微调过程中的差异。

虽然在期望上看，PLM几乎实现了双向编码功能的自回归模型，但是**针对某一个因式分解序列来说，被预测的token依然只能关注到它前面的序列**，导致模型依然无法看到完整序列信息和位置信息。

## 3.MPNet 原理及创新点简述

结合BERT、XLNet的思路，南京大学和微软在2020年共同提出了新的预训练语言模型**MPNet：Masked and Permuted Pre-training for Language Understanding。**

MPNet的创新点在于4个字：**位置补偿（position compensation）**，大家先留个印象，下文会再详细介绍。

论文开篇，作者针对上文MLM、PLM各自特点，希望用一种统一的模型既保留二者的优点，又弥补它们的不足，这就是MPNet。

### 3.1 统一视角

![img](https://pic2.zhimg.com/80/v2-b5845a13fd7eeb7608a56fde46495e85_720w.jpg)

首先，作者通过重新排列和切分输入序列中的tokens，将MLM和PLM统一为非预测部分（non-predicted）和预测部分（predicted），如图(a),(b)右侧。如此一来，MLM和PLM就拥有了相似的数学表达公式，仅在条件部分有细小差异。

![img](https://pic2.zhimg.com/80/v2-96011126b519b36edfec2dbbba7d64a9_720w.jpg)

### 3.2 模型架构

![img](https://pic4.zhimg.com/80/v2-ca9a89048e859718bed824c6b47ae2c3_720w.jpg)

**为缓解BERT-mask可能丢失依赖信息的问题，MPNet沿用了XLNet的自回归结构，同时为弥补XLNet无法捕捉全部序列位置信息的缺陷，添加了「位置补偿」：针对需要预测的token，额外添加了它们的位置信息。使得自回归过程中，在任意一个位置i，除了可以看到之前部分的token编码，还能看到序列所有token的位置编码（类似于BERT）。**

例如，对于一个长度为6的token序列 ![[公式]](https://www.zhihu.com/equation?tex=x%3D%28x%7B1%7D%2Cx%7B2%7D%2Cx%7B3%7D%2Cx%7B4%7D%2Cx%7B5%7D%2Cx%7B6%7D%29) ，采样得到一个因式分解序列 ![[公式]](https://www.zhihu.com/equation?tex=x%7Bz%7D%3D%28x%7B1%7D%2Cx%7B3%7D%2Cx%7B5%7D%2Cx%7B4%7D%2Cx%7B6%7D%2Cx%7B2%7D%29) ；假设非预测部分为 ![[公式]](https://www.zhihu.com/equation?tex=c%3D3%2Cx%7B%28z%3C%3Dc%29%7D%3D%28x%7B1%7D%2Cx%7B3%7D%2Cx%7B5%7D%29)

待预测部分为 ![[公式]](https://www.zhihu.com/equation?tex=x%7B%28z%3Ec%29%7D%3D%28x%7B4%7D%2Cx%7B6%7D%2Cx%7B2%7D%29) 。对于 ![[公式]](https://www.zhihu.com/equation?tex=z%3Ec+) 部分，作者在待预测的tokens左边额外添加了mask-token ![[公式]](https://www.zhihu.com/equation?tex=M%28z%3Ec%29)，最终整个token的输入序列由三部分组成： ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B%28z%3C%3Dc%29%7D%2CM%28z%3Ec%29%2Cx%28z%3Ec%29%29%3D%28x%7B1%7D%2Cx%7B3%7D%2Cx%7B5%7D%2C%5BM%5D%2C%5BM%5D%2C%5BM%5D%2Cx%7B4%7D%2Cx%7B6%7D%2Cx%7B2%7D%29)

，[M]表示遮盖该token；对应的位置序列为： ![[公式]](https://www.zhihu.com/equation?tex=%28z%28%3C%3Dc%29%2Cz%28%3Ec%29%2Cz%28%3Ec%29%29%3D%28p1%2Cp3%2Cp5%2Cp4%2Cp6%2Cp2%2Cp4%2Cp6%2Cp2%29)。

3个[M]和对应位置position-embedding的加入，就是位置补偿。**例如在序列 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B1%7D%2Cx%7B3%7D%2Cx%7B5%7D%2C%5BM%5D%2C%5BM%5D%2C%5BM%5D%2Cx%7B4%7D%2Cx%7B6%7D%2Cx%7B2%7D%29) 中预测 ![[公式]](https://www.zhihu.com/equation?tex=x%7B4%7D)时，不仅能看到 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B1%7D%2Cx%7B3%7D%2Cx%7B5%7D%29) 的token-embedding，还能看到 ![[公式]](https://www.zhihu.com/equation?tex=%28x%7B1%7D%2Cx%7B3%7D%2Cx%7B5%7D%2Cx%7B4%7D%2Cx%7B6%7D%2Cx%7B2%7D%29) 的position-embedding**；依次递归预测![[公式]](https://www.zhihu.com/equation?tex=%28x%7B6%7D%2Cx%7B2%7D%29) 。

![img](https://pic4.zhimg.com/80/v2-e678455c2d2545ffdb5056a550c0f5f7_720w.jpg)

### 3.3 MPNet优势

MPNet使用**自回归编码**，避免了BERT做Mask时可能丢失被Mask的token的彼此关联信息和pretrain（有mask）、finetune（无mask）不一致的问题；通过位置补偿，又解决了XLNet无法看到全局位置信息的缺陷。取其精华，确实是挺巧妙的一种思路。



![img](https://pic1.zhimg.com/80/v2-ecb312d640de154ae5713dee35617238_720w.jpg)

观察输入信息的占比，MPNet输入的信息量是最大的；从直观上理解，模型每次可以接受到更多的文本特征，从而容易训练出更优结果。

### 3.4 SOTA结果

作者在权威的语义理解评估数据集GLUE上的实验结果表面，MPNet确实比它的前辈BERT和XLNet略胜一筹。另外，作者表示MPNet在训练时加入了全词掩码whole word mask以及相对位置编码等已被证明有效的trick，加上和RoBERTa训练一样的160GB训练语料，取得这样的结果应该说是情理之中了。

![img](https://pic4.zhimg.com/80/v2-799de6714ada5fc56bc0b1fae5ece91b_720w.jpg)

末尾的消融实验，可以看到位置补偿和PLM对实验结果的提升都很关键。

![img](https://pic4.zhimg.com/80/v2-b10d12a2cf3a71e78e168c1408e93dc7_720w.jpg)

## 4.NLP预训练模型趋势跟踪

从目前来看，大规模语料预训练+finetune的方式，应该会是NLP接下去几年的主流。各种基于语言模型的改进也是层出不穷。虽然玩法种类各异，我们还是可以瞥见一些具有突破性的方向。

### 4.1 土豪系列 - T5、GPT3、MegatronLM

![img](https://pic4.zhimg.com/80/v2-00cb8ccf43c77d69e7fd09c6f732e793_720w.jpg)

前期BERT到RoBERTa，GPT到GPT2效果的提升，已经证明更多数据可以跑出更强大更通用的预训练模型。去年底到今年，英伟达、谷歌、Open-AI相继放出巨无霸模型MegatronLM（83亿参数）、T5（110亿）、GPT3（1500亿），不断刷榜令人咋舌的同时也彰显了巨头们的实力。

相信未来，巨无霸模型依然会成为大公司的研究目标之一，却让普通科研人员可望不可及。

### 4.2 小而美系列 - DistillBERT、TinyBERT、FastBERT

没有前排巨头们的经济实力，普通公司和科研机构沿着相反赛道-模型轻量化下足了功夫。如何在尽可能少的参数量下，取得和大模型接近的效果，同时训练/预测速度翻倍，是很实际很有价值的课题。

这其中，有代表性的工作如华为诺亚方舟实验室发布的TinyBERT、北大的FastBERT都取得了瞩目的效果。例如FastBERT在BERT的每一层都接入一个分类器，通过样本自适应机制自动调整每个样本的计算量（容易的样本通过一两层就可以预测出来，较难的样本则需要走完全程）。

![img](https://pic4.zhimg.com/80/v2-5f78019db957ce55bc1628169d1f5907_720w.jpg)

图中“Speed”代表不确定性的阈值，和推理速度成正比。在Speed=0.2时，FastBERT速度可以提升1-10倍，且精度下降全部在0.11个点之内。

除了知识蒸馏，常规的模型轻量化一般包含层数裁剪、精度量化等手段。

### 4.3 潜力股系列 - few shot learning

在实际业务场景中，对于中小AI企业往往容易出现数据量不足的问题。例如用户需要订制一个FAQ问答机器人，有100个标准问，但表示每个问句只有2-3条同义句...

![img](https://pic3.zhimg.com/80/v2-052167ba5e51edc8b1309cffa122cdc2_720w.png)

战略上，“客户就是上帝“的精神激励我们不能虚，要迎难而上。战术上，除了花高成本找标注团队造数据外，迁移学习、小样本学习可能会非常有帮助。受到人类具有快速从少量（单）样本中学习能力的启发（例如生活在北方的人可能没有见过榴莲，一旦看过一次榴莲的照片，就认识了！），让模型在少量样本中学习获得有力的泛化能力，成为近年的研究热点之一。

感兴趣的同学可以参考阿里的这篇paper：Few-Shot Text Classification with Induction Network。

## 5.附录-快速上手BERT的4大工具包

预训练语言模型的代表BERT，已经成为NLP领域的重要工具，不同机构/个人也分别开发了轻松使用BERT的工具包。笔者结合自身经验，简单概括了一下：

### 5.1 肖涵 - bert-as-service

顾名思义，将BERT模型直接封装成一个服务，堪称上手最快的BERT工具。作者是xxx肖涵博士。

![img](https://pic1.zhimg.com/80/v2-45573088e817d93b1c13d1dee7e6b058_720w.jpg)

按照GIthub上的教程，下载BERT权重并安装工具包，三行代码即可轻松使用BERT获得文本的向量特征，完成下游NLP各项任务。bert-as-service是跨平台的服务，不受限于OS、深度学习框架，且作者对于并发做了大量优化与加速，可以满足日常实验甚至公司的实际业务需求。

### 5.2 Google - BERT源码

BERT源码官方仓库，可以学习BERT各模块的底层实现细节。Google开源了权重的同时，也开源了预训练、子任务微调的脚本，是学习BERT不可略过的学习教程。代码基于tensorflow，对TF熟练的同学会更快上手。

![img](https://pic2.zhimg.com/80/v2-e2773bad811c2d56ad854c89be26f7a5_720w.jpg)

当前，仓库中还发布了2/4/6/8..层不同大小的BERT，以缓解BERT资源开销大、inference缓慢带来的问题。中文BERT可以参考哈工大崔一鸣、实在智能徐亮等开源的权重。

### 5.3 huggingface - transformers

有了TF版，pytorch怎甘落后。机构huggingface开发的transformers工具包，堪称预训练模型大礼包，囊括了10几种火热模型。

![img](https://pic3.zhimg.com/80/v2-1ee2c191e11c0fbef21c068d2c77e57e_720w.jpg)

种类齐全且api接口实现统一、调用简单，是pytorch框架与BERT的最佳组合。transformers的src源码也是学习BERT等模型原理的绝佳资料。

### 5.4 苏剑林 - bert4keras

接下来自然而然该Keras出场了！作为tf2.0的官方高阶api，Keras的简洁特性始终拥有超高人气。

![img](https://pic1.zhimg.com/80/v2-410c4ffe9be444991b7af509a22331ec_720w.jpg)

来自追一科技的苏剑林，在业余时间自己实现了bert4keras框架，且提供了详细教程、众多下游任务微调脚本（分类、文本生成、QA、图片标题生成等）。始终走在BERT任务的前沿。

除以上工具包，github上还有众多用户开源的BERT相关工具，按需参考使用即可。

## Reference

[1] Devlin J, Chang M W, Lee K, et al. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding[J]. arXiv preprint arXiv:1810.04805, 2018.

[2] Vaswani A, Shazeer N, Parmar N, et al. Attention is all you need [C]//Advances in Neural Information Processing Systems. 2017: 5998-6008.

[3]Zhilin Yang, Zihang Dai, Yiming, et.al. XLNet: Generalized Autoregressive Pretraining for Language Understanding[C]. arXiv preprint arXiv:1906.08237, 2019.

[4]Kaitao Song, Xu Tan, Tao Qin, Tie-Yan Liu, et.al. MPNet: Masked and Permuted Pre-training for Language Understanding [C]. arXiv preprint arXiv:2004.09297, 2020.

[5]Weijie Liu, PengZhou, QiJu, et.al. FastBERT: a Self-distilling BERT with Adaptive Inference Time[C]. arXiv preprint arXiv:2004.02178, 2020.

[6]张俊林 - XLNet:运行机制及和Bert的异同比较

[7]李如 - FastBERT：又快又稳的推理提速方法