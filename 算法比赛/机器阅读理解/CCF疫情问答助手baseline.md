# CCF疫情问答助手baseline

### **比赛地址：**

*https://www.datafountain.cn/competitions/424/datasets*

### **开源地址：**

*https://github.com/AI-confused/COVID19_qa_baseline*

## 安装依赖

- pip install -r requirements.txt

## ES导入文档索引&数据预处理

- 为了在预测答案中用到检索功能，需要提前在服务器把ES搭建好，并把文档导入节点 https://blog.csdn.net/zjh_746140129/article/details/86483661
- 安装过程中可能遇到的报错 https://blog.csdn.net/feng12345zi/article/details/80367907
- 装好ES中文分词插件ik
- 在preprocess.sh中修改相应的参数，尤其是es索引的名字和ip，默认是passages和localhost
- bash preprocess.sh，这里默认的pandas读取train,passage,test的sep分别是\t , ,
- 如果不一致需要在preprocess.py的clean_data()做修改
- 清洗完后训练集会变成4995个，因为有5个样本的答案不在文档内

## 训练

- 将清洗好的训练集拆分为训练集和验证集，在train.sh中修改相应的参数
- bash train.sh
- 在eval后会在输出文件夹保存一个验证集预测文本和答案文本的对比文件eval_prediction.csv

## 测试

- 评测方法ROUGE-L链接 https://www.jianshu.com/p/2d7c3a1fcbe3
- 修改相应的参数
- bash test.sh
- 输出文件夹生成预测文件test_prediction.csv，用于提交

## 线上线下结果对比

| model         | lr   | max_seq_length | max_question_length | eval_score | test_score |
| ------------- | ---- | -------------- | ------------------- | ---------- | ---------- |
| bert-base-wwm | 1e-5 | 512            | 96                  | 0.7338     | 0.5458     |

[![Screen-Pictures/CCF%E7%96%AB%E6%83%85%E9%97%AE%E7%AD%94%E5%8A%A9%E6%89%8Bbaseline/2020-04-04_11-19-25_%E6%88%AA%E5%B1%8F2020-04-04%20%E4%B8%8A%E5%8D%8811.19.21.png](https://github.com/AI-confused/COVID19_qa_baseline/raw/master/Screen-Pictures/CCF%E7%96%AB%E6%83%85%E9%97%AE%E7%AD%94%E5%8A%A9%E6%89%8Bbaseline/2020-04-04_11-19-25_%E6%88%AA%E5%B1%8F2020-04-04%20%E4%B8%8A%E5%8D%8811.19.21.png)](https://github.com/AI-confused/COVID19_qa_baseline/blob/master/Screen-Pictures/CCF疫情问答助手baseline/2020-04-04_11-19-25_截屏2020-04-04 上午11.19.21.png) 预计用更大的预训练模型能提升几个点

## 处理流程简单说明

- 文档预处理使用句子组合的形式，在最大可容纳字长中包含连续的多个句子，考虑到答案是连续且完整的句子组合
- 在正负样本的选择中，选取了所有的正样本和随机一个负样本进行训练
- 训练过程使用多任务方式，同时预测答案是否在当前片段内以及答案的起始位置，这两个loss按照合适的权重相加
- 预测过程中，样本的每个token都会输出一个start&end的logit，各自选择logit最大的前k个，排列组合为备选span，然后计算span-score：startlogit+endlogit-cls_start-cls_end，按照spanscore对预测样本进行排序，选择分值最大的span最为最终答案
- 之后提分的思路可以从检索方面提高检索准确率，从重排序的分值计算方式和排序方式，以及多任务的训练方式上面提高单模的性能，使用更合适的预训练语言模型也能直接提升效果
- 有帮助的话，请点击右上角的star~

