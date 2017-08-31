#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/4 9:27
# @Author  : ywendeng
# @Description : UserCF-基于用户的协同过滤

import sim_calculate_score as sc
from recommendations_data import critics


# 使用简单的最相似的推荐
def top_Matchs(prefs, person, n=5, similarity=sc.sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]
    scores.sort()
    scores.reverse()
    # 返回相似度最高的前五个商品
    return scores[:n]


# 基于userCF的协同过滤
def recommender_user_cf(prefs, person, topN, sim_function=sc.sim_pearson):
    # 声明一个变量保存加权评分之和
    totals = dict()
    sim_sums = dict()
    for other in prefs:
        if other == person: continue
        # 计算两个用户的相似度
        sim = sim_function(prefs, other, person)
        # 如果两个用户的相似度为零则直接返回
        if sim <= 0: continue
        # 找出person 和其他用户没有购买或者评分为零的商品
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item] == 0.0:
                totals.setdefault(item, 0)
                sim_sums.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim
                sim_sums[item] += sim
    all_score_item = [(totals[item] / sim_sums[item], item) for item in totals]
    all_score_item.sort(reverse=True)
    return all_score_item[:topN]


if __name__ == '__main__':
    s = recommender_user_cf(critics, 'Michael Phillips', sc.sim_pearson, 5)
    print s
