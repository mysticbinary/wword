# -*- coding: UTF-8 -*-
# @Author  : Mysticbinary
import os
import src.tool.tools as t


def getnumberoffolders(directorypath):
    dlist = os.listdir(directorypath)
    return int(dlist.__len__())


def getrandomfilename(directorypath):
    dlist = os.listdir(directorypath)
    r = t.getrandomnumber(0, int(dlist.__len__()) - 1)
    return dlist[r]


def getallfilename(directorypath):
    dlist = os.listdir(directorypath)
    # mac 文件操作异常会出现隐藏文件".DS_Store" 用命令清理： sudo find / -name ".DS_Store" -depth -exec rm {} \;
    newdlist = []
    for filenemem in dlist:
        xlist = filenemem.split(".")
        newdlist.append(xlist[0])
    return newdlist
