import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag):
    if AFTD:
        enterWJXLfun()
        signup()
        shop()
        ship()
        employee()
        if huodongflag:
            huodong_1_3()
        else:
            explore()
    else:
        enterWJXLfun()
        ship()
        if huodongflag:
            huodong_1_3()
            pass
        else:
            explore()
        mission()
        gamepass()
        employee()
        mission()
    # generalact.MUMUmain()
    # generalact.MUMUdrag2()


def enterWJXLfun():
    generalact.logger.info('WJXLfun.enterWJXLfunF')
    n = 0
    generalact.ImgShiftWhileDelay1Cdelay1('WJXL\\WJXL.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    time.sleep(3)
    generalact.ImgFor3Cdelay1('WJXL\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    while 1:
        if generalact.ImgReturn1For3('WJXL\\UID.bmp', 0.8, 0, 0, 1920, 1080):
            time.sleep(1)
            break
        else:
            generalact.moveclick_1s(71, 82)
            generalact.ImgFor3Cdelay1('WJXL\\WJXLenterday.bmp', 0.9, 1700, 100, 1920, 1080)
            if generalact.ImgReturn1For3('WJXL\\login.bmp', 0.9, 0, 0, 1920, 1080):
                generalact.moveclick_1s(966, 647)  # 登陆
                generalact.moveclick_1s(773, 547)
                CSauto.hotkey('a', 'enter', interval=0.02)  # ctrl-c to copy
                time.sleep(0.2)
                CSauto.write("1181266134", interval=0.02)
                generalact.moveclick_1s(966, 647)  # 登陆
            n += 1
            if n >= 60:
                generalact.ImgShiftFor3Cdelay1('WJXL\\WJXL.bmp', 0.8, 0, 0, 1920, 1080, 0, -40)
                n = 0


def signup():
    while 1:
        if generalact.ImgFor3Cdelay1('WJXL\\signup.bmp', 0.9, 0, 0, 1920, 1080):
            break
        else:
            generalact.moveclick_1s(71, 82)
            generalact.ImgFor3Cdelay1('WJXL\\WJXLenterday.bmp', 0.9, 0, 0, 1920, 1080)
    backtomainui()


def shop():
    generalact.logger.info('WJXL.shop')
    generalact.ImgWhileCdelay1('WJXL\\shop.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\giftpackage.bmp', 0.9, 0, 0, 1920, 1080)
    for i in range(5):
        generalact.dragmouse(1781, 625, 515, 614)
    generalact.ImgWhileCdelay1('WJXL\\giftpackage_dailyfree.bmp', 0.9, 0, 0, 1920, 1080)
    shopbuy()
    generalact.ImgWhileCdelay1('WJXL\\supplystore.bmp', 0.9, 0, 0, 1920, 1080)
    while 1:
        if generalact.ImgFor3Cdelay1('WJXL\\supplystore_90.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        if generalact.ImgFor3Cdelay1('WJXL\\supplystore_50.bmp', 0.9, 0, 0, 1920, 1080):
            shopbuy()
        else:
            break
    backtomainui()


def shopbuy():
    generalact.ImgWhileCdelay1('WJXL\\shop_buy.bmp', 0.9, 0, 0, 1920, 1080)
    clickblock()


def ship():
    generalact.logger.info('WJXL.ship')
    generalact.ImgWhileCdelay2('WJXL\\ship.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1745, 1028)
    generalact.ImgWhileCdelay1('WJXL\\logistics.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_05s(511, 921)
    generalact.moveclick_05s(1700, 412)  # 加速
    generalact.moveclick_05s(1284, 674)
    generalact.moveclick_05s(1310, 814)
    backtomainui()


def mission():
    generalact.logger.info('WJXL.mission')
    generalact.ImgWhileCdelay1('WJXL\\mission.bmp', 0.9, 0, 0, 1920, 1080)
    # generalact.ImgWhileCdelay1('WJXL\\mission_get.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_05s(1660, 970)
    clickblock()
    generalact.moveclick_05s(1148, 91)
    generalact.moveclick_05s(1660, 970)
    clickblock()
    backtomainui()


def gamepass():
    generalact.moveclick_2s(1533, 422)
    generalact.moveclick_1s(500, 1000)
    generalact.moveclick_1s(1670, 880)  # mission get
    clickblock()
    generalact.moveclick_1s(575, 486)
    generalact.moveclick_1s(1670, 880)  # mission get
    clickblock()
    backtomainui()


def employee():
    generalact.logger.info('employee.ship')
    generalact.ImgWhileCdelay2('WJXL\\employee.bmp', 0.9, 0, 0, 1920, 1080)
    for i in range(2):
        generalact.dragmouse(248, 591, 192, 201)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\employee_free.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhile('WJXL\\employee_free1.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(20, 1726, 952)
    backtomainui()


def explore():
    generalact.logger.info('WJXL.explore')
    generalact.moveclick_1s(1730, 943)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\dailywork.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\bailiandilao.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(5)
    generalact.moveclick_1s(1027, 645)
    batquickall()


def backtomainui():
    generalact.moveclick_1s(345, 95)
    while 1:
        if generalact.ImgReturn1For3('WJXL\\UID.bmp', 0.9, 0, 0, 1920, 1080):
            time.sleep(1)
            break
        else:
            generalact.moveclick_1s(71, 82)
            generalact.ImgFor3Cdelay1('WJXL\\WJXLenterday.bmp', 0.9, 0, 0, 1920, 1080)


def back1():
    generalact.moveclick_1s(70, 80)


def back2():
    generalact.moveclick_2s(70, 80)


def back3():
    generalact.moveclick_3s(70, 80)


def clickblock():
    generalact.rangeclick01(6, 941, 1064)


def batquickall():
    generalact.logger.info('WJXL.batquickall')
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\come.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\max.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\start.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\startbat.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\startbat1.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\bat\\escape.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(2)
    generalact.ImgFor3Cdelay1('WJXL\\bat\\escape.bmp', 0.9, 0, 0, 1920, 1080)
    backtomainui()


def huodong_1_3():
    generalact.logger.info('WJXL.huodong_1_3')
    generalact.moveclick_1s(1617, 289)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\huodong\\1_3\\up.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    if generalact.ImgFor3Cdelay1('WJXL\\huodong\\1_3\\up_4.bmp', 0.9, 0, 0, 1920, 1080):
        time.sleep(1)
    else:
        generalact.moveclick_1s(985, 560)
    batquickall()


def huodong_1_2():
    generalact.logger.info('WJXL.huodong_1_2')
    generalact.moveclick_1s(1617, 289)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\huodong\\1_2\\up.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    for i in range(2):
        generalact.dragmouse(915, 886, 915, 86)
    if generalact.ImgFor3Cdelay1('WJXL\\huodong\\1_2\\up_7.bmp', 0.9, 0, 0, 1920, 1080):
        time.sleep(1)
    else:
        generalact.moveclick_1s(985, 560)
    batquickall()


def huodong_1_1():
    generalact.logger.info('WJXL.huodong_1_1')
    generalact.moveclick_1s(1617, 289)
    generalact.ImgWhileDelay1Cdelay1('WJXL\\huodong\\1_1\\down.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(3)
    if generalact.ImgFor3Cdelay1('WJXL\\huodong\\1_1\\down1.bmp', 0.9, 0, 0, 1920, 1080):
        time.sleep(1)
    else:
        generalact.moveclick_1s(985, 560)
    batquickall()

