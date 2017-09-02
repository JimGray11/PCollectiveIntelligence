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
            data.append(map(int, p[1:-1]))
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
    return 1 - num / den


# 使用层次聚类
def hcluster(data_set, distance=pearson):
    # 使用一个map将两个点之间的距离计算一次之后就缓存起来
    distances = {}
    # 新形成的点id为负
    cluster_id = -1
    # 1.初始化每个点都作为一个簇
    clust = [bi_cluster(data_set[i], i) for i in range(len(data_set))]
    # 开始进行循环遍历进行层次聚类
    while len(clust) > 1:
        # 2.开始计算两个点之间的距离，并选择最小的两个点
        loest_pair = (0, 1)
        cloest = distance(clust[0].vec, clust[1].vec)
        distances[(clust[0].id, clust[1].id)] = cloest
        for i in range(len(clust)):
            for j in range(i + 1, len(clust)):
                if (clust[i].id, clust[j].id) not in distances:
                    # 如果两个点之间的距离不存在，则将两点之间的距离加入结合中
                    distances[(clust[i].id, clust[j].id)] = distance(clust[i].vec, clust[j].vec)
                d = distances[(clust[i].id, clust[j].id)]
                if d < cloest:
                    cloest = d
                    loest_pair = (i, j)
        # 3.更新簇的中心点
        center_ver = [(p1 + p2) / 2 for p1, p2 in zip(clust[loest_pair[0]].vec,
                                                      clust[loest_pair[1]].vec)]
        cluster_center = bi_cluster(center_ver, cluster_id,
                                    clust[loest_pair[0]], clust[loest_pair[1]], cloest)
        cluster_id -= 1
        # 4.并更新簇节点(删除聚类最近的两个节点,添加新的簇中心)
        # 注意由于下标的变化，需要先删除1，再删除0
        del clust[loest_pair[1]]
        del clust[loest_pair[0]]

        clust.append(cluster_center)
    return clust[0]


def roate_matrix(data_set):
    roate_data = []
    for i in range(len(data_set[0])):
        # 注意普通二维数组的遍历和numpy、DataFrame多维数组遍历的区别
        obj = [data_set[j][i] for j in range(len(data))]
        roate_data.append(obj)
    return roate_data


if __name__ == '__main__':
    columns, data, rows = read_file("data_set/blogdata.txt")
    hcluster(data)
    roate= roate_matrix(data)
