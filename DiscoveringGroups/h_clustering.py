#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 21:42
# @Author  : ywendeng
# @Description : 使用二叉树构建层次聚类
'''
 该类主要用于保存节点结构
'''
from math import sqrt


class bi_cluster(object):
    def __init__(self, vec, id, left=None, right=None, distance=None):
        # distance 用于保存两个簇之间的相似度
        self.vec = vec
        self.id = id
        self.left = left
        self.right = right
        self.distance = distance


def read_file(file_name):
    columns_name = []
    rows_name = []
    data = []
    with open(file_name, 'r') as fr:
        columns_name.extend(fr.readline().split("\t"))
        line = fr.readline()
        while line:
            p = line.split("\t")
            rows_name.append(p[0])
            data.append(map(int,p[1:-1]))
            line = fr.readline()
    return columns_name, data, rows_name


# 基于userItem来计算两个用户博客之间的相似性
def pearson(v1, v2):
    # 皮尔逊相关系数显示的是两个对象之间的变化趋势，能够解决"夸大分值"的情况
    # 简单求和
    sum1 = sum(v1)
    sum2 = sum(v2)
    # 乘积求和
    psum = sum([v1[i] * v2[i] for i in range(len(v1))])
    sum1Sq = sum([val * val for val in v1])
    sum2Sq = sum([val * val for val in v2])
    num = psum - (sum1 * sum2) / len(v1)
    den = sqrt((sum1Sq - pow(sum1, 2) / len(v1)) * (sum2Sq - pow(sum2, 2) / len(v1)))
    if den == 0:
        return 0
    return 1-num / den


if __name__ == '__main__':
    columns, data, rows = read_file("data_set/blogdata.txt")

     pearson(data[1], data[2])
