# -*- coding: UTF-8 -*-
# @Author  : Mysticbinary
import random


def getlinescreate(filename):
    # 如果文件没有创建 就创建一个，但是用'a'模式读文本，指针会跳到最后，就会读取到0行
    fa = open(filename, 'a')
    fa.close()

    f = open(filename, 'r')
    flist = f.readlines()
    f.close()
    return flist.__len__()


def getlines(filename):
    f = open(filename, 'r')
    flist = f.readlines()

    return flist.__len__()


# 在file行数范围内取一个随机数
def getrandomnumbers(filenmae):
    # 先判断文本是否为空
    linenumber = getlines(filenmae)
    if linenumber == 0:
        return 0
    else:
        return random.randint(1, linenumber)


# line content
def getlinecontent(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        r = getrandomnumbers(filename)
        if (lines == 0):
            return 0
        else:
            return lines[r-1]


# writer a+
def moveoldfile(olefile, str1):
    with open(olefile, mode="a+") as f_w:
        f_w.write(str(str1.lstrip().rstrip()) + '\n')


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


def writerlist(path, list):
    f = open(path, "a+")
    for line in list:
        f.write(line)
    f.close()


# 覆盖写入
def coverwriter(name, str):
    f = open(name, "w")
    f.write(str)
    f.close()


# 读文本内的内容
def readallcontent(name):
    f = open(name, "r")
    a = f.read()
    f.close()
    return a
