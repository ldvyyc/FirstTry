import numpy as np
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

def Comment_Danmu():
    x = []
    y = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(1, 5018):
        Danmu = int(sheet.cell(i, 5).value)
        x.append(Danmu)
        # print(Co)
        Comment = int(sheet.cell(i, 6).value)
        y.append(Comment)
        # print(foll_num)
    # x = [300, 500, 600, 200]
    # y = [170045, 75463, 194320, 300000]
    plt.figure(figsize=(20, 15))
    plt.scatter(x, y, marker='o', color='blue')
    plt.title('Comment_Danmu', fontsize=100)
    plt.xlabel('Danmu', fontsize=60)
    plt.ylabel('Comment', fontsize=60)
    plt.xticks([0, 300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000], fontsize=40)
    plt.yticks([0,100,200,300,400,500,600,700,800,900,1000,1100], fontsize=40)
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
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for j in range(1, 3):
        print(str(sheet.cell(j, 7).value))
        ori = str(sheet.cell(j, 7).value)[5:6]
        print(ori)
        mon = int(ori)
        if mon==6:
            if len(ori)==9:
                day = str(ori)[7:]
                day = int(day)
                if day>=20:
                    c = c+1
                else:
                    b = b+1
            else:
                a = a+1
        elif mon==7:
            if len(ori)==9:
                day = str(ori)[7:]
                day = int(day)
                if day>=20:
                    f = f+1
                else:
                    e = e+1
            else:
                d = d+1
        elif mon==6:
            if len(ori)==9:
                day = str(ori)[7:]
                day = int(day)
                if day>=20:
                    i = i+1
                else:
                    h = h+1
            else:
                g = g+1
        else:
            continue

    # data = [a,b,c,d,e,f,g,h,i]
    #
    # plt.figure(figsize=(20, 15))
    # plt.bar(range(4), data, align = 'center',color='steelblue', alpha = 0.8)
    # plt.title('PostNum——Followers', fontsize=100)
    # plt.xlabel('Followers', fontsize=60)
    # plt.ylabel('PostNum', fontsize=60)
    # plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700], fontsize=40)
    # plt.xticks(range(9)[6.1-6.10,1.11-6.20,6.21-6.30,7.1-7.10,7.11-7.20,7.21-7.31,8.1-8.10,8.11-8.20,8.21-8.31], fontsize=40)
    # plt.show()


def ccc():
    x = []
    y = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    aaa = 0
    for i in range(1, 5018):
        if i == 1:
            x.append(int(sheet.cell(i, 16).value))
            y.append(int(sheet.cell(i,12).value))
        ttt = int(sheet.cell(i, 13).value)
        # print(ttt)
        if aaa == ttt:
            continue
        else:
            x.append(int(sheet.cell(i, 16).value))
            y.append(int(sheet.cell(i,12).value))
            # print(int(sheet.cell(i,12).value))
            # print(int(sheet.cell(i, 16).value))
            aaa = ttt
        # print(foll_num)
    x = [300, 500, 600, 200]
    y = [170045, 75463, 194320, 300000]
    plt.figure(figsize=(20, 15))
    plt.scatter(x, y, marker='o', color='blue')
    plt.title('PostNum——Followers', fontsize=100)
    plt.xlabel('Followers', fontsize=60)
    plt.ylabel('PostNum', fontsize=60)
    plt.yticks([0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550], fontsize=40)
    plt.xticks([0,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000,550000], fontsize=40)
    plt.show()

def AuthorFoll_VideoLike():
    a = []
    b = []
    readbook = xlrd.open_workbook(r"D:\CS\pythonProject\bilibili\dataTo.xlsx")
    sheet = readbook.sheet_by_name('Sheet1')
    for i in range(2, 6):
        stow_num = int(sheet.cell(i, 9).value)
        a.append(stow_num)
        print(stow_num)
        foll_num = int(sheet.cell(i, 15).value)
        b.append(foll_num)
        print(foll_num)
    # x = [300, 500, 600, 200]
    # y = [170045, 75463, 194320, 300000]
    x = a
    y = b

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, marker='o', color='blue')
    plt.title('ceshi', fontsize=40)
    plt.xlabel('Stow', fontsize=20)
    plt.ylabel('Follow', fontsize=20)
    plt.xticks([0,100,200,300,400,500,600,700,800,900,1000])
    plt.yticks([0,50000,100000,150000,200000,250000,300000,350000,400000,450000,500000,550000])
    # plt.yticks([0,1,2,3,4,5,6,7])
    # plt.xticks([0,200,400,600,800,100,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800,4000,4200,4400,4600,4800])
    # plt.yticks([0,200,400,600,800,100,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800,4000,4200,4400,4600,4800])
    plt.show()


if __name__=="__main__":
    # ccc()
    Date()
    # Comment_Danmu()
    # AuthorFoll_VideoLike()