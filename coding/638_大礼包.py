'''
题目描述：
在LeetCode商店中， 有许多在售的物品。

然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。

现给定每个物品的价格，每个大礼包包含物品的清单，以及待购物品清单。请输出确切完成待购清单的最低花费。

每个大礼包的由一个数组中的一组数据描述，最后一个数字代表大礼包的价格，其他数字分别表示内含的其他种类物品的数量。

任意大礼包可无限次购买。

示例 1:

输入: [2,5], [[3,0,5],[1,2,10]], [3,2]
输出: 14
解释: 
有A和B两种物品，价格分别为¥2和¥5。
大礼包1，你可以以¥5的价格购买3A和0B。
大礼包2， 你可以以¥10的价格购买1A和2B。
你需要购买3个A和2个B， 所以你付了¥10购买了1A和2B（大礼包2），以及¥4购买2A。
示例 2:

输入: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
输出: 11
解释: 
A，B，C的价格分别为¥2，¥3，¥4.
你可以用¥4购买1A和1B，也可以用¥9购买2A，2B和1C。
你需要买1A，2B和1C，所以你付了¥4买了1A和1B（大礼包1），以及¥3购买1B， ¥4购买1C。
你不可以购买超出待购清单的物品，尽管购买大礼包2更加便宜。
说明:

最多6种物品， 100种大礼包。
每种物品，你最多只需要购买6个。
你不可以购买超出待购清单的物品，即使更便宜。

解题思路：
方法一：递归，每次递归时，判断是使用购买礼包的方式还是使用原价，取更小值
方法二：记忆化搜索，在方法一的基础上，记录每个need对应的最低价格，直接返回，不用计算
'''
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        #记忆化搜索
        need_cost_map={}
        def getcostbyprice(needs,price):
            cost=0
            for ineed,price in zip(needs,price):
                cost+=ineed*price
            return cost
        def shopping(price,special,needs):
            #使用原价购买
            if str(needs) in need_cost_map.keys():
                return need_cost_map[str(needs)]
            res=getcostbyprice(needs,price) 
            if  sum(needs)==0:
                return 0
            #看礼包：
            for ispecial in special:
                isok=True
                newneed=[]
                new_cost=0
                for icontain,ineed in zip(ispecial[:-1],needs):
                    if icontain>ineed:
                        isok=False
                        break
                    newneed.append(ineed-icontain) 
                #当前礼包可以购买
                if isok:
                    res=min(res,ispecial[-1]+shopping(price,special,newneed))
                    need_cost_map[str(needs)]=res
            return res
                    
        return shopping(price,special,needs)


        #递归
        #注意：不可以购买超出待购清单的物品，即使更便宜。
        def getcostbyprice(needs,price):
            cost=0
            for ineed,price in zip(needs,price):
                cost+=ineed*price
            return cost
        def shopping(price,special,needs):
            #使用原价购买
            res=getcostbyprice(needs,price)
            if  sum(needs)==0:
                return 0
            #看礼包：
            for ispecial in special:
                isok=True
                newneed=[]
                new_cost=0
                for icontain,ineed in zip(ispecial[:-1],needs):
                    if icontain>ineed:
                        isok=False
                        break
                    newneed.append(ineed-icontain) 
                #当前礼包可以购买
                if isok:
                    res=min(res,ispecial[-1]+shopping(price,special,newneed))
            return res
                    
        return shopping(price,special,needs)





