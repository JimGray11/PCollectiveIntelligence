#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/2 21:29
# @Author  : ywendeng
# @Description : k-means 聚类算法
from h_clustering import *
import random


def k_cluster(data_set, k=3, distance=pearson):
    # 找到每个属性列的最大值
    columns_min_max = [(min(row[i] for row in data_set), max(row[i] for row in data_set))
                       for i in range(len(data_set[0]))]
    # 随机初始化K个聚类中心点
    clusters = [[random.random() * (columns_min_max[i][1] - columns_min_max[i][0]) + columns_min_max[i][0]
                 for i in range(len(data_set[0]))] for j in range(k)]
    # 开始进行聚类
    last_match = 0
    for t in range(100):
        print "Iteration %d " % t
        best_match = [[] for i in range(k)]
        # 计算每个样本点距离那个k中心点最近

        for j in range(len(data_set)):
            row = data_set[j]
            best = 0
            dst = distance(row, clusters[0])
            for i in range(1, k):
                if dst > distance(row, clusters[i]):
                    dst = distance
                    best = i
            best_match[best].append(j)
        # 如果提前收敛,则退出循环
        if last_match == best_match: break
        last_match = best_match
        # 更新每个簇的聚类中心
        for i in range(k):
            avg = [0.0] * len(data_set[0])
            if len(best_match[i]) > 0:
                for row_id in best_match[i]:
                    for k in range(len(data_set[row_id])):
                        # 对list中的值进行更新
                        avg[k] += data_set[row_id][k]
                for m in range(len(avg)):
                    avg[m] /= len(best_match[i])
            clusters[i] = avg
        return best_match


if __name__ == '__main__':
    clumns, data, rows = read_file("data_set/blogdata.txt")
    print k_cluster(data)
