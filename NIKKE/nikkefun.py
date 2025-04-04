import time
import general_actions as generalact
import pyautogui as CSauto
from enum import Enum


CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


class LJ_BOSS(Enum):
    克拉肯 = 1
    镜像容器 = 2
    茵迪维利亚 = 3
    过激派 = 4
    死神 = 5


def dailytaskst(LJ_choose):
    backtomainmenu()
    collect()
    shop()
    nikke()
    ark(LJ_choose)
    dispatch()
    danrentuji()
    friend()


def ark(LJ_choose):
    generalact.logger.info('nikkefun.ark')
    generalact.imgcorrdinatefun('NIKKE\\picture\\ark.bmp', 0.7, 1100, 500, 1920, 1080)
    generalact.imgcorrdinatefunde2('NIKKE\\picture\\JJC.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\SPJJC.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(959, 267)
    generalact.moveclick_1s(1047, 956)
    backtoark()
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\mock.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(1)
    generalact.rangeclick02(5, 961, 731)
    generalact.moveclick_1s(952, 641)
    generalact.moveclick_5s(1080, 915)  # 快速模拟
    generalact.moveclick_3s(990, 971)
    generalact.moveclick_1s(1125, 1000)
    generalact.imgcorrdinatefun('NIKKE\\picture\\nextstep.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\mockfinish.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
    generalact.imgcorrdinatefuncount3('NIKKE\\picture\\noselect1.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefuncount3('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
    generalact.imgcorrdinatefuncount3('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
    backtomainmenu()

    generalact.imgcorrdinatefun('NIKKE\\picture\\ark.bmp', 0.7, 1100, 500, 1920, 1080)
    generalact.imgcorrdinatefunde2('NIKKE\\picture\\JJC.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\NEWJJC.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    if generalact.imgcorrdinatefuncount3('NIKKE\\picture\\JJCBAT.bmp', 0.9, 680, 770, 1920, 1080):
        for i in range(5):
            generalact.imgcorrdinatefunde1('NIKKE\\picture\\JJCBAT.bmp', 0.9, 680, 770, 1920, 1080)
            generalact.imgcorrdinatefunde1('NIKKE\\picture\\JJCBAT2.bmp', 0.9, 0, 0, 1920, 1080)
            generalact.imgcorrdinatefunde1('NIKKE\\picture\\nextstep2.bmp', 0.9, 0, 0, 1920, 1080)
            for j in range(3):
                generalact.moveclick_02s(960, 973)
                generalact.moveclick_02s(963, 1008)
    generalact.moveclick_1s(163, 1024)  # home
    generalact.moveclick_1s(163, 1024)  # home
    backtomainmenu()

    generalact.imgcorrdinatefun('NIKKE\\picture\\ark.bmp', 0.7, 1100, 500, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\ark_LJ.bmp', 0.9, 0, 0, 1920, 1080)
    if LJ_choose == LJ_BOSS.克拉肯:
        while 1:
            if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\LJ_BOSS1.bmp', 0.8, 0, 0, 1920, 1080):
                break
            generalact.moveclick_3s(1146, 810)
        generalact.moveclick_3s(960, 886)
        generalact.rangeclick02(5, 940, 735)  # 1
        # generalact.rangeclick02(5, 1010, 735)  # 2
        # generalact.rangeclick02(5, 1075, 735)  # 3
        # generalact.rangeclick02(5, 1145, 735)  # 4
        # generalact.rangeclick02(5, 1215, 735)  # 5
        generalact.rangeclick02(5, 1100, 1000)
        while 1:
            if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\nextstep.bmp', 0.8, 0, 0, 1920, 1080):
                break
            if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\nextstep2.bmp', 0.8, 0, 0, 1920, 1080):
                break
            time.sleep(5)
        generalact.rangeclick02(10, 940, 1045)
        generalact.rangeclick02(5, 1107, 920)
        generalact.rangeclick02(10, 940, 1045)
        generalact.rangeclick02(5, 1107, 920)
    backtomainmenu()
    # if LJ_choose == LJ_BOSS.镜像容器:
    #     print(LJ_BOSS.镜像容器.value)
    #     pass


def mock():
    generalact.logger.info('nikkefun.mock')
    time.sleep(1)
    if generalact.imgcorrdinatefuncount3('NIKKE\\picture\\quickbat.bmp', 0.9, 600, 600, 1920, 1080):
        generalact.moveclick_1s(1136, 922)
        if generalact.imgcorrdinatefuncount('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
            if generalact.imgcorrdinatefuncount3('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
                time.sleep(1)
                generalact.moveclick_1s(991, 747)
                generalact.imgcorrdinatefun('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
                if generalact.imgcorrdinatefuncount3('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
                    generalact.moveclick_1s(989, 712)
                    generalact.imgcorrdinatefun('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
                for i in range(5):
                    generalact.moveclick_01s(951, 1009)
    if generalact.imgcorrdinatefuncount3('NIKKE\\picture\\noselect.bmp', 0.9, 600, 600, 1920, 1080):
        generalact.imgcorrdinatefun('NIKKE\\picture\\noselect.bmp', 0.9, 600, 600, 1920, 1080)
        generalact.imgcorrdinatefun('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
        for i in range(5):
            generalact.moveclick_01s(951, 1009)
    if generalact.imgcorrdinatefuncount3('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
        time.sleep(1)
        generalact.moveclick_02s(942, 827)
        generalact.moveclick_02s(942, 787)
        generalact.moveclick_02s(942, 737)
        generalact.moveclick_02s(942, 707)
        generalact.imgcorrdinatefun('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
        for i in range(5):
            generalact.moveclick_01s(951, 1009)


def danrentuji():
    if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\danrentuji.bmp', 0.8, 0, 0, 1000, 1000):
        generalact.logger.info('nikkefun.danrentuji')
        time.sleep(5)
        if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\danrentuji_result.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.rangeclick02(5, 965, 1061)
        else:
            if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\quickbat.bmp', 0.9, 0, 0, 1920, 1080):
                generalact.rangeclick02(4, 1097, 755)
                generalact.rangeclick02(4, 1068, 835)
            else:
                for i in range(3):
                    generalact.moveclick_1s(963, 907)
                    generalact.moveclick_5s(1090, 678)
                    generalact.moveclick_8s(1117, 928)
                    while 1:
                        if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\nextstep.bmp', 0.8, 0, 0, 1920, 1080):
                            break
                        if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\nextstep2.bmp', 0.8, 0, 0, 1920, 1080):
                            break
                        time.sleep(5)
                    generalact.rangeclick02(10, 940, 1045)
        backtomainmenu()


def backtoark():
    count = 0
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\picture\\JJC.bmp', 0.9, 0, 0, 1920, 1080):
            break
        else:
            back1()
            if count > 5:
                generalact.imgcorrdinatefun('NIKKE\\picture\\ark.bmp', 0.9, 1100, 500, 1920, 1080)
                break


def nikke():
    generalact.logger.info('nikkefun.nikke')
    generalact.moveclick_1s(740, 991)  # nikke
    backtonikke()
    # generalact.moveclick_1s(781, 220)  # 1
    generalact.moveclick_1s(925, 220)  # 3
    for i in range(2):
        generalact.dragmouse(1000, 800, 1000, 300)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\lapi.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\lvup.bmp', 0.9, 1500, 200, 1920, 1080)
    generalact.moveclick_1s(954, 844)
    backtonikke()
    # generalact.moveclick_1s(781, 220)  # 1
    generalact.moveclick_1s(925, 220)  # 3
    # generalact.moveclick_1s(925, 220)  # 3
    while 1:
        if generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\longhair.bmp', 0.9, 0, 0, 1920, 1080):
            break
        else:
            generalact.dragmouse(1430, 650, 1430, 450)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\limitbreak.bmp', 0.9, 1500, 200, 1920, 1080)
    generalact.moveclick_1s(1789, 888)
    generalact.moveclick_1s(1789, 888)
    # generalact.moveclick_1s(978, 829)  # 装备升级
    generalact.moveclick_1s(960, 921)
    for i in range(3):
        generalact.moveclick_1s(763, 541)
        generalact.moveclick_2s(1056, 909)
    backtonikke()
    # # generalact.moveclick_1s(781, 220)  # 1
    # generalact.moveclick_1s(925, 220)  # 3

    generalact.moveclick_1s(1656, 137)
    generalact.moveclick_1s(368, 378)
    for i in range(10):
        generalact.moveclick_1s(1105, 900)  # 咨询
        generalact.moveclick_1s(1000, 680)
        consultation()
    generalact.moveclick_1s(163, 1024)  # home
    backtomainmenu()


def consultation():
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\picture\\consultation1.bmp', 0.9, 0, 0, 1920, 1080):
            for i in range(10):
                generalact.moveclick_01s(965, 998)
            generalact.moveclick_1s(1885, 484)
            break
        else:
            for i in range(6):
                generalact.moveclick_01s(989, 733)
                CSauto.press("1")


def backtonikke():
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\picture\\liberate.bmp', 0.9, 0, 90, 200, 200):
            break
        else:
            back1()


def shop():
    generalact.logger.info('nikkefun.shop')
    generalact.moveclick_1s(575, 747)  # shop
    backtoshop1()
    for i in range(2):
        generalact.moveclick_1s(157, 687)
        shopbuyback()
        # x = 0
        # for j in range(4):
        #     generalact.moveclick_1s(298 + x, 654)
        #     while 1:
        #         if generalact.imgcorrdinatefuncount3('NIKKE\\picture\\shopcredit.bmp', 0.9, 700, 150, 500, 700):
        #             shopbuyback()
        #             break
        #         else:
        #             backtoshop()
        #             break
        #     x += 160
        if i == 1:
            break
        generalact.moveclick_1s(342, 492)
        generalact.imgcorrdinatefun('NIKKE\\picture\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
        backtoshop()
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\shop_JJC.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(48, 668)
    x = 0
    for i in range(6):
        generalact.moveclick_05s(190 + x, 653)
        x += 165
        shopmax1()
    if generalact.firstDayOfWeek2():
        generalact.imgcorrdinatefunde1('NIKKE\\picture\\scrapshop.bmp', 0.9, 0, 0, 1920, 1080)
        scrapshop_xia3()
    backtomainmenu()


def shopbuyback():
    generalact.imgcorrdinatefun('NIKKE\\picture\\buy.bmp', 0.9, 700, 850, 1920, 1080)
    backtoshop()


def collect():
    generalact.logger.info('nikkefun.collect')
    generalact.moveclick_1s(575, 897)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\huodejiangli.bmp', 0.9, 700, 850, 1920, 1080)
    backtomainmenu()
    generalact.moveclick_1s(575, 897)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\yijujianmie.bmp', 0.9, 700, 850, 1920, 1080)
    generalact.moveclick_1s(1037, 824)
    backtomainmenu()


def dispatch():
    generalact.logger.info('nikkefun.dispatch')
    generalact.moveclick_1s(604, 830)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\dispatch.bmp', 0.9, 600, 850, 1920, 1080)
    for i in range(5):
        generalact.moveclick_02s(1116, 902)
    for i in range(5):
        generalact.moveclick_02s(1005, 900)
    generalact.moveclick_1s(163, 1024)  # home
    generalact.moveclick_1s(163, 1024)  # home
    backtomainmenu()


def friend():
    generalact.logger.info('nikkefun.friend')
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\friend.bmp', 0.9, 1600, 0, 1920, 1080)
    generalact.rangeclick02(3, 1149, 923)
    backtomainmenu()
    generalact.moveclick_1s(575, 897)
    generalact.imgcorrdinatefun('NIKKE\\picture\\huodejiangli.bmp', 0.9, 700, 850, 1920, 1080)
    backtomainmenu()
    generalact.moveclick_3s(1668, 113)
    generalact.rangeclick02(10, 1154, 970)
    backtomainmenu()
    generalact.moveclick_2s(561, 666)  # 付费商店
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\Dgift.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(268, 313)
    generalact.moveclick_1s(127, 542)
    backtomainmenu()
    if generalact.firstDayOfWeek2():
        generalact.moveclick_2s(561, 666)  # 付费商店
        generalact.imgcorrdinatefunde1('NIKKE\\picture\\Dgift.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_1s(425, 313)
        generalact.moveclick_1s(127, 542)
        backtomainmenu()


def ALS():
    time.sleep(2)
    while 1:
        # generalact.imgcorrdinatefunwhilenotime('NIKKE\\picture\\ALS1.bmp', 0.2, 700, 500, 500, 500)
        # CSauto.mouseDown()
        # generalact.imgcorrdinatefunwhilenotime('NIKKE\\picture\\ALS2.bmp', 0.2, 700, 500, 500, 500)
        # time.sleep(0.055)
        # CSauto.mouseUp()
        # CSauto.click()
        CSauto.mouseDown()
        time.sleep(0.1)
        CSauto.mouseUp()


def startwholegame():
    CSauto.hotkey('winleft', 'd')
    time.sleep(3)
    generalact.startup_time('C:\\Software\\AKPlatform\\AK.exe', 10)
    generalact.rangeclick02(10, 1150, 430)
    generalact.moveclick_1s(882, 593)
    time.sleep(10)
    generalact.rangeclick02(10, 1900, 20)
    generalact.startup_time('C:\\Software\\AKPlatform\\AK.exe', 2)
    generalact.moveclick_1s(882, 593)
    generalact.imgcorrdinatefunwhile('MUMU\\ak_startgame.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.startup_time('C:\\MobileGame\\NIKKE\\Launcher\\nikke_launcher.exe', 10)
    # generalact.imgcorrdinatefunwhile('NIKKE\\picture\\gui_start.bmp', 0.9, 0, 0, 1920, 1080)
    # generalact.imgcorrdinatefunde1('NIKKE\\picture\\gui_start.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunwhile('NIKKE\\picture\\gui_start2.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\picture\\gui_start2.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(10)
    generalact.rangeclick02(10, 44, 46)
    time.sleep(3)
    generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\enterdownload.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainmenu()


def closegame():
    generalact.killprocess("AK.exe")
    generalact.killprocess("nikke.exe")
    generalact.killprocess("nikke_launcher.exe")


def backtomainmenu():
    n = 0
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\picture\\ID.bmp', 0.8, 670, 190, 1920, 1080) == 1:
            generalact.moveclick_1s(44, 46)
            break
        else:
            back1()
            n += 1
            if n == 2:
                generalact.moveclick_05s(44, 46)
                n = 0
        generalact.imgcorrdinatefunclickcount3('NIKKE\\picture\\enterdownload.bmp', 0.8, 0, 0, 1920, 1080)


def back1():
    generalact.moveclick_1s(60, 1024)


def back2():
    generalact.moveclick_2s(60, 1024)


def back3():
    generalact.moveclick_3s(60, 1024)


def scrapshop():
    x = 0
    y = 0
    for i in range(11):
        generalact.moveclick_05s(190 + x, 653 + y)
        x += 165
        shopmax1()
    y += 240
    x = 0
    for i in range(2):
        generalact.moveclick_05s(190 + x, 653 + y)
        x += 165
        shopmax1()
    x = 0
    for i in range(2):
        generalact.moveclick_05s(850 + x, 653 + y)
        x = x+165*3
        shopmax1()
    x += 170
    generalact.moveclick_05s(189 + x, 653 + y)
    shopmax1()


def scrapshop_xia3():
    x = 0
    y = 0
    for i in range(8):
        generalact.moveclick_1s(190 + x, 653 + y)
        x += 165
        shopmax1()
    for i in range(1):
        x += 165
    for i in range(2):
        generalact.moveclick_1s(190 + x, 653 + y)
        x += 165
        shopmax1()
    y += 240
    x = 0 + 165
    for i in range(2):
        generalact.moveclick_1s(190 + x, 653 + y)
        x += 165
        shopmax1()


def shopmax1():
    generalact.imgcorrdinatefun3('NIKKE\\picture\\MAX.bmp', 0.8, 700, 500, 1920, 1080)
    generalact.moveclick_1s(1160, 670)
    generalact.imgcorrdinatefun('NIKKE\\picture\\buy.bmp', 0.8, 700, 500, 1920, 1080)
    generalact.rangeclick01(4, 1760, 950)


def backtoshop():
    # while 1:
    #     if generalact.imgcorrdinatefuncount('NIKKE\\picture\\shop.bmp', 0.9, 0, 0, 1920, 1080) == 1:
    #         backup1()
    #         break
    #     else:
    #         # break
    #         backup1()
    generalact.rangeclick02(5, 955, 118)


def backtoshop1():
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\picture\\shop.bmp', 0.9, 0, 0, 1920, 1080) == 1:
            backup1()
            break
        else:
            # break
            backup1()


def backup1():
    generalact.moveclick_1s(46, 37)
