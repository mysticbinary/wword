# -*- coding: UTF-8 -*-
# @Author  : Mysticbinary
import os
import random


def printfont(str):
    process = os.popen(str)
    output = process.read()
    process.close()
    return output


# 在两数范围内取一个随机数
def getrandomnumber(minimum, max):
    r = random.randint(minimum, max)
    return r
