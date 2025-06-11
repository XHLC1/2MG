import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]

# imgcoordinate = CSauto.locateCenterOnScreen('vectory.bmp', confidence=0.9, region=(1145, 130, 1610, 300))
# generalact.logger.info(imgcoordinate)
# generalact.ImgWhileCdelay1('vectory.bmp', 0.9, 1145, 130, 1610, 300)


def dailytaskst(AFTD, huodongflag, resourceflag):
    enter1999fun()
    signinfun()
    if AFTD:
        levelup()
        signM()
        shopM()
        willanalysis()
        poussiere(huodongflag, resourceflag)
    else:
        poussiere(huodongflag, resourceflag)
        mission()
        gamepass()
        somnambulism()
    generalact.MUMUclose1()
    generalact.MUMUdrag2()


def enter1999fun():
    generalact.logger.info('RE1999Fun.enter1999fun')
    generalact.ImgShiftWhileDelay1Cdelay1('RE1999\\RE1999.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    # generalact.moveclick_3s(1283, 328)  # 1-4
    time.sleep(15)
    generalact.ImgFor3Cdelay1('RE1999\\download.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainuienter()
    generalact.rangeclick01(5, 930, 538)


def signinfun():
    generalact.logger.info('RE1999Fun.signinfun')
    generalact.moveclick_05s(1484, 620)  # 不休荒原
    generalact.ImgWhile('RE1999\\wilderness.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgReturn1For3('RE1999\\wilderness.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(1)
    generalact.moveclick_1s(747, 205)  # 微小
    generalact.moveclick_1s(1161, 152)  # 利齿
    # generalact.moveclick_1s(800, 268)
    # generalact.moveclick_1s(1133, 199)
    generalact.moveclick_3s(116, 338)
    back1()
    generalact.rangeclick01(20, 1464, 630)
    generalact.ImgReturn1For3('RE1999\\wilderness.bmp', 0.8, 0, 0, 1920, 1080)
    # generalact.ImgWhileDelay1Cdelay1('RE1999\\wilderness.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(747, 205)  # 微小
    generalact.moveclick_1s(1161, 152)  # 利齿
    # generalact.moveclick_1s(800, 268)
    # generalact.moveclick_1s(1133, 199)
    backtomainui()
    # generalact.moveclick_05s(1484, 620)  # 不休荒原
    # generalact.ImgWhile('RE1999\\wilder_P_produce.bmp', 0.8, 0, 0, 1920, 1080)
    # generalact.ImgWhileDelay1Cdelay1('RE1999\\wilder_P_produce.bmp', 0.8, 0, 0, 1920, 1080)
    # generalact.moveclick_1s(1512, 311)
    # clickblock()
    # generalact.moveclick_1s(666, 985)  # 员工
    # while 1:
    #     if generalact.ImgFor3Cdelay1('RE1999\\wilder_P_produce_E.bmp', 0.9, 0, 0, 1920, 1080):
    #         pass
    #     else:
    #         clickblock()
    #         break
    # generalact.moveclick_1s(1234, 985)  # 产品
    # generalact.rangeclick02(4, 945, 860)
    # backtomainui()


def signM():
    if generalact.firstDayOfMonth7():
        generalact.logger.info('RE1999Fun.signM')
        generalact.moveclick_1s(132, 817)
        generalact.moveclick_2s(361, 877)  # sign
        generalact.rangeclick01(4, 268, 861)
        backtomainui()
    if generalact.firstDayOfMonth15():
        generalact.logger.info('RE1999Fun.signM')
        generalact.moveclick_1s(132, 817)
        generalact.moveclick_2s(361, 877)  # sign
        generalact.rangeclick01(4, 415, 851)
        backtomainui()
    if generalact.firstDayOfMonth25():
        generalact.logger.info('RE1999Fun.signM')
        generalact.moveclick_1s(132, 817)
        generalact.moveclick_2s(361, 877)  # sign
        generalact.rangeclick01(4, 572, 861)
        backtomainui()


def shopM():
    if generalact.firstDayOfMonth():
        generalact.logger.info('RE1999Fun.shopM')
        generalact.moveclick_1s(147, 659)
        generalact.ImgWhileDelay1Cdelay1('RE1999\\shop_pawnshop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('RE1999\\shop_pawnshop_L1.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('RE1999\\shop_pawnshop_L2.bmp', 0.9, 0, 0, 1920, 1080)
        if generalact.ImgFor3Cdelay1('RE1999\\shop_pawnshop_L_1.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        if generalact.ImgFor3Cdelay1('RE1999\\shop_pawnshop_L_2.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        if generalact.ImgFor3Cdelay1('RE1999\\shop_pawnshop_L_3.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        if generalact.ImgFor3Cdelay1('RE1999\\shop_pawnshop_L_4.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        #############################################碎片叙事############################################################
        generalact.ImgWhileDelay1Cdelay1('RE1999\\shop_frameshop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_P1.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_P2.bmp', 0.9, 0, 0, 1920, 1080)
        if generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_P_1.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        while 1:
            if generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_P_2.bmp', 0.9, 0, 0, 1920, 1080):
                shopbuy()
                break
            else:
                generalact.dragmouse(1090, 900, 1090, 600)
        generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_D1.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_D2.bmp', 0.9, 0, 0, 1920, 1080)
        if generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_D_1.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        if generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_D_1.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        if generalact.ImgFor3Cdelay1('RE1999\\shop_frameshop_D_2.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        #############################################碎片叙事############################################################
        backtomainui()


def shopbuy():
    generalact.moveclick_1s(1413, 725)
    generalact.ImgWhileCdelay1('RE1999\\shop_buy.bmp', 0.8, 0, 0, 1920, 1080)
    clickblock()


def levelup():
    generalact.logger.info('RE1999Fun.levelup')
    generalact.moveclick_1s(1682, 610)  # 角色
    generalact.moveclick_1s(1092, 108)
    generalact.moveclick_1s(343, 420)
    generalact.moveclick_1s(1461, 260)
    generalact.moveclick_1s(1575, 841)
    back1()
    back1()
    generalact.moveclick_1s(1092, 108)
    back1()
    backtomainui()


def willanalysis():
    generalact.logger.info('RE1999Fun.willanalysis')
    generalact.moveclick_1s(1686, 525)  # 入场
    generalact.rangeclick02(3, 750, 990)  # 4
    generalact.ImgWhileDelay1Cdelay1('RE1999\\resource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(504, 572)  # 意志解析
    generalact.moveclick_1s(654, 899)
    generalact.moveclick_1s(1467, 920)  # 开始行动
    batconfirm2()
    battlevectory()
    backtomainui()


def poussiere(huodongflag, resourceflag):
    generalact.logger.info('RE1999Fun.poussiere')
    if huodongflag:
        huodong2_7()
    else:
        if resourceflag == 1:
            generalact.moveclick_1s(1686, 525)  # 入场
            generalact.ImgWhileDelay1Cdelay1('RE1999\\resource.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.ImgWhileDelay1Cdelay1('RE1999\\resource_porssiere.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.moveclick_1s(654, 899)
            generalact.moveclick_1s(1467, 920)  # 开始行动
            batconfirm4()
            battlevectory()
            generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
            batconfirm2()
            if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
                pass
            else:
                battlevectory()
        if resourceflag == 2:
            generalact.moveclick_1s(1686, 525)  # 入场
            generalact.ImgWhileDelay1Cdelay1('RE1999\\resource.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.ImgWhileDelay1Cdelay1('RE1999\\resource_mintage.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.moveclick_1s(654, 899)
            generalact.moveclick_1s(1467, 920)  # 开始行动
            batconfirm4()
            battlevectory()
            generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
            batconfirm2()
            if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
                pass
            else:
                battlevectory()
        if resourceflag == 3:
            generalact.moveclick_1s(1686, 525)  # 入场
            generalact.ImgWhileDelay1Cdelay1('RE1999\\resource.bmp', 0.8, 0, 0, 1920, 1080)
            for i in range(2):
                generalact.dragmouse(1644, 536, 131, 580)
            generalact.ImgWhileDelay1Cdelay1('RE1999\\resource_analy.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.moveclick_1s(654, 899)
            generalact.moveclick_1s(1467, 920)  # 开始行动
            batconfirm4()
            battlevectory()
            generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
            batconfirm2()
            if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
                pass
            else:
                battlevectory()
    backtomainui()
    misihai()


def misihai():
    if generalact.firstDayOfWeek():
        generalact.moveclick_1s(1686, 525)  # 入场
        generalact.ImgWhileDelay1Cdelay1('RE1999\\yuzhongxuanxiang.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('RE1999\\yuzhongxuanxiang_misihai.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgWhile('RE1999\\yuzhongxuanxiang_misihai_skip.bmp', 0.8, 0, 0, 1920, 1080)
        time.sleep(3)
        generalact.ImgWhileDelay1Cdelay1('RE1999\\yuzhongxuanxiang_misihai_skip.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1229, 740)
        generalact.moveclick_1s(1237, 392)
        generalact.moveclick_1s(1525, 742)
        clickblock()
        backtomainui()


def somnambulism():
    generalact.logger.info('RE1999Fun.rengongmengyou')
    if generalact.firstDayOfWeek():
        generalact.moveclick_1s(1686, 525)  # 入场
        generalact.ImgWhileDelay1Cdelay1('RE1999\\resource.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('RE1999\\resource_somnambulism.bmp', 0.8, 0, 0, 1920, 1080)
        clickblock()
        generalact.rangeclick02(4, 335, 250)
        generalact.rangeclick02(6, 1550, 365)
        backtomainui()


def mission():
    generalact.logger.info('RE1999Fun.mission')
    generalact.moveclick_1s(150, 430)  # 任务
    generalact.ImgWhileDelay1Cdelay1('RE1999\\dailymission.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1740, 270)
    generalact.rangeclick01(10, 870, 1015)
    generalact.moveclick_1s(1680, 133)  # 每周活跃
    generalact.moveclick_1s(1740, 270)
    generalact.rangeclick01(6, 241, 101)
    backtomainui()


def gamepass():
    for i in range(3):
        generalact.ImgFor3Cdelay1('RE1999\\gamepass.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('RE1999\\gamepass1.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('RE1999\\gamepass2.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    if generalact.ImgFor3Cdelay1('RE1999\\pass_get.bmp', 0.9, 0, 0, 1920, 1080):
        clickblock()
    backtomainui()


def clickblock():
    generalact.rangeclick01(6, 941, 1064)


def batconfirm4():
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    if generalact.ImgReturn1For3('RE1999\\replay.bmp', 0.9, 590, 151, 1371, 868) == 1:
        generalact.moveclick_1s(1258, 988)
        generalact.moveclick_1s(1255, 640)  # 4
        generalact.moveclick_1s(1600, 1000)
    else:
        generalact.moveclick_1s(925, 990)
        generalact.moveclick_1s(1240, 990)
        generalact.moveclick_1s(1245, 645)  # 4
        generalact.moveclick_1s(1600, 1000)
        generalact.moveclick_1s(1600, 1000)


def batconfirm2():
    generalact.ImgWhile('RE1999\\goal.bmp', 0.9, 0, 0, 1920, 1080)
    if generalact.ImgReturn1For3('RE1999\\replay.bmp', 0.9, 590, 151, 1371, 868) == 1:
        generalact.moveclick_1s(1258, 988)
        generalact.moveclick_1s(1262, 826)  # 2
        generalact.moveclick_1s(1600, 1000)
    else:
        generalact.moveclick_1s(925, 990)
        generalact.moveclick_1s(1240, 990)
        generalact.moveclick_1s(1246, 820)  # 2
        generalact.moveclick_1s(1600, 1000)
        generalact.moveclick_1s(1600, 1000)


def backtomainui():
    n = 0
    while 1:
        if generalact.ImgReturn1For5('RE1999\\me.bmp', 0.7, 590, 151, 1371, 868) == 1:
            back3()
            break
        else:
            n += 1
            if n > 10:
                pass
            # break
            back1()


def backtomainuienter():
    n = 0
    while 1:
        if generalact.ImgFor3Cdelay1('RE1999\\me.bmp', 0.7, 590, 151, 1371, 868) == 1:
            back3()
            break
        else:
            # break
            back1()
            n += 1
            if n >= 80:
                generalact.ImgShiftFor3Cdelay1('RE1999\\RE1999.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
                generalact.MUMUclose1()
                generalact.MUMUclose1()
                generalact.ImgShiftWhileDelay1Cdelay1('RE1999\\RE1999.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
                time.sleep(15)
                generalact.ImgFor3Cdelay1('RE1999\\download.bmp', 0.8, 0, 0, 1920, 1080)
                n = 0


def battlevectory():
    generalact.ImgWhileCdelay1('RE1999\\vectory.bmp', 0.9, 1145, 130, 1610, 300)
    back1()
    back1()
    clickblock()


def back1():  # 返回
    generalact.moveclick_1s(105, 103)


def back2():  # 返回
    generalact.moveclick_2s(105, 103)


def back3():  # 返回
    generalact.moveclick_3s(105, 103)


def huodong2_7():  # 1987宇宙组曲
    count = 0
    generalact.logger.info('RE1999Fun.huodong2_7')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE2.7\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(5)
    while 1:
        if generalact.ImgFor3Cdelay1('RE1999\\huodong\\RE2.7\\18.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            count += 1
            if count < 12:
                generalact.dragmouse(1720, 915, 165, 895)
            else:
                generalact.dragmouse(165, 915, 1720, 895)
            time.sleep(1)
    generalact.rangeclick02(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong2_5():  # 唐人街影话
    count = 0
    generalact.logger.info('RE1999Fun.huodong2_5')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE2.5\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(5)
    while 1:
        if generalact.ImgFor3Cdelay1('RE1999\\huodong\\RE2.5\\18.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            count += 1
            if count < 12:
                generalact.dragmouse(1720, 915, 165, 895)
            else:
                generalact.dragmouse(165, 915, 1720, 895)
            time.sleep(1)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong2_4():  # 东区黎明
    count = 0
    generalact.logger.info('RE1999Fun.huodong2_4')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE2.4\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(5)
    while 1:
        if generalact.ImgFor3Cdelay1('RE1999\\huodong\\RE2.4\\18.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            count += 1
            if count < 12:
                generalact.dragmouse(1720, 915, 165, 895)
            else:
                generalact.dragmouse(165, 915, 1720, 895)
            time.sleep(1)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong2_3():  # 东区黎明
    count = 0
    generalact.logger.info('RE1999Fun.huodong2_3')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE2.3\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(5)
    while 1:
        if generalact.ImgFor3Cdelay1('RE1999\\huodong\\RE2.3\\18.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            count += 1
            if count < 8:
                generalact.dragmouse(1720, 915, 165, 895)
            else:
                generalact.dragmouse(165, 915, 1720, 895)
            time.sleep(1)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong2_1():  # 77号往事
    count = 0
    generalact.logger.info('RE1999Fun.huodong2_1')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE2.1\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(5)
    while 1:
        if generalact.ImgFor3Cdelay1('RE1999\\huodong\\RE2.1\\18.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            count += 1
            if count < 8:
                generalact.dragmouse(1720, 915, 165, 895)
            else:
                generalact.dragmouse(165, 915, 1720, 895)
            time.sleep(1)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong2_0():  # 飞驰，明日之城
    generalact.logger.info('RE1999Fun.huodong2_0')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE2.0\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    while 1:
        if generalact.ImgFor3Cdelay1('RE1999\\huodong\\RE2.0\\18.bmp', 0.9, 0, 0, 1920, 1080):
            break
        else:
            generalact.dragmouse(1720, 915, 165, 895)
            time.sleep(1)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong1_7():  # 再见，来亚什基
    generalact.logger.info('RE1999Fun.huodong1_7')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE1.7\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    if generalact.ImgFor3Cdelay1('RE1999\\huodong\\RE1.7\\16.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        generalact.moveclick_1s(100, 896)
        generalact.moveclick_1s(100, 896)
        generalact.moveclick_1s(100, 896)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong1_6():
    generalact.logger.info('RE1999Fun.huodong1_6')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE1.6\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE1.6\\19.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong1_5():
    generalact.logger.info('RE1999Fun.huodong1_5')
    generalact.moveclick_1s(1550, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE1.5\\RE1.5_Lfire.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE1.5\\RE1.5_com_13.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def huodong1_4_37():
    generalact.moveclick_1s(1600, 355)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE1.4_qishi.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1660, 616)
    generalact.moveclick_1s(1280, 727)
    batconfirm4()
    battlevectory()
    backtomainui()


def huodong1_2():
    generalact.logger.info('RE1999Fun.huodong1_2')
    generalact.moveclick_2s(1422, 265)  # 入场
    generalact.moveclick_1s(1580, 970)  # 入场
    generalact.ImgWhileDelay1Cdelay1('RE1999\\huodong\\RE1.2\\17.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(5, 1800, 400)
    generalact.moveclick_1s(1545, 946)
    batconfirm4()
    battlevectory()
    generalact.ImgWhile('RE1999\\energy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1506, 999)
    if generalact.ImgReturn1For3('RE1999\\getenergy.bmp', 0.9, 0, 0, 1920, 1080):
        pass
    else:
        battlevectory()


def test():
    generalact.moveclick_05s(1484, 620)  # 不休荒原
    generalact.ImgWhile('RE1999\\wilderness.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('RE1999\\wilderness.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(747, 205)  # 微小
    generalact.moveclick_1s(1161, 152)  # 利齿
    # generalact.moveclick_1s(800, 268)
    # generalact.moveclick_1s(1133, 199)
    generalact.moveclick_3s(116, 338)
    back1()
    generalact.rangeclick01(20, 1464,630)
    backtomainui()
