import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag, resourceflag):
    if AFTD:
        entergalacticrealmfun()
        levelup()
        shipaffairs()
        ship_dinner(AFTD)
        shopFM()
        TacticalModule()
        huodong(huodongflag, resourceflag)
    else:
        entergalacticrealmfun()
        shipaffairsN()
        mission()
        huodong(huodongflag, resourceflag)
    generalact.MUMUmain()
    generalact.MUMUdrag2()


def entergalacticrealmfun():
    generalact.logger.info('GalacticRealmFun.entergalacticrealmfun')
    galacticrealmicon()
    n = 0
    # while 1:
    #     if generalact.comparecolorsnest2count5(488, 783, 78, 56, 33, 1226, 691, 254, 167, 45) == 1:
    #         break
    #     else:
    #         generalact.moveclick_1s(960, 741)
    #         back1()
    #         n += 1
    #         print(n)
    #         if n % 60 == 0:
    #             # generalact.ImgShiftFor3Cdelay1('Galactic_realm\\GalacticRealm.bmp',
    #             #                                             0.8, 42, 181, 1780, 1000, 0, -40)
    #             generalact.MUMUclose1()
    #             generalact.MUMUclose1()
    #             galacticrealmicon()
    #         if n % 300 == 0:
    #             CSauto.hotkey('alt', 'f4')
    #             generalact.startupMUMU(generalact.MUMUpath, 40)
    #             galacticrealmicon()
    generalact.moveclick_3s(1202, 678)
    generalact.moveclick_3s(1202, 678)
    generalact.moveclick_3s(52, 65)
    backtomainui()


def galacticrealmicon():
    generalact.ImgShiftWhileDelay1Cdelay1('Galactic_realm\\GalacticRealm.bmp', 0.8, 42, 181, 1780, 1000, 0, -40)
    time.sleep(3)
    if generalact.ImgReturn1For3('RE1999\\download.bmp', 0.9, 0, 0, 1920, 1080):
        generalact.moveclick_1s(960, 746)


def levelup():
    generalact.logger.info('GalacticRealmFun.levelup')
    generalact.moveclick_1s(1251, 524)  # 角色
    generalact.moveclick_1s(1387, 77)
    generalact.moveclick_2s(240, 452)
    generalact.moveclick_1s(1633, 957)  # 升级
    generalact.moveclick_1s(1830, 689)
    generalact.moveclick_1s(1758, 972)
    back1()
    back1()
    generalact.moveclick_1s(1387, 77)
    backtomainui()


def shipaffairs():
    generalact.logger.info('GalacticRealmFun.shipaffairs')
    generalact.moveclick_1s(1361, 317)  # 舰务
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_eco.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhile('Galactic_realm\\ship_eco1.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 1810, 1020)
    if generalact.firstDayOfWeek():
        # ship_eco(400, 430)
        ship_eco(620, 430)  # 黄瓜
    if generalact.firstDayOfWeek2():
        ship_eco(830, 430)  # 茶树
    if generalact.firstDayOfWeek3():
        ship_eco(175, 650)  # 洋葱
    if generalact.firstDayOfWeek4():
        ship_eco(400, 630)  # 水稻
    if generalact.firstDayOfWeek5():
        ship_eco(620, 630)  # 番茄
    if generalact.firstDayOfWeek6():
        ship_eco(830, 630)  # 小麦
    if generalact.firstDayOfWeek7():
        ship_eco(175, 430)  # 玉米
    back2()
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_proving.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(2)
    generalact.moveclick_1s(965, 987)
    generalact.moveclick_1s(1600, 1035)
    generalact.rangeclick01(6, 1130, 1058)
    # generalact.moveclick_1s(222, 977)
    generalact.moveclick_1s(519, 874)  # 前往生产
    generalact.moveclick_1s(1126, 851)
    generalact.moveclick_1s(1126, 851)
    generalact.moveclick_1s(1126, 851)
    generalact.moveclick_1s(1342, 852)
    generalact.moveclick_1s(1342, 852)
    backtomainui()


def shipcomcenter():
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_comcenter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay2('Galactic_realm\\ship_comcenter1.bmp', 0.9, 0, 0, 1920, 1080)
    while 1:
        time.sleep(3)
        if generalact.ImgReturn1For3('Galactic_realm\\ship_comcenter_0.bmp',
                                             0.95, 1500, 40, 1920, 1080):
            break
        if generalact.ImgShiftFor3Cdelay1('Galactic_realm\\ship_comcenter_3.bmp',
                                                       0.95, 980, 1000, 1920, 1080, 0, -100):
            generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_comcenterfinish.bmp', 0.9, 0, 0, 1920, 1080)
            generalact.ImgWhile('Galactic_realm\\ship_comcenter_get.bmp', 0.9, 0, 0, 1920, 1080)
            generalact.moveclick_05s(986, 938)
            generalact.dragmouse(986, 938, 1091, 247)
            generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\skip.bmp', 0.9, 0, 0, 1920, 1080)
            continue
        if generalact.ImgShiftFor3Cdelay1('Galactic_realm\\ship_comcenter_4.bmp',
                                                       0.9, 980, 1000, 1920, 1080, 0, -100):
            generalact.moveclick_05s(1456, 578)
            generalact.moveclick_05s(1069, 912)
            generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_comcenterfinish.bmp', 0.9, 0, 0, 1920, 1080)
            generalact.ImgWhile('Galactic_realm\\ship_comcenter_get.bmp', 0.9, 0, 0, 1920, 1080)
            generalact.rangeclick01(5, 1009, 927)
            generalact.dragmouse(986, 938, 1091, 247)
            generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\skip.bmp', 0.9, 0, 0, 1920, 1080)
        else:
            break
    back2()
    back2()


def shipaffairsN():
    generalact.logger.info('GalacticRealmFun.shipaffairsN')
    generalact.moveclick_1s(1361, 317)  # 舰务
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_eco.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhile('Galactic_realm\\ship_eco1.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 1810, 1020)
    if generalact.firstDayOfWeek7():
        ship_eco(400, 430)
    back2()
    shipcomcenter()
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_proving.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(2)
    generalact.moveclick_1s(965, 987)
    generalact.moveclick_1s(1600, 1035)
    generalact.rangeclick01(6, 1130, 1058)
    # generalact.moveclick_1s(340, 971)
    generalact.moveclick_1s(519, 874)  # 前往生产
    generalact.moveclick_1s(1126, 851)
    generalact.moveclick_1s(1126, 851)
    generalact.moveclick_1s(1126, 851)
    generalact.moveclick_1s(1342, 852)
    generalact.moveclick_1s(1342, 852)
    backtomainui()


def ship_dinner(AFTD):
    if generalact.firstDayOfWeek5() and AFTD:
        generalact.logger.info('GalacticRealmFun.ship_dinner')
        generalact.moveclick_1s(1361, 317)  # 舰务
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_dinner.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\ship_dinner_cook.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.movemouse(770, 287)
        for i in range(6):
            generalact.dragmouse(775, 1000, 775, 200)
        time.sleep(1)
        generalact.rangeclick01(2, 1170, 900)
        generalact.moveclick_1s(1590, 990)
        generalact.rangeclick02(4, 1150, 900)
        generalact.moveclick_1s(955, 1015)
        backtomainui()


def ship_eco(x, y):
    generalact.moveclick_05s(790, 1010)  # 1
    generalact.moveclick_05s(x, y)
    generalact.moveclick_1s(545, 1020)
    generalact.moveclick_05s(950, 1010)  # 2
    generalact.moveclick_05s(x, y)
    generalact.moveclick_1s(545, 1020)
    generalact.moveclick_05s(1100, 1010)  # 3
    generalact.moveclick_05s(x, y)
    generalact.moveclick_1s(545, 1020)
    generalact.moveclick_05s(1280, 1010)  # 4
    generalact.moveclick_05s(x, y)
    generalact.moveclick_1s(545, 1020)
    generalact.moveclick_05s(1430, 1010)  # 5
    generalact.moveclick_05s(x, y)
    generalact.moveclick_1s(545, 1020)
    generalact.moveclick_05s(1600, 1010)  # 6
    generalact.moveclick_05s(x, y)
    generalact.moveclick_1s(545, 1020)


def mission():
    generalact.logger.info('GalacticRealmFun.mission')
    generalact.moveclick_05s(1469, 983)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\mission_get.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1600, 980)
    generalact.moveclick_05s(160, 433)
    generalact.rangeclick01(10, 1600, 980)
    generalact.moveclick_05s(160, 590)
    generalact.rangeclick01(10, 1338, 978)
    backtomainui()


def shopFM():
    if generalact.firstDayOfMonth3():
        generalact.logger.info('GalacticRealmFun.shopFM')
        generalact.moveclick_1s(1350, 700)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\tehuilibao.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\tehuilibao_jichubugeibao.bmp', 0.9, 0, 0, 1920, 1080)
        shopbuy()
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\supplystore.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\supplystore_exchange.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(1270, 945)
        clickblock()
        shopbuymove(586, 386, 6)  # 1L1R
        generalact.moveclick_05s(690, 208)  # Middle supply
        shopbuymove(911, 436, 1)  # 1L2R
        generalact.moveclick_05s(1100, 200)  # Tactical Module
        shopbuymove(577, 740, 1)  # 2L1R
        backtomainui()


def TacticalModule():
    if generalact.firstDayOfMonth():
        generalact.logger.info('GalacticRealmFun.TacticalModule')
        generalact.moveclick_1s(1790, 995)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\storage_module.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1700, 1000)  # discard
        for i in range(4):
            generalact.moveclick_1s(885, 223)  # quick choice
            generalact.moveclick_1s(850, 335)  # 1 level module
            generalact.rangeclick02(2, 1700, 1000)  # discard
            clickblock()
        for i in range(2):
            generalact.moveclick_1s(885, 223)  # quick choice
            generalact.moveclick_1s(830, 420)  # 2 level module
            generalact.rangeclick02(2, 1700, 1000)  # discard
            clickblock()
        backtomainui()


def shopbuymove(x, y, count):
    for i in range(count):
        generalact.moveclick_05s(x, y)
        generalact.moveclick_05s(1446, 565)
        generalact.moveclick_05s(1300, 911)
        clickblock()


def shopbuy():
    generalact.moveclick_05s(1446, 565)
    generalact.moveclick_05s(1300, 911)
    clickblock()


def clickblock():
    generalact.rangeclick01(6, 941, 1064)


def huodongshop():
    while 1:
        generalact.moveclick_05s(1731, 511)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\shop_max.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(1321, 899)
        generalact.rangeclick01(6, 1126, 1040)


def batagain():
    generalact.ImgWhile('Galactic_realm\\bat_again.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(5, 1226, 659)


def autobat():
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\bat_autobatH.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\bat_batstartH.bmp', 0.9, 0, 0, 1920, 1080)


def huodong(huodongflag, resourceflag):
    if huodongflag:
        huodong1_6()
    else:
        generalact.moveclick_1s(1654, 505)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\houqing.bmp', 0.9, 0, 0, 1920, 1080)
        if resourceflag == 0:  # money
            generalact.moveclick_1s(403, 602)
            generalact.moveclick_1s(1264, 544)
            autobat()
            batagain()
            generalact.moveclick_1s(682, 640)
            autobat()
        if resourceflag == 1:  # exp
            generalact.moveclick_1s(958, 602)
            generalact.moveclick_1s(1264, 644)
            autobat()
            batagain()
            generalact.moveclick_1s(682, 640)
            autobat()
        if resourceflag == 2:
            generalact.moveclick_1s(1453, 602)


def xinghaixunyou():
    while 1:
        generalact.ImgWhile('Galactic_realm\\xinghaixunyou\\XHXY_notes.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1540, 860)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_skip.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1150, 720)
        generalact.ImgWhile('Galactic_realm\\xinghaixunyou\\XHXY_confirm.bmp', 0.9, 0, 0, 1920, 1080)
        for i in range(4):
            if generalact.ImgFor3Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_30.bmp',
                                                      0.9, 0, 0, 1920, 1080):
                pass
            else:
                generalact.moveclick_05s(645, 600)
            generalact.moveclick_05s(960, 970)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_confirm1.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_yellow.bmp', 0.8, 0, 0, 800, 1080)
        generalact.moveclick_05s(1570, 700)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_Deploymentactions.bmp', 0.9, 0, 0, 1920,
                                       1080)
        generalact.moveclick_05s(1200, 770)
        generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_batstart.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(1200, 770)
        generalact.ImgWhile('Galactic_realm\\xinghaixunyou\\BAT_skip.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1525, 115)
        while 1:
            if generalact.ImgFor3Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_continue.bmp',
                                                      0.8, 0, 0, 1920, 1080):
                generalact.moveclick_05s(430, 600)
                generalact.moveclick_05s(660, 400)
                generalact.moveclick_05s(1750, 1030)
                generalact.moveclick_1s(1180, 960)
                generalact.moveclick_05s(1600, 585)
                generalact.moveclick_1s(1200, 770)
                break
            if generalact.ImgFor3Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_fail.bmp',
                                                      0.8, 0, 0, 1920, 1080):
                generalact.moveclick_05s(777, 766)
                break
        generalact.ImgWhile('Galactic_realm\\xinghaixunyou\\XHXY_chuzhan.bmp', 0.9, 0, 0, 1920, 1080)
        if generalact.ImgFor3Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_shop.bmp',
                                                  0.9, 0, 0, 1920, 1080):
            generalact.moveclick_1s(1440, 680)
            generalact.moveclick_1s(1700, 835)
            generalact.moveclick_1s(1290, 775)
        generalact.moveclick_1s(610, 90)
        generalact.moveclick_1s(1200, 760)
        generalact.moveclick_1s(1760, 600)
        generalact.moveclick_1s(1760, 600)


def xinghaixunyou_map():
    if generalact.ImgFor3Cdelay1('Galactic_realm\\xinghaixunyou\\XHXY_zhongcheng.bmp',
                                              0.9, 0, 0, 1920, 1080):
        generalact.moveclick_1s(1440, 701)
        generalact.moveclick_1s(434, 1000)
        generalact.moveclick_05s(660, 400)
        generalact.moveclick_05s(1750, 1030)
        generalact.rangeclick02(2, 700, 580)


def fish(counter):
    for i in range(counter):
        # generalact.comparecolorsnest2while(1133, 860, 250, 1134, 831, 255, 255, 255)
        pass


def backtomainui():
    while 1:
        if generalact.ImgReturn1For5('Galactic_realm\\ID.bmp', 0.9, 1100, 83, 1878, 984) == 1:
            back3()
            break
        else:
            # break
            back1()


def back1():  # 返回
    generalact.moveclick_1s(71, 73)


def back2():  # 返回
    generalact.moveclick_2s(71, 73)


def back3():  # 返回
    generalact.moveclick_3s(71, 73)


def huodong1_6():
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.6\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.6\\map.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.6\\money.bmp', 0.9, 0, 0, 1920, 1080)
    # generalact.moveclick_1s(1241, 532)
    autobat()
    batagain()
    generalact.moveclick_1s(682, 640)
    autobat()


def huodong1_5_1():
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.5.1\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.5.1\\map.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.5.1\\exp.bmp', 0.9, 0, 0, 1920, 1080)
    # generalact.moveclick_1s(1241, 532)
    autobat()
    batagain()
    generalact.moveclick_1s(682, 640)
    autobat()


def huodong1_5():
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.5\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.5\\zhanbei.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.5\\fangshou.bmp', 0.9, 0, 0, 1920, 1080)
    # generalact.moveclick_1s(1241, 532)
    autobat()
    batagain()
    generalact.moveclick_1s(682, 640)
    autobat()


def huodong1_4():
    generalact.moveclick_1s(151, 737)
    generalact.ImgWhileDelay1Cdelay1('Galactic_realm\\huodong\\ver1.4\\weijinzhilu.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1241, 532)
    autobat()
    batagain()
    generalact.moveclick_1s(682, 640)
    autobat()
