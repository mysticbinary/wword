# -*- coding: UTF-8 -*-
# @Author  : Mysticbinary
import src.tool.tools as t
import src.tool.diroperation as dt
import src.tool.fileoperation as ft

# 注意：要使用之前，先将这3个路径修改成你主机内的正确路径
regulartxt = '/Users/Mysticbinary/Document/code/wword/db/underwaylibrary/regular.txt'
kindslibrarypath = '/Users/Mysticbinary/Document/code/wword/db/kindslibrary/'
underwaylibrarypath = '/Users/Mysticbinary/Document/code/wword/db/underwaylibrary/'
usermoneypath = '/Users/Mysticbinary/Document/code/wword/src/initfiles/usermoney.txt'
fontstylepath = '/Users/Mysticbinary/Document/code/wword/src/initfiles/fontstyle.txt'


def createfile(dirpath, underwaypath):

    dirlist = dt.getallfilename(dirpath)

    for filename in dirlist:

        f1 = open(underwaypath + filename + "-" + "cache.txt", "a")
        f1.close()
        for i in range(1, 6):
            f = open(underwaypath + filename + "-" + str(i) + ".txt", "a")
            f.close()

        # 检测 xxx-1.txt 是否为0
        cachef = open(underwaypath + filename + "-cache.txt", "r")
        cachelist = cachef.readlines()
        cachef.close()

        if cachelist.__len__() == 0:
            # writer in cache
            oldf = open(kindslibrarypath + filename + ".txt", "r")
            oldlist = oldf.readlines()
            oldf.close()
            ft.writerlist(underwaypath + filename + "-cache.txt", oldlist)

            # writer in xxx-1.txt
            # 插入xx-1.txt的格式：狗@dog@verb-1
            inserterlist = []
            for line in oldlist:
                inserterlist.append(line.replace("\n", "") + "@" + filename + "-1\n")

            ft.writerlist(underwaypath + filename + "-1.txt", inserterlist)


def getcorsscontent(regularpath, kindspath, filename):
    f = open(regularpath, "r")
    templist = f.readlines()
    f.close()
    for i in range(1, 6):
        f = open(kindspath + filename + "-" + str(i) + ".txt")
        templist.append(f.readlines())
        f.close()
    return templist


def main():
    count = 0
    tempfilg = 1

    # init underwaylibrary
    createfile(kindslibrarypath, underwaylibrarypath)

    while (tempfilg == 1):
        count = count + 1

        # init regular, 如果文本行小于8

        if ft.getlinescreate(regulartxt) < 8:
            # 对比kindslibrary目录内的文本 是否有更新
            # 将6个旧文本的内的行 追加的方式 添加到list
            dirlist = dt.getallfilename(kindslibrarypath)
            for filename in dirlist:
                # 用冒泡算法 对比 新旧文本 是否有更新
                newf = open(kindslibrarypath + filename + ".txt", "r")
                newlist = newf.readlines()
                newf.close()

                oldf = open(underwaylibrarypath + filename + "-cache.txt", "r")
                oldflist = oldf.readlines()
                oldf.close()

                for iline in newlist:
                    if iline in oldflist:
                        pass
                    else:
                        # 发现了新更新的行，添加到 xxx-1.txt
                        addf = open(underwaylibrarypath + filename + "-1.txt", "a+")
                        addf.write(iline.replace("\n", "") + "@" + filename + "-1\n")
                        addf.close()

                        addf1 = open(underwaylibrarypath + filename + "-cache.txt", "a+")
                        addf1.write(iline)
                        addf1.close()

            # 概率分布到方式获取 将 regular.txt 填充到30行 ,
            # 递归判断 文本里面都为空的话 xx-1～xx-4

            totalline = 0
            for filename in dt.getallfilename(kindslibrarypath):
                # 先统计有多少行
                statisticsf1 = open(underwaylibrarypath + filename + "-1.txt", "r")
                statisticsf2 = open(underwaylibrarypath + filename + "-2.txt", "r")
                statisticsf3 = open(underwaylibrarypath + filename + "-3.txt", "r")
                statisticsf4 = open(underwaylibrarypath + filename + "-4.txt", "r")
                s1list1 = statisticsf1.readlines()
                s1list2 = statisticsf2.readlines()
                s1list3 = statisticsf3.readlines()
                s1list4 = statisticsf4.readlines()
                statisticsf1.close()
                statisticsf2.close()
                statisticsf3.close()
                statisticsf4.close()
                totalline += s1list1.__len__() + s1list2.__len__() + s1list3.__len__() + s1list4.__len__()

            # 当没有内容时 跳出
            ref = open(regulartxt, "r")
            reflist = ref.readlines()
            ref.close()
            if totalline + reflist.__len__() == 0:
                tempfilg = 777
                continue

            # 判断是否够 30 行
            if totalline > 22:
                while ft.getlines(regulartxt) < 30:
                    r = t.getrandomnumber(1, 100)
                    # 随机获取
                    filename = dt.getrandomfilename(kindslibrarypath)
                    filename = filename.split(".")
                    filename = filename[0]

                    if r in range(1, 51):
                        fregular = open(regulartxt, "a+")
                        templine1 = ft.getlinecontent(underwaylibrarypath + filename + "-1.txt")

                        if templine1 != 0:
                            fregular.write(templine1)
                            ft.deleteline(underwaylibrarypath + filename + "-1.txt", templine1)

                        fregular.close()
                    elif r in range(51, 81):
                        fregular = open(regulartxt, "a+")
                        templine2 = ft.getrandomnumbers(underwaylibrarypath + filename + "-2.txt")

                        if templine2 != 0:
                            fregular.write(templine2)
                            ft.deleteline(underwaylibrarypath + filename + "-2.txt", templine2)

                        fregular.close()
                    elif r in range(81, 96):
                        fregular = open(regulartxt, "a+")
                        templine3 = ft.getrandomnumbers(underwaylibrarypath + filename + "-3.txt")

                        if templine3 != 0:
                            fregular.write(templine3)
                            ft.deleteline(underwaylibrarypath + filename + "-3.txt", templine3)

                        fregular.close()
                    elif r in range(95, 100):
                        fregular = open(regulartxt, "a+")
                        templine4 = ft.getrandomnumbers(underwaylibrarypath + filename + "-4.txt")

                        if templine4 != 0:
                            fregular.write(templine4)
                            ft.deleteline(underwaylibrarypath + filename + "-4.txt", templine4)

                        fregular.close()
            else:
                # 将剩的文本行全部写入 regular.txt
                for filename in dt.getallfilename(kindslibrarypath):
                    for i in range(1, 5):
                        littlef = open(underwaylibrarypath + filename + "-" + str(i) + ".txt", "r")
                        littlelist = littlef.readlines()
                        littlef.close()
                        if littlelist.__len__() != 0:
                            ft.writerlist(regulartxt, littlelist)
                            wf = open(underwaylibrarypath + filename + "-" + str(i) + ".txt", "w")
                            wf.close()

        # 随机从 regular.txt 获取一行内容
        templine = ft.getlinecontent(regulartxt)

        if templine == 0:
            tempfilg = 777
        else:
            # 分割
            linelist = templine.split("@")

            # get 键盘上的输入
            word = "\033[7;33m " + linelist[0].lstrip().rstrip() + " \033[0m"
            inputword = raw_input("👉 ‍请输入" + word + "的英文单词 : ")

            linelist2 = linelist[2].split("-")

            # 如果用 == 字符串对比不正确，考虑是否左右有空格
            if (inputword.lstrip().rstrip() == linelist[1].lstrip().rstrip()):
                # right

                print "🔰 恭喜，输入正确 : ", inputword.lstrip().rstrip()

                # 递归 向下层级
                if linelist2[1].lstrip().rstrip() == "1":
                    # 先删除当前文本，在转移到下一层文本
                    formatline1 = linelist[0] + "@" + linelist[1] + "@" + linelist2[0] + "-2"
                    ft.moveoldfile(underwaylibrarypath + linelist2[0] + "-2.txt", formatline1)
                    ft.deleteline(regulartxt, templine)

                elif linelist2[1].lstrip().rstrip() == "2":
                    formatline1 = linelist[0] + "@" + linelist[1] + "@" + linelist2[0] + "-3"
                    ft.moveoldfile(underwaylibrarypath + linelist2[0] + "-3.txt", formatline1)
                    ft.deleteline(regulartxt, templine)

                elif linelist2[1].lstrip().rstrip() == "3":
                    formatline1 = linelist[0] + "@" + linelist[1] + "@" + linelist2[0] + "-4"
                    ft.moveoldfile(underwaylibrarypath + linelist2[0] + "-4.txt", formatline1)
                    ft.deleteline(regulartxt, templine)

                elif linelist2[1].lstrip().rstrip() == "4":
                    formatline1 = linelist[0] + "@" + linelist[1] + "@" + linelist2[0] + "-5"
                    ft.moveoldfile(underwaylibrarypath + linelist2[0] + "-5.txt", formatline1)
                    ft.deleteline(regulartxt, templine)

                # 随机获取金币奖励
                r = t.getrandomnumber(1, 10)
                if r in [4, 7]:
                    amoney = "💰"
                    tempmoney = ""
                    rmoney = t.getrandomnumber(1, 9)
                    for c in range(rmoney):
                        tempmoney += amoney
                    print "✨✨✨" + tempmoney + "✨✨"

                    # get usermoney.txt
                    oldmoney = ft.readallcontent(usermoneypath)
                    tempmoneynumbers = tempmoney.__len__() / 4
                    newmoney = int(oldmoney) + tempmoneynumbers
                    print "恭喜您获得了" + str(tempmoneynumbers) + "个金币奖励.------------[已累积的金币数：" + str(newmoney) + "]"

                    # writer usermoney.txt
                    ft.coverwriter(usermoneypath, str(newmoney))
            else:
                # 执行 递归回上一层级
                if linelist2[1].lstrip().rstrip() == "2":
                    formatline1 = linelist[0] + "@" + linelist[1] + "@" + linelist2[0] + "-1"
                    print formatline1
                    ft.moveoldfile(underwaylibrarypath + linelist2[0] + "-1.txt", formatline1)
                    ft.deleteline(regulartxt, templine)

                elif linelist2[1].lstrip().rstrip() == "3":
                    formatline1 = linelist[0] + "@" + linelist[1] + "@" + linelist2[0] + "-2"
                    print formatline1
                    ft.moveoldfile(underwaylibrarypath + linelist2[0] + "-2.txt", formatline1)
                    ft.deleteline(regulartxt, templine)

                elif linelist2[1].lstrip().rstrip() == "4":
                    formatline1 = linelist[0] + "@" + linelist[1] + "@" + linelist2[0] + "-3"
                    print formatline1
                    ft.moveoldfile(underwaylibrarypath + linelist2[0] + "-3.txt", formatline1)
                    ft.deleteline(regulartxt, templine)

                # 随机读取 显示style # 字符小于8可以用
                if linelist[1].lstrip().rstrip().__len__() <= 8:
                    ff = open(fontstylepath, "r")
                    fflist = ff.readlines()
                    ff.close()
                    r1 = t.getrandomnumber(1, fflist.__len__())

                    outprint = t.printfont(fflist[r1 - 1].replace("\n", "") + " " + str(linelist[1].lstrip().rstrip()))
                else:
                    outprint = t.printfont("toilet " + linelist[1].lstrip().rstrip())

                print outprint
                errorword = "\033[7;31m " + linelist[1].lstrip().rstrip() + " \033[0m"
                print "❌ 输入错误！正确单词为:" + errorword

            # 刻意让练习次数逢8进一，让用户知道自己练习量并不多；
            if count == 8:
                count = 1
            print "-------------------------------------------------[当前练习次数：" + str(count) + "]"

    print "提示：db/kindslibarary/内的文本您已经熟悉,您可以添加新的内容后在运行程序。"
    print "提示：程序运行结束！"


if __name__ == '__main__':
    main()
else:
    print "Error"
