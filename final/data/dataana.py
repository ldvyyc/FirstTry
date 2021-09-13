import numpy as np
import re
import xlrd
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import pylab as plb

def Play_Comm():
    comm = []
    play_ = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5018):
        playori = str(sheet.cell(i, 4).value)
        if playori[-1] == '万':
            playtem = str(playori)[0:-1]
            playtem = float(playtem)
            play = playtem * 10000
            play = int(play)
            play_.append(play)
        else:
            playori = float(playori)
            play_.append(int(playori))

        commori = str(sheet.cell(i, 6).value)
        if commori[-1] == '万':
            commtem = str(commori)[0:-1]
            commtem = float(commtem)
            commm = commtem * 10000
            commm = int(commm)
            comm.append(commm)
        else:
            commori = float(commori)
            comm.append(int(commori))

    g_s_m = pd.Series(comm)  # 利用Series将列表转换成新的、pandas可处理的数据

    g_a_d = pd.Series(play_)
    corr_gust = round(g_s_m.corr(g_a_d), 4)  # 计算标准差，round(a, 4)是保留a的前四位小数

    print('corr_gust :', corr_gust)

    plt.scatter(play_, comm)

    plt.title('play_comm :' + str(corr_gust), fontproperties='SimHei')  # 给图写上title

    plt.show()


def UpVideoStable():
    up_followers = []
    play__ = []
    data = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5018):
        if len(up_followers)==10:
            break
        playori = str(sheet.cell(i, 16).value)
        if playori not in up_followers:
            play__.append(data)
            data = []
            up_followers.append(playori)
            aaa = str(sheet.cell(i, 4).value)
            if aaa[-1] == '万':
                aaa = str(aaa)[0:-1]
                aaa = float(aaa)
                aaaa = aaa * 10000
                aaaa = int(aaaa)
                data.append(aaaa)
            else:
                aaa = float(aaa)
                data.append(int(aaa))
        else:
            aaa = str(sheet.cell(i, 4).value)
            if aaa[-1] == '万':
                aaa = str(aaa)[0:-1]
                aaa = float(aaa)
                aaaa = aaa * 10000
                aaaa = int(aaaa)
                data.append(aaaa)
            else:
                aaa = float(aaa)
                data.append(int(aaa))


    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(11, 11))
    plt.suptitle("关注人数前九的UP主视频播放量", fontsize = 40)

    plt.subplot(3,3,1)
    sub1 = play__[1]
    len1 = len(sub1)
    axis1 = range(len1)
    plt.bar(axis1,sub1)

    plt.subplot(3,3,2)
    sub2 = play__[2]
    len2 = len(sub2)
    axis2 = range(len2)
    plt.bar(axis2,sub2)

    plt.subplot(3,3,3)
    sub3 = play__[3]
    len3 = len(sub3)
    axis3 = range(len3)
    plt.bar(axis3,sub3)

    plt.subplot(3,3,4)
    sub4 = play__[4]
    len4 = len(sub4)
    axis4 = range(len4)
    plt.bar(axis4,sub4)

    plt.subplot(3,3,5)
    sub5 = play__[5]
    len5 = len(sub5)
    axis5 = range(len5)
    plt.bar(axis5,sub5)

    plt.subplot(3,3,6)
    sub6 = play__[6]
    len6 = len(sub6)
    axis6 = range(len6)
    plt.bar(axis6,sub6)

    plt.subplot(3,3,7)
    sub7 = play__[7]
    len7 = len(sub7)
    axis7 = range(len7)
    plt.bar(axis7,sub7)

    plt.subplot(3,3,8)
    sub8 = play__[8]
    len8 = len(sub8)
    axis8 = range(len8)
    plt.bar(axis8,sub8)

    plt.subplot(3,3,9)
    sub9 = play__[9]
    len9 = len(sub9)
    axis9 = range(len9)
    plt.bar(axis9,sub9)
    plt.show()


def Like_Banana():
    like_ = []
    banana_ = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5018):
        likeori = str(sheet.cell(i, 8).value)
        if likeori == '点赞':
            like_.append(0)
        elif likeori[-1] == '万':
            playtem = str(likeori)[0:-1]
            playtem = float(playtem)
            play = playtem * 10000
            play = int(play)
            like_.append(play)
        else:
            likeori = float(likeori)
            like_.append(int(likeori))

        bananaori = str(sheet.cell(i, 10).value)
        if bananaori[-1] == '万':
            commtem = str(bananaori)[0:-1]
            commtem = float(commtem)
            commm = commtem * 10000
            commm = int(commm)
            banana_.append(commm)
        else:
            bananaori = float(bananaori)
            banana_.append(int(bananaori))


    ax = np.array(like_)
    ay = np.array(banana_)
    az = np.polyfit(ax, ay, 1)
    print(az)

    g_s_m = pd.Series(banana_)  # 利用Series将列表转换成新的、pandas可处理的数据

    g_a_d = pd.Series(like_)
    corr_gust = round(g_s_m.corr(g_a_d), 4)  # 计算标准差，round(a, 4)是保留a的前四位小数

    print('corr_gust :', corr_gust)

    plt.scatter(like_, banana_)

    plt.title('Banana_Like :' + str(corr_gust) + '    y='+str(az[0]) +'x' + str(az[1]), fontproperties='SimHei')  # 给图写上title

    plt.show()




findGame = re.compile(r'游戏')
findMusic = re.compile(r'音乐')
findYuanShen = re.compile(r'原神')
findGaoxiao = re.compile(r'搞笑')
def Search_game():
    a = 0
    b = 0
    c = 0
    d = 0
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5018):
        strr = str(sheet.cell(i, 2).value)
        if re.findall(findGame, strr):
            a = a+1
        if re.findall(findMusic, strr):
            b = b+1
        if re.findall(findYuanShen, strr):
            c = c+1
        if re.findall(findGaoxiao,strr):
            d = d+1
        else:
            continue
    print(a)
    print(b)
    print(c)
    print(d)


def Mean():
    like_ = []
    banana_ = []
    comm = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5018):
        likeori = str(sheet.cell(i, 8).value)
        if likeori == '点赞':
            like_.append(0)
        elif likeori[-1] == '万':
            playtem = str(likeori)[0:-1]
            playtem = float(playtem)
            play = playtem * 10000
            play = int(play)
            like_.append(play)
        else:
            likeori = float(likeori)
            like_.append(int(likeori))

        bananaori = str(sheet.cell(i, 10).value)
        if bananaori[-1] == '万':
            commtem = str(bananaori)[0:-1]
            commtem = float(commtem)
            commm = commtem * 10000
            commm = int(commm)
            banana_.append(commm)
        else:
            bananaori = float(bananaori)
            banana_.append(int(bananaori))

        commori = str(sheet.cell(i, 6).value)
        if commori[-1] == '万':
            commtem = str(commori)[0:-1]
            commtem = float(commtem)
            commm = commtem * 10000
            commm = int(commm)
            comm.append(commm)
        else:
            commori = float(commori)
            comm.append(int(commori))

    ax = np.array(like_)
    ay = np.array(comm)
    az = np.array(banana_)
    print(np.mean(ax))
    print(np.std(ax))
    print(np.mean(ay))
    print(np.std(ay))
    print(np.mean(az))
    print(np.std(az))

    plt.hist(ax,bins = 200, range=(0,1500), color='red')
    plt.title("Likes")
    plt.show()


    plt.hist(az,bins = 100, range=(0,5000), color='blue')
    plt.title("Bananas")
    plt.show()

    plt.hist(ay, bins=100, range=(0, 2000), color='brown')
    plt.title("Comments")
    plt.show()

def Date():
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0

    aa=0
    bb=0
    cc=0
    dd=0
    ee=0
    ff=0
    gg=0
    hh=0
    ii=0
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for j in range(0, 5018):
        strr = str(sheet.cell(i, 2).value)
        if str(sheet.cell(j, 7).value)[-1] == '前':
            continue
        ori = str(sheet.cell(j, 7).value)
        orii = str(sheet.cell(j, 7).value)[5:6]
        # print(str(sheet.cell(j, 7).value))
        mon = int(orii)
        # print(mon)
        if mon==6:
            if len(ori)==9:
                day = str(ori)[7:]
                day = int(day)
                if day>=20:
                    c = c+1
                    if re.findall(findGaoxiao,strr):
                        cc = cc+1
                else:
                    b = b+1
                    if re.findall(findGaoxiao,strr):
                        bb = bb+1
            else:
                a = a+1
                if re.findall(findGaoxiao, strr):
                    aa = aa + 1
        elif mon==7:
            if len(ori)==9:
                day = str(ori)[7:]
                day = int(day)
                if day>=20:
                    f = f+1
                    if re.findall(findGaoxiao,strr):
                        ff = ff+1
                else:
                    e = e+1
                    if re.findall(findGaoxiao,strr):
                        ee = ee+1
            else:
                d = d+1
                if re.findall(findGaoxiao, strr):
                    dd = dd + 1
        elif mon==8:
            if len(ori)==9:
                day = str(ori)[7:]
                day = int(day)
                if day>=20:
                    i = i+1
                    if re.findall(findGaoxiao,strr):
                        ii = ii+1
                else:
                    h = h+1
                    if re.findall(findGaoxiao,strr):
                        hh = hh+1
            else:
                g = g+1
                if re.findall(findGaoxiao, strr):
                    gg = gg + 1
        else:
            continue

    height = [a,b,c,d,e,f,g,h,i]
    gaoxiao = [aa,bb,cc,dd,ee,ff,gg,hh,ii]

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    names = ('6.1-6.10','1.11-6.20','6.21-6.30','7.1-7.10','7.11-7.20','7.21-7.31','8.1-8.10','8.11-8.20','8.21-8.31')

    plt.bar(names, height)
    plt.plot(names,gaoxiao,'ro-')
    plt.xticks(rotation=30)
    plt.title('发布数量&"搞笑"关键词时间分布')
    plt.show()


def Two():
    comm = []
    play_ = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5018):
        playori = str(sheet.cell(i, 4).value)
        if playori[-1] == '万':
            playtem = str(playori)[0:-1]
            playtem = float(playtem)
            play = playtem * 10000
            play = int(play)
            play_.append(play)
        else:
            playori = float(playori)
            play_.append(int(playori))
        commori = str(sheet.cell(i, 6).value)
        if commori[-1] == '万':
            commtem = str(playori)[0:-1]
            commtem = float(commtem)
            commm = commtem * 10000
            commm = int(commm)
            comm.append(commm)
        else:
            commori = float(commori)
            comm.append(int(commori))

    cols1 = play_
    cols2 = comm
    n = 100
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    for i in range(n):
        s1 = s1 + cols2[i]
        s2 = s2 + cols1[i]
        s3 = s3 + cols1[i] * cols1[i]
        s4 = s4 + cols1[i] * cols2[i]
        s5 = s5 + cols1[i] * cols1[i] * cols1[i]
        s6 = s6 + cols1[i] * cols1[i] * cols2[i]
        s7 = s7 + cols1[i] * cols1[i] * cols1[i] * cols1[i]
    b0 = sp.Symbol('b0')
    b1 = sp.Symbol('b1')
    b2 = sp.Symbol('b2')
    f1 = ((s1 - b1 * s2 - b2 * s3) / 100) - b0
    f2 = ((s4 - b0 * s2 - b2 * s5) / s3) - b1
    f3 = ((s6 - b0 * s3 - b1 * s5) / s7) - b2
    result = sp.solve([f1, f2, f3], [b0, b1, b2])
    a = result[b0]
    b = result[b1]
    c = result[b2]
    plt.scatter(cols1, cols2, color='blue')
    x = np.linspace(0, 15, 100)
    y = a + b * x + c * x * x
    plt.plot(x, y, color="red")
    plt.show()

def Comment_Danmu():
    x = []
    y = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5000):
        Danmu = int(sheet.cell(i, 5).value)
        x.append(Danmu)
        Comment = int(sheet.cell(i, 6).value)
        y.append(Comment)

    g_s_m = pd.Series(x)
    g_a_d = pd.Series(y)
    corr_gust = round(g_s_m.corr(g_a_d), 4)
    print('corr_gust :', corr_gust)
    plt.scatter(x, y)
    plt.title('Comment-Danmu :' + str(corr_gust),fontproperties='SimHei')
    plt.show()

if __name__=="__main__":
    # Play_Comm()
    # Search_game()
    # Date()
    # Two()
    # Like_Banana()
    # Mean()
    # UpVideoStable()
    Comment_Danmu()