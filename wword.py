# -*- coding: UTF-8 -*-
# @Author  : Mysticbinary
import src.tools as t

# 注意：要使用之前，先将这两个路径修改成你主机内的正确路径
newwordsname = '/Users/Mysticbinary/Document/code/wword/db/newwords.txt'
oldwordsname = '/Users/Mysticbinary/Document/code/wword/db/oldwords.txt'

count = 0
tempfilg = 1
while (tempfilg == 1):
    count = count + 1
    # 随机获取一行
    templine = t.getlinecontent(newwordsname)
    if templine == 0:
        tempfilg = 0
    else:
        # 分割
        linelist = templine.split(",")

        # get 键盘上的输入
        word = "\033[7;33m " + linelist[0].lstrip().rstrip() + " \033[0m"
        inputword = raw_input("😊 ‍请输入" + word + "的英文单词 : ")

        # 如果用 == 字符串对比不正确，考虑是否左右有空格
        if (inputword.lstrip().rstrip() == linelist[1].lstrip().rstrip()):
            print "🔰 恭喜！输入正确 : ", inputword.lstrip().rstrip(), " （提示：该单词已经从当前文本删除）"
            # 将输入正确的行移动到 oldwords
            t.moveoldfile(oldwordsname, templine)
            t.deleteline(newwordsname, templine)
        else:
            errorword = "\033[7;31m " + linelist[1].lstrip().rstrip() + " \033[0m"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "---------分割线，防止看到上面的正确输出-------"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "-"
            print "❌ 输入错误！正确单词为:" + errorword

        print "+--------------------------------------------------[当前练习次数：" + str(count) + "]"

print "提示：newwords.txt文本为空,程序结束！"
