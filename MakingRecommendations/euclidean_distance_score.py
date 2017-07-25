#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 8:45
# @Author  : ywendeng
# @Description : 使用欧式距离来计算两个用户之间对物品品味的相似性
from math import sqrt

critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


def sim_distance(prefs, person_a, person_b):
    # 遍历两个对象之间的共同拥有的爱好
    si = {}
    for item in prefs[person_a]:
        if item in prefs[person_b]:
            si[item] = 1
    # 两个对象之间没有任何相关性
    if len(si) == 0:
        return 0
    # 欧几里德计算距离,所有的平方差求和
    sim_of_object = sum([pow(prefs[person_a][item] - prefs[person_b][item], 2)
                         for item in prefs[person_a] if item in prefs[person_b]])
    # 格式化显示
    return 1 / (1 + sqrt(sim_of_object))


if __name__ == '__main__':
    s = sim_distance(critics, 'Lisa Rose', 'Claudia Puig')
    print s
