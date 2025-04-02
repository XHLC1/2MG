import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst():
    backtomainmenu()
    collect()
    shop()
    nikke()
    ark()
    dispatch()
    friend()


def ark():
    generalact.imgcorrdinatefun('NIKKE\\ark.bmp', 0.7, 1100, 500, 1920, 1080)
    generalact.imgcorrdinatefunde2('NIKKE\\JJC.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\SPJJC.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(959, 267)
    generalact.moveclick_1s(1047, 956)
    backtoark()
    generalact.imgcorrdinatefunde1('NIKKE\\mock.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(1)
    generalact.moveclick_1s(952, 641)
    generalact.moveclick_1s(955, 537)
    generalact.moveclick_1s(1118, 657)
    generalact.moveclick_1s(991, 918)  # 开始模拟
    generalact.imgcorrdinatefunwhile('NIKKE\\mockstop.bmp', 0.9, 0, 0, 1920, 1080)
    for i in range(5):
        generalact.moveclick_1s(1124, 727)
        mock()
    generalact.imgcorrdinatefun('NIKKE\\treatmentroom.bmp', 0.9, 0, 0, 1920, 1080)
    mock()
    generalact.moveclick_1s(961, 771)
    generalact.moveclick_1s(1148, 1002)
    generalact.imgcorrdinatefun('NIKKE\\nextstep.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\mockfinish.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\noselect1.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
    generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
    backtomainmenu()
    generalact.imgcorrdinatefun('NIKKE\\ark.bmp', 0.7, 1100, 500, 1920, 1080)
    generalact.imgcorrdinatefunde2('NIKKE\\JJC.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\NEWJJC.bmp', 0.9, 0, 0, 1920, 1080)
    for i in range(5):
        generalact.imgcorrdinatefunde1('NIKKE\\JJCBAT.bmp', 0.9, 680, 770, 1920, 1080)
        generalact.imgcorrdinatefunde1('NIKKE\\JJCBAT2.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('NIKKE\\nextstep2.bmp', 0.9, 0, 0, 1920, 1080)
        for j in range(3):
            generalact.moveclick_02s(960, 973)
            generalact.moveclick_02s(963, 1008)
    generalact.moveclick_1s(163, 1024)  # home
    generalact.moveclick_1s(163, 1024)  # home
    backtomainmenu()


def mock():
    time.sleep(1)
    if generalact.imgcorrdinatefuncount3('NIKKE\\quickbat.bmp', 0.9, 600, 600, 1920, 1080):
        generalact.moveclick_1s(1136, 922)
        if generalact.imgcorrdinatefuncount('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
            if generalact.imgcorrdinatefuncount3('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
                time.sleep(1)
                generalact.moveclick_1s(991, 747)
                generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
                if generalact.imgcorrdinatefuncount3('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
                    generalact.moveclick_1s(989, 712)
                    generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
                for i in range(5):
                    generalact.moveclick_01s(951, 1009)
    if generalact.imgcorrdinatefuncount3('NIKKE\\noselect.bmp', 0.9, 600, 600, 1920, 1080):
        generalact.imgcorrdinatefun('NIKKE\\noselect.bmp', 0.9, 600, 600, 1920, 1080)
        generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
        for i in range(5):
            generalact.moveclick_01s(951, 1009)
    if generalact.imgcorrdinatefuncount3('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080):
        time.sleep(1)
        generalact.moveclick_02s(942, 827)
        generalact.moveclick_02s(942, 787)
        generalact.moveclick_02s(942, 737)
        generalact.moveclick_02s(942, 707)
        generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
        for i in range(5):
            generalact.moveclick_01s(951, 1009)


def backtoark():
    count = 0
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\JJC.bmp', 0.9, 0, 0, 1920, 1080):
            break
        else:
            back1()
            if count > 5:
                generalact.imgcorrdinatefun('NIKKE\\ark.bmp', 0.9, 1100, 500, 1920, 1080)
                break


def nikke():
    generalact.moveclick_1s(740, 991)  # nikke
    backtonikke()
    generalact.moveclick_1s(781, 220)
    for i in range(2):
        generalact.dragmouse(1000, 800, 1000, 300)
    generalact.imgcorrdinatefun('NIKKE\\iDoll.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun('NIKKE\\lvup.bmp', 0.9, 1500, 200, 1920, 1080)
    generalact.moveclick_1s(954, 844)
    backtonikke()
    generalact.imgcorrdinatefunde1('NIKKE\\longhair.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('NIKKE\\limitbreak.bmp', 0.9, 1500, 200, 1920, 1080)
    generalact.moveclick_1s(1789, 888)
    generalact.moveclick_1s(1789, 888)
    generalact.moveclick_1s(978, 829)  # 装备升级
    for i in range(3):
        generalact.moveclick_1s(763, 541)
        generalact.moveclick_2s(1056, 909)
    backtonikke()
    generalact.moveclick_1s(781, 220)

    generalact.moveclick_1s(1656, 137)
    generalact.moveclick_1s(368, 378)
    for i in range(10):
        generalact.moveclick_1s(1099, 900)  # 咨询
        generalact.moveclick_1s(1000, 680)
        consultation()
    generalact.moveclick_1s(163, 1024)  # home
    backtomainmenu()


def consultation():
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\consultation.bmp', 0.9, 0, 0, 1920, 1080):
            for i in range(10):
                generalact.moveclick_01s(965, 998)
            generalact.moveclick_1s(1885, 484)
            break
        else:
            for i in range(6):
                generalact.moveclick_01s(989, 733)


def backtonikke():
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\liberate.bmp', 0.9, 0, 90, 200, 200):
            break
        else:
            back1()


def shop():
    generalact.moveclick_1s(575, 747)  # shop
    backtoshop()
    for i in range(2):
        generalact.moveclick_1s(157, 687)
        shopbuyback()
        x = 0
        for j in range(4):
            generalact.moveclick_1s(298 + x, 654)
            while 1:
                if generalact.imgcorrdinatefuncount3('NIKKE\\shopcredit.bmp', 0.9, 700, 150, 500, 700):
                    shopbuyback()
                    break
                else:
                    backtoshop()
                    break
            x += 160
        if i == 1:
            break
        generalact.moveclick_1s(342, 492)
        generalact.imgcorrdinatefun('NIKKE\\confirm.bmp', 0.9, 600, 600, 1920, 1080)
    backtomainmenu()


def shopbuyback():
    generalact.imgcorrdinatefun('NIKKE\\buy.bmp', 0.9, 700, 850, 1920, 1080)
    backtoshop()


def collect():
    generalact.moveclick_1s(575, 897)
    generalact.imgcorrdinatefun('NIKKE\\huodejiangli.bmp', 0.9, 700, 850, 1920, 1080)
    backtomainmenu()
    generalact.moveclick_1s(575, 897)
    generalact.imgcorrdinatefun('NIKKE\\yijujianmie.bmp', 0.9, 700, 850, 1920, 1080)
    generalact.moveclick_1s(1037, 824)
    backtomainmenu()


def dispatch():
    generalact.moveclick_1s(604, 830)
    generalact.imgcorrdinatefunde1('NIKKE\\dispatch.bmp', 0.9, 600, 850, 1920, 1080)
    for i in range(5):
        generalact.moveclick_02s(1116, 902)
    for i in range(5):
        generalact.moveclick_02s(1005, 900)
    generalact.moveclick_1s(163, 1024)  # home
    generalact.moveclick_1s(163, 1024)  # home
    backtomainmenu()


def friend():
    generalact.imgcorrdinatefunde1('NIKKE\\friend.bmp', 0.9, 1600, 0, 1920, 1080)
    generalact.rangeclick02(3, 1149, 923)
    backtomainmenu()
    generalact.moveclick_1s(575, 897)
    generalact.imgcorrdinatefun('NIKKE\\huodejiangli.bmp', 0.9, 700, 850, 1920, 1080)
    backtomainmenu()
    generalact.moveclick_1s(1668, 113)
    generalact.rangeclick01(8, 1154, 970)
    backtomainmenu()
    generalact.moveclick_2s(561, 666)  # 付费商店
    generalact.imgcorrdinatefunde1('NIKKE\\Dgift.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(268, 313)
    generalact.moveclick_1s(127, 542)
    backtomainmenu()
    if generalact.firstDayOfWeek2():
        generalact.moveclick_2s(561, 666)  # 付费商店
        generalact.imgcorrdinatefunde1('NIKKE\\Dgift.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_1s(425, 313)
        generalact.moveclick_1s(127, 542)
        backtomainmenu()


def ALS():
    time.sleep(2)
    while 1:
        # generalact.imgcorrdinatefunwhilenotime('NIKKE\\ALS1.bmp', 0.2, 700, 500, 500, 500)
        # CSauto.mouseDown()
        # generalact.imgcorrdinatefunwhilenotime('NIKKE\\ALS2.bmp', 0.2, 700, 500, 500, 500)
        # time.sleep(0.055)
        # CSauto.mouseUp()
        # CSauto.click()
        CSauto.mouseDown()
        time.sleep(0.1)
        CSauto.mouseUp()


def backtomainmenu():
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\ID.bmp', 0.9, 670, 190, 1920, 1080) == 1:
            generalact.moveclick_1s(44, 46)
            break
        else:
            back1()
            generalact.moveclick_01s(44, 46)


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


def shopmax1():
    generalact.imgcorrdinatefun3('NIKKE\\MAX.bmp', 0.8, 700, 500, 1920, 1080)
    generalact.imgcorrdinatefun('NIKKE\\buy.bmp', 0.8, 700, 500, 1920, 1080)
    generalact.rangeclick01(4, 1760, 950)


def backtoshop():
    while 1:
        if generalact.imgcorrdinatefuncount('NIKKE\\shop.bmp', 0.9, 0, 0, 1920, 1080) == 1:
            backup1()
            break
        else:
            # break
            backup1()


def backup1():
    generalact.moveclick_1s(46, 37)




