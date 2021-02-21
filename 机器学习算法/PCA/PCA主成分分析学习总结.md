# PCA主成分分析学习总结

![PCA主成分分析学习总结](https://pic1.zhimg.com/v2-db0c770d8dd55e5a433b6306d7085bf3_1440w.jpg?source=172ae18b)

> 作者：鱼遇雨欲语与余
>
> 原文链接：*https://zhuanlan.zhihu.com/p/32412043*

大概主成分分析（Principal components analysis，以下简称PCA）是最重要的降维方法之一。在数据压缩消除冗余和数据噪音消除等领域都有广泛的应用。一般我们提到降维最容易想到的算法就是PCA，下面我们就对PCA的原理做一个总结。

首先考虑一个问题：对于正交属性空间中的样本点，如何用一个超平面（直线的高维推广）对所有样本进行恰当的表达？

可以想到，若存在这样的超平面，那么它大概具有这样的性质：

- 最近重构性：样本点到这个超平面的距离足够近
- 最大可分性：样本点在这个超平面上的投影能尽可能的分开

基于最近重构性和最大可分性能分别得到主成分分析的两种等价推到，我们这里主要考虑最大可分性，并且一步一步推到出最终PCA。

## **1.PCA最大可分性的思想**

PCA顾名思义，就是找出数据里最主要的方面，用数据里最主要的方面来代替原始数据。具体的，假如我们的数据集是 ![[公式]](https://www.zhihu.com/equation?tex=n)维的，共有 ![[公式]](https://www.zhihu.com/equation?tex=m) 个数据 ![[公式]](https://www.zhihu.com/equation?tex=%28x_%7B1%7D%2Cx_%7B2%7D%2C...%2Cx_%7Bm%7D%29) 。我们希望将这 ![[公式]](https://www.zhihu.com/equation?tex=m) 个数据的维度从 ![[公式]](https://www.zhihu.com/equation?tex=n) 维降到 ![[公式]](https://www.zhihu.com/equation?tex=n%27) 维，希望这 ![[公式]](https://www.zhihu.com/equation?tex=m) 个 ![[公式]](https://www.zhihu.com/equation?tex=n%27) 维的数据集尽可能的代表原始数据集。我们知道数据从 ![[公式]](https://www.zhihu.com/equation?tex=n) 维降到 ![[公式]](https://www.zhihu.com/equation?tex=n%27+) 维肯定会有损失，但是我们希望损失尽可能的小。那么如何让这 ![[公式]](https://www.zhihu.com/equation?tex=n%27) 维的数据尽可能表示原来的数据呢？

我们先看看最简单的情况，也就是 ![[公式]](https://www.zhihu.com/equation?tex=n%3D2) ， ![[公式]](https://www.zhihu.com/equation?tex=n%27%3D1) ,也就是将数据从二维降维到一维。数据如下图。我们希望找到某一个维度方向，它可以代表这两个维度的数据。图中列了两个向量方向， ![[公式]](https://www.zhihu.com/equation?tex=u_1) 和 ![[公式]](https://www.zhihu.com/equation?tex=u_2) ，那么哪个向量可以更好的代表原始数据集呢？

![img](https://pic4.zhimg.com/80/v2-3b1f88a3e08562457a4d8e57094786cb_720w.jpg)

从直观上也可以看出， ![[公式]](https://www.zhihu.com/equation?tex=u_1) 比 ![[公式]](https://www.zhihu.com/equation?tex=u_2) 好，这就是我们所说的**最大可分性。**

## **2.基变换**

一般来说，欲获得原始数据新的表示空间，最简单的是对原始数据进行线性变换（基变换）：

![[公式]](https://www.zhihu.com/equation?tex=Y%3DPX)

其中 ![[公式]](https://www.zhihu.com/equation?tex=Y) 是样本在新空间的表达， ![[公式]](https://www.zhihu.com/equation?tex=P) 是基向量， ![[公式]](https://www.zhihu.com/equation?tex=X) 是原始样本。我们可知选择不同的基可以对一组数据给出不同的表示，同时当基的数量少于原始样本本身的维数则可达到降维的效果，矩阵表示如下：

![[公式]](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+p_1+%5C%5C+p_2+%5C%5C+%5Cvdots+%5C%5C+p_R+%5Cend%7Bpmatrix%7D+%5Cbegin%7Bpmatrix%7D+a_1+%26+a_2+%26+%5Ccdots+%26+a_M+%5Cend%7Bpmatrix%7D+%3D+%5Cbegin%7Bpmatrix%7D+p_1a_1+%26+p_1a_2+%26+%5Ccdots+%26+p_1a_M+%5C%5C+p_2a_1+%26+p_2a_2+%26+%5Ccdots+%26+p_2a_M+%5C%5C+%5Cvdots+%26+%5Cvdots+%26+%5Cddots+%26+%5Cvdots+%5C%5C+p_Ra_1+%26+p_Ra_2+%26+%5Ccdots+%26+p_Ra_M+%5Cend%7Bpmatrix%7D)

其中![[公式]](https://www.zhihu.com/equation?tex=p_i%5Cin%5C%7Bp_1%2Cp_2%2C...%2Cp_R%5C%7D)， ![[公式]](https://www.zhihu.com/equation?tex=p_i%5Cin%5Cmathbb%7BR%7D%5E%7B1%2AN%7D) 是一个行向量，表示第![[公式]](https://www.zhihu.com/equation?tex=i)个基；![[公式]](https://www.zhihu.com/equation?tex=a_j%5Cin%5C%7Ba_1%2Ca_2%2C...a_M%5C%7D)， ![[公式]](https://www.zhihu.com/equation?tex=a_i%5Cin%5Cmathbb%7BR%7D%5E%7BN%2A1%7D) 是一个列向量，表示第![[公式]](https://www.zhihu.com/equation?tex=j)个原始数据记录。特别要注意的是，这里 ![[公式]](https://www.zhihu.com/equation?tex=R) 可以小于 ![[公式]](https://www.zhihu.com/equation?tex=N) ，而 ![[公式]](https://www.zhihu.com/equation?tex=R) 决定了变换后数据的维数。也就是说，我们可以将一个 ![[公式]](https://www.zhihu.com/equation?tex=N) 维数据变换到更低维度的空间中去，变换后的维度取决于基的数量。**从原本 ![[公式]](https://www.zhihu.com/equation?tex=X%5Cin%5Cmathbb%7BR%7D%5E%7BN%2AM%7D) 降维到 ![[公式]](https://www.zhihu.com/equation?tex=Y%5Cin%5Cmathbb%7BR%7D%5E%7BR%2AM%7D) 。**因此这种矩阵相乘的表示也可以表示降维变换。

最后，上述分析同时给矩阵相乘找到了一种物理解释：两个矩阵相乘的意义是将右边矩阵中的每一列列向量变换到左边矩阵中每一行行向量为基所表示的空间中去。更抽象的说，一个矩阵可以表示一种线性变换。很多同学在学线性代数时对矩阵相乘的方法感到奇怪，但是如果明白了矩阵相乘的物理意义，其合理性就一目了然了。

## **3.方差**

那么考虑，如何选择一个方向或 者基才是最优的？观察下图

![img](https://pic2.zhimg.com/80/v2-a0247d797bf9a62b2b57bc6c169bb3a9_720w.jpg)周志华《机器学习》插图

我们将所有的点分别向两条直线做投影，基于前面PCA最大可分思想，我们要找的方向是降维后损失最小，可以理解为投影后的数据尽可能的分开，那么这种分散程度可以用数学上的方差来表示，方差越大数据越分散。方差公式如下：

![[公式]](https://www.zhihu.com/equation?tex=Var%28a%29+%3D+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7B%7B%28a_i-%5Cmu%29%7D%5E2%7D)

对数据进行了中心化后（可以方便后面的操作）：

![[公式]](https://www.zhihu.com/equation?tex=Var%28a%29+%3D+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7B%7Ba_i%7D%5E2%7D)

现在我们已经知道了以下几点：

- 对原始样本进行（线性变换）基变换可以对原始样本给出不同的表示
- 基的维度小于数据的维度可以起到降维的效果
- 对基变换后新的样本求其方差，选取使其方差最大的基

那么在下面我们来考虑一个新的问题

上面我们导出了优化目标，但是这个目标似乎不能直接作为操作指南（或者说算法），因为它只说要什么，但根本没有说怎么做。所以我们要继续在数学上研究计算方案。

## **4.协方差**

从二维降到一维可以使用方差最大来选出能使基变换后数据分散最大的方向（基），但如果遇到高维的变换，当完成第一个方向（基）选择后，第二个投影方向应该与第一个“几乎重合在一起”，这显然是没有用的，因此要有其它的约束条件。我们希望两个字段尽可能表示更多的信息，使其不存在相关性。

数学上用协方差表示其相关性：

![[公式]](https://www.zhihu.com/equation?tex=Cov%28a%2Cb%29+%3D+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7Da_i+b_i)

当![[公式]](https://www.zhihu.com/equation?tex=Cov%28a%2Cb%29%3D0) 时，表示两个字段完全独立，这也是我们的优化目标。

## **5.协方差矩阵**

我们想达到的目标与字段内方差及字段间协方差有密切关系，假如只有 ![[公式]](https://www.zhihu.com/equation?tex=a) 、 ![[公式]](https://www.zhihu.com/equation?tex=b) 两个字段，那么我们将它们按行组成矩阵 ![[公式]](https://www.zhihu.com/equation?tex=X) ,表示如下：

![[公式]](https://www.zhihu.com/equation?tex=X%3D%5Cleft%28+%5Cbegin%7Bmatrix%7D+a_1%26a_2%26...%26a_m%5C%5C+b_1%26b_2%26...%26b_m%5C%5C+%5Cend%7Bmatrix%7D%5Cright%29)

然后我们用 ![[公式]](https://www.zhihu.com/equation?tex=X) 乘以 ![[公式]](https://www.zhihu.com/equation?tex=X) 的转置，并乘上系数 ![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7Bm%7D) :

![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7Bm%7DXX%5E%5Ctop%3D%5Cleft%28+%5Cbegin%7Bmatrix%7D+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Ba_i%5E2%7D%26%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Ba_i+b_i%7D%5C%5C+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Ba_i+b_i%7D%26%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Bb_i+%5E2%7D%5C%5C+%5Cend%7Bmatrix%7D%5Cright%29)

可见，协方差矩阵是一个对称的矩阵，而且对角线是各个维度的方差，而其它元素是 ![[公式]](https://www.zhihu.com/equation?tex=a) 和 ![[公式]](https://www.zhihu.com/equation?tex=b) 的协方差，然后会发现两者被统一到了一个矩阵的。

## **6.协方差矩阵对角化**

我们的目标是使 ![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7Da_i+b_i+%3D+0) ，根据上述推倒，可以看出我们的优化目标 ![[公式]](https://www.zhihu.com/equation?tex=C%3D%5Cfrac%7B1%7D%7Bm%7DXX%5E%5Ctop) 等价于协方差矩阵对角化。即除对角线外的其它元素（ 如![[公式]](https://www.zhihu.com/equation?tex=+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7Da_i+b_i) ）化为0，并且在对角线上将元素按大小从上到下排列，这样我们就达到了优化目的。这样说可能还不是很明晰，我们进一步看下原矩阵与基变换后矩阵协方差矩阵的关系：

设原始数据矩阵 ![[公式]](https://www.zhihu.com/equation?tex=X) 对应的协方差矩阵为 ![[公式]](https://www.zhihu.com/equation?tex=C) ，而 ![[公式]](https://www.zhihu.com/equation?tex=P) 是一组基按行组成的矩阵，设 ![[公式]](https://www.zhihu.com/equation?tex=Y%3DPX) ，则 ![[公式]](https://www.zhihu.com/equation?tex=Y) 为 ![[公式]](https://www.zhihu.com/equation?tex=X) 对 ![[公式]](https://www.zhihu.com/equation?tex=P) 做基变换后的数据。设 ![[公式]](https://www.zhihu.com/equation?tex=Y) 的协方差矩阵为 ![[公式]](https://www.zhihu.com/equation?tex=D) ，我们推导一下 ![[公式]](https://www.zhihu.com/equation?tex=D) 与 ![[公式]](https://www.zhihu.com/equation?tex=C) 的关系：

![[公式]](https://www.zhihu.com/equation?tex=D+%3D+%5Cfrac%7B1%7D%7Bm%7DYY%5E%5Ctop+)

![[公式]](https://www.zhihu.com/equation?tex=+%3D%5Cfrac%7B1%7D%7Bm%7D%28PX%29%28PX%29%5E%5Ctop)

![[公式]](https://www.zhihu.com/equation?tex=%3D+%5Cfrac%7B1%7D%7Bm%7DPX+X%5E%5Ctop+P%5E%5Ctop)

![[公式]](https://www.zhihu.com/equation?tex=%3D+P%28%5Cfrac%7B1%7D%7Bm%7DX+X%5E%5Ctop%29+P%5E%5Ctop)

![[公式]](https://www.zhihu.com/equation?tex=%3DPCP%5E%5Ctop)

![[公式]](https://www.zhihu.com/equation?tex=%3DP%5Cleft%28+%5Cbegin%7Bmatrix%7D+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Ba_i%5E2%7D%26%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Ba_i+b_i%7D%5C%5C+%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Ba_i+b_i%7D%26%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bi%3D1%7D%5E%7Bm%7D%7Bb_i+%5E2%7D%5C%5C+%5Cend%7Bmatrix%7D%5Cright%29P%5E%5Ctop)

可见，我们要找的 ![[公式]](https://www.zhihu.com/equation?tex=P) 不是别的，而是能让原始协方差矩阵对角化的 ![[公式]](https://www.zhihu.com/equation?tex=P) 。换句话说，优化目标变成了寻找一个矩阵 ![[公式]](https://www.zhihu.com/equation?tex=P) ，满足![[公式]](https://www.zhihu.com/equation?tex=PCP%5E%5Cmathsf%7BT%7D)是一个对角矩阵，并且对角元素按从大到小依次排列，那么 ![[公式]](https://www.zhihu.com/equation?tex=P) 的前 ![[公式]](https://www.zhihu.com/equation?tex=K) 行就是要寻找的基，用 ![[公式]](https://www.zhihu.com/equation?tex=P) 的前 ![[公式]](https://www.zhihu.com/equation?tex=K) 行组成的矩阵乘以 ![[公式]](https://www.zhihu.com/equation?tex=X) 就使得 ![[公式]](https://www.zhihu.com/equation?tex=X) 从 ![[公式]](https://www.zhihu.com/equation?tex=N) 维降到了 ![[公式]](https://www.zhihu.com/equation?tex=K) 维并满足上述优化条件。

我们希望的是投影后的方差最大化，于是我们的优化目标可以写为：

![[公式]](https://www.zhihu.com/equation?tex=%5Cmax_%7BP%7D%5C+tr%28PCP%5E%5Ctop%29)

![[公式]](https://www.zhihu.com/equation?tex=s.t.+%5C+%5C+PP%5E%5Ctop%3DI)

利用拉格朗日函数可以得到:

![[公式]](https://www.zhihu.com/equation?tex=J%28P%29%3Dtr%28PCP%5E%5Ctop%29%2B%5Clambda%28PP%5E%5Ctop-I%29)

对 ![[公式]](https://www.zhihu.com/equation?tex=P) 求导有 ![[公式]](https://www.zhihu.com/equation?tex=CP%5E%5Ctop%2B%5Clambda+P%5E%5Ctop+%3D+0) ，整理下即为：

![[公式]](https://www.zhihu.com/equation?tex=CP%5E%5Ctop%3D%EF%BC%88-%5Clambda%EF%BC%89+P%5E%5Ctop+)

于是，只需对协方差矩阵 ![[公式]](https://www.zhihu.com/equation?tex=C) 进行特征分解，对求得的特征值进行排序，再对 ![[公式]](https://www.zhihu.com/equation?tex=P%5E%5Ctop%3D%EF%BC%88P_1%2C+P_2%2C...%2CP_R%EF%BC%89) 取前 ![[公式]](https://www.zhihu.com/equation?tex=K) 列组成的矩阵乘以原始数据矩阵X，就得到了我们需要的降维后的数据矩阵Y。

## **7.PCA算法流程**

从上面两节我们可以看出，求样本 ![[公式]](https://www.zhihu.com/equation?tex=x_i) 的 ![[公式]](https://www.zhihu.com/equation?tex=n%27) 维的主成分其实就是求样本集的协方差矩阵 ![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B1%7D%7Bm%7DXX%5E%5Ctop) 的前 ![[公式]](https://www.zhihu.com/equation?tex=n%27) 个特征值对应特征向量矩阵 ![[公式]](https://www.zhihu.com/equation?tex=P) ，然后对于每个样本 ![[公式]](https://www.zhihu.com/equation?tex=x_i) ,做如下变换 ![[公式]](https://www.zhihu.com/equation?tex=y_i%3DPx_i) ，即达到降维的PCA目的。

下面我们看看具体的算法流程：

输入： ![[公式]](https://www.zhihu.com/equation?tex=n) 维样本集 ![[公式]](https://www.zhihu.com/equation?tex=X%3D%28x_1%2Cx_2%2C...%2Cx_m%29) ，要降维到的维数 ![[公式]](https://www.zhihu.com/equation?tex=n%27) .

输出：降维后的样本集 ![[公式]](https://www.zhihu.com/equation?tex=Y)

1.对所有的样本进行中心化 ![[公式]](https://www.zhihu.com/equation?tex=x_i%3Dx_i-%5Cfrac%7B1%7D%7Bm%7D%5Csum_%7Bj%3D1%7D%5E%7Bm%7Dx_j)

2.计算样本的协方差矩阵![[公式]](https://www.zhihu.com/equation?tex=C%3D%5Cfrac%7B1%7D%7Bm%7DXX%5E%5Cmathsf%7BT%7D)

3.求出协方差矩阵的特征值及对应的特征向量

4.将特征向量按对应特征值大小从上到下按行排列成矩阵，取前k行组成矩阵P

5.Y=PX即为降维到k维后的数据

注意：

有时候，我们不指定降维后的 ![[公式]](https://www.zhihu.com/equation?tex=n%27) 的值，而是换种方式，指定一个降维到的主成分比重阈值 ![[公式]](https://www.zhihu.com/equation?tex=t) 。这个阈值t在 ![[公式]](https://www.zhihu.com/equation?tex=%280%2C1%5D) 之间。假如我们的 ![[公式]](https://www.zhihu.com/equation?tex=n) 个特征值为 ![[公式]](https://www.zhihu.com/equation?tex=%5Clambda_1%5Cgeq%5Clambda_2%5Cgeq...%5Cgeq%5Clambda_n) ,则n'可以通过下式得到:

![[公式]](https://www.zhihu.com/equation?tex=%5Cfrac%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%27%7D%5Clambda_i%7D%7B%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%5Clambda_i%7D%5Cgeq+t)

## **8.PCA算法总结**

这里对PCA算法做一个总结。作为一个非监督学习的降维方法，它只需要特征值分解，就可以对数据进行压缩，去噪。因此在实际场景应用很广泛。为了克服PCA的一些缺点，出现了很多PCA的变种，比如为解决非线性降维的KPCA，还有解决内存限制的增量PCA方法Incremental PCA，以及解决稀疏数据降维的PCA方法Sparse PCA等。

PCA算法的主要优点有：

- 仅仅需要以方差衡量信息量，不受数据集以外的因素影响。　
- 各主成分之间正交，可消除原始数据成分间的相互影响的因素。
- 计算方法简单，主要运算是特征值分解，易于实现。

PCA算法的主要缺点有：

- 主成分各个特征维度的含义具有一定的模糊性，不如原始样本特征的解释性强。
- 方差小的非主成分也可能含有对样本差异的重要信息，因降维丢弃可能对后续数据处理有影响。

## **继续阅读**

在PCA降维过程中，当进行协方差矩阵上求解特征值时，如果面对维度高达 ![[公式]](https://www.zhihu.com/equation?tex=10000%2A10000)，可想而知耗费的计算量程平方级增长。面对这样一个难点，从而引出奇异值分解(SVD)，利用SVD不仅可以解出PCA的解，而且无需大的计算量。

[Betten：奇异值分解(SVD)原理zhuanlan.zhihu.com![图标](https://pic1.zhimg.com/v2-7a6471cabd5b3fa5c015e57a176c7120_180x120.jpg)](https://zhuanlan.zhihu.com/p/32600280)



PCA（主成分分析）和LDA（线性判别分析）有很多的相似点，其本质是要将初始样本映射到维度更低的样本空间中，但是PCA和LDA的映射目标不一样：PCA是为了让映射后的样本具有最大的发散性；而LDA是为了让映射后的样本有最好的分类性能。所以说PCA是一种无监督的降维方法，而LDA是一种有监督的降维方法。

## **参考资料**

[Pattern Recognition and Machine Learning](https://link.zhihu.com/?target=https%3A//book.douban.com/subject/2061116/)

[《机器学习》](https://link.zhihu.com/?target=https%3A//www.baidu.com/link%3Furl%3Dfg7a3GQOzBYhIzRp1M-Xm3Xy3Uy6Xqay7eUWQuKxrBmmRqKpdXOQT6gVPDa1_dYxCTea6Og8qepBWJr4urKZv_%26wd%3D%26eqid%3Dd06943e90000caa3000000055a4f7607)

[主成分分析（Principal components analysis）-最大方差解释](https://link.zhihu.com/?target=http%3A//www.cnblogs.com/jerrylead/archive/2011/04/18/2020209.html)

[Betten：机器学习面试干货精讲zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/32877396)