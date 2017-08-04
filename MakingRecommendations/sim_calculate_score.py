#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 8:45
# @Author  : ywendeng
# @Description : 计算不同用户偏好的相似性
from math import sqrt

'''
 使用欧几里德距离计算相似性
'''


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


'''
使用pearson 相关系数计算相似性
'''


def sim_pearson(prefs, p1, p2):
    # 找出两个人相同的item
    sim = [item for item in prefs[p1] if item in prefs[p2]]
    n = len(sim)
    # 没有相同的item则返回1
    if n == 0: return 1
    sum1 = sum([prefs[p1][item] for item in sim])
    sum2 = sum([prefs[p2][item] for item in sim])
    # 求解乘积之和
    psum = sum([prefs[p1][item] * prefs[p2][item] for item in sim])
    # 求解平方和
    psum1 = sum([pow(prefs[p1][item], 2) for item in sim])
    psum2 = sum([pow(prefs[p2][item], 2) for item in sim])
    # 计算协方差
    cov = psum - sum1 * sum2 / n
    # 计算两个用户相同item的标准差
    var = sqrt((psum1 - pow(sum1, 2) / n) * (psum2 - pow(sum2, 2) / n))
    if var == 0: return 0
    pearson = cov / var
    return pearson

