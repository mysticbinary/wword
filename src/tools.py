# -*- coding: UTF-8 -*-
# @Author  : Mysticbinary
import random


# 先获取文本里的最大行数
def getlines(filename):
    file = open(filename, mode='r')
    lines = file.readlines()
    file.close()
    n = 0
    for line in lines:
        n = n + 1
    return n


# 在最大行数范围内取一个随机数
def getrandomnumbers(filenmae):
    # 先判断文本是否为空
    linenumber = getlines(filenmae)
    if linenumber == 0:
        return 0

    r = random.randint(1, getlines(filenmae))
    # print "当前随机数：", r
    return r


def getlinecontent(filename):
    with open(filename, mode="r") as f:
        lines = f.readlines()
        n = 0
        temp = getrandomnumbers(filename)
        if (temp == 0):
            return 0
        for line in lines:
            n = n + 1
            if (n == temp):
                return line


# 指定删除某行
def deleteline(newfile, str):
    with open(newfile, mode="r") as f:
        lines = f.readlines()
        # print(lines)
    with open(newfile, mode="w") as f_w:
        for line in lines:
            if str in line:
                continue
            f_w.write(line)


def moveoldfile(olefile, str1):
    with open(olefile, mode="a+") as f_w:
        f_w.write(str(str1.lstrip().rstrip()) + '\n')
