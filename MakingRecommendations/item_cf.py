#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 9:16
# @Author  : ywendeng
# @Description :  基于Item的协同过滤

# 将基于user的协同过滤数据集转换为基于item的数据集
import recommendations_data as rd
import user_cf as ucf


def transformPrefs(prefs):
    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # 实现用户和item的位置互换
            result[item][person] = prefs[person][item]
    return result


# 预先计算货物之间的相似性
def calculate_similar_items(prefs, n=10):
    result = {}
    items_pref = transformPrefs(prefs)
    c = 0
    for item in items_pref:
        # 动态显示大数据集的状态
        c += 1
        if c % 100 == 0: print "%d/%d" % (c, len(items_pref))
        score = ucf.top_Matchs(items_pref, item, n)
        # 返回和货物最为相似的物品
        result[item] = score
    return result


# 现在可以不遍历整个数据的情况下，利用反应物品相似度的字典来给出推荐了
def recommender_item_cf(prefs, item_match, user):
    user_rating = prefs[user]
    score = {}
    total_sim = {}
    # 遍历用户购买过的商品
    for item, rating in user_rating.items():
        # 遍历和用户购买过最相似的商品----使用item_match实现了商品相似的预计算
        for similar, item2 in item_match[item]:
            # 如果该商品用户已经购买则需要加权处理
            if item2 in user_rating: continue
            score.setdefault(item2, 0)
            score[item2] += float(similar) * rating
            total_sim.setdefault(item2, 0)
            total_sim[item2] += similar
    # 计算加权相似度
    ranking = [(score / total_sim[item], item) for item,score in score.items()]
    ranking.sort()
    ranking.reverse()
    return ranking


if __name__ == '__main__':
    # 返回相似度最高的商品列表
    result = calculate_similar_items(rd.critics)
    print recommender_item_cf(rd.critics,result,'Toby')
