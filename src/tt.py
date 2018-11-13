# -*- coding: UTF-8 -*-
# @Author  : Mysticbinary
import os

import src.tool.tools as t
import src.tool.fileoperation as ft
import src.tool.diroperation as dt

# f = open("/Users/Mysticbinary/Document/code/wword/db/kindslibrary/wordgroup.txt", "r")
# f2 = open("/Users/Mysticbinary/Document/code/wword/db/kindslibrary/wordgroup-1.txt", "r")
# f1list = f.readlines()
# f2list = f2.readlines()
#
# for f2line in f2list:
#     if f2line in f1list:
#         pass
#     else:
#         print f2line

regulartxt = '/Users/Mysticbinary/Document/code/wword/db/underwaylibrary/regular.txt'
fontstylepath='/Users/Mysticbinary/Document/code/wword/src/initfiles/fontstyle.txt'

ff = open(fontstylepath, "r")
fflist = ff.readlines()
ff.close()
rfont = t.getrandomnumber(1, 4)

a = fflist[rfont-1]
b = a.replace("\n","")+" aaa"
print b

# outprint = t.printfont("toilet -f mono12 -F crop aaa")
process = os.popen(b)
output1 = process.read()
process.close()
print output1