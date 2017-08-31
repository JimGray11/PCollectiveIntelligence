#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 21:27
# @Author  : ywendeng
# @Description : 基于user_cf的方法协同过滤推荐
# 构建用户电影评分数据集
import user_cf as userCF


def load_user_movies_data(root_path):
    moives = {}
    mread = open(root_path + "u.item")
    for m in mread:
        id, movie_name = m.split("|")[0:2]
        moives[id] = movie_name
    mread.close()
    user_scores = {}
    iread = open(root_path + "u.data")
    for line in iread:
        user_id, movive_id, score, times = line.split("\t")
        # 如果用户则对其进行初始化
        user_scores.setdefault(user_id, {})
        user_scores[user_id][moives[movive_id]] = int(score)
    iread.close()
    return user_scores


if __name__ == '__main__':
    data = load_user_movies_data("../MakingRecommendations/data_set/")
    rec=userCF.recommender_user_cf(data,'37',5)
    print rec
