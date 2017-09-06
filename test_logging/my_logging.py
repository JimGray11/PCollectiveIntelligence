#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/6 15:55
# @Author  : ywendeng
# @Description : 主要使用logging日志控制输出的使用,修改不同的日志级别显示不同的信息
import logging
import sys
import time
# # 使用basicConfig 来设置logging 日志输出信息
logging.basicConfig(
    # 输入可变的命名参数
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=time.strftime("%Y%m%d%H%M")+".log",
    filemode='w'
)
# 定义一个StreamHandler,将日志打印到日志文件的同时输出到控制台
logger = logging.getLogger("LOGGING")
fmt = logging.Formatter('%(name)-8s:%(levelname)-4s %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(fmt)
logger.addHandler(console_handler)


if __name__ == '__main__':
    logger.info("call main function ")
    try:
        logger.debug("try.....except may exist error ")
        a = 1 / 0
    except Exception as e:
        logger.error("除法存在异常错误: %s", e.args[0])
