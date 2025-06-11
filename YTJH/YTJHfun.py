import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag, shopflag):
    if AFTD:
        enterYTJHf()
        oasis()
        character()
        shop(shopflag)
        explore(1, 1)
        huodong(huodongflag, 0)
        if huodongflag == 0:
            generalact.MUMUclose1()
            generalact.MUMUdrag2()
        else:
            generalact.MUMUclose1()
            generalact.MUMUdrag2()
    else:
        enterYTJHf()
        oasis()
        generalact.moveclick_1s(1564, 811)
        shopcoin_night(0)
        factory()
        dormroom()
        # YGXZ()
        huodong(huodongflag, 1)
        guzhangxieyi()
        generalact.MUMUclose1()
        generalact.MUMUdrag2()


def enterYTJHf():
    generalact.logger.info('YTJHfun.enterYTJHf')
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\YTJH.bmp', 0.8, 0, 0, 1920, 1080, 0, -40)
    n = 0
    while 1:
        if generalact.ImgFor3Cdelay1('YTJH\\entergame.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            time.sleep(1)
            n += 1
            if n >= 60:
                generalact.ImgShiftFor3Cdelay1('YTJH\\YTJH.bmp', 0.8, 0, 0, 1920, 1080, 0, -40)
                n = 0
    time.sleep(5)
    generalact.ImgFor3Cdelay1('YTJH\\entergame2.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1811, 190)
    backtomainui1()


def enterYTJH():
    generalact.logger.info('YTJHfun.enterYTJH')
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\YTJH.bmp', 0.8, 0, 0, 1920, 1080, 0, -40)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\entergame.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1811, 190)
    backtomainui()


def oasis():
    generalact.logger.info('YTJHfun.oasis')
    generalact.ImgWhileDelay1Cdelay1('YTJH\\oasis.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\oasisresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.click_02s()
    backtomainui()


def character():
    generalact.logger.info('YTJHfun.character')
    generalact.ImgWhileDelay1Cdelay1('YTJH\\character.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\level.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(276, 366)
    if generalact.ImgFor3Cdelay1('YTJH\\level_break.bmp', 0.8, 0, 0, 1920, 1080):
        generalact.moveclick_3s(1390, 930)
    generalact.moveclick_1s(1673, 736)
    back05()
    generalact.ImgWhileDelay1Cdelay1('YTJH\\level.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainui()


def factory():
    generalact.logger.info('YTJHfun.factory')
    generalact.moveclick_2s(1846, 928)
    generalact.ImgFor3Cdelay1('YTJH\\factoryreceive.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainui()
    generalact.moveclick_1s(1246, 606)  # 扩展栏开
    generalact.ImgWhileDelay1Cdelay1('YTJH\\drawcard.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(8, 1112, 1006)
    for i in range(6):
        generalact.moveclick_1s(1694, 996)
        if generalact.ImgReturn1For3('YTJH\\drawcardconfirm.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.ImgWhileCdelay1('YTJH\\drawcardconfirm.bmp', 0.8, 0, 0, 1920, 1080)
            break
        generalact.ImgFor3Cdelay1('YTJH\\drawcardskip.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick01(4, 1112, 1006)
    backtomainui()
    generalact.moveclick_1s(735, 606)  # 扩展栏关
    generalact.moveclick_2s(1846, 928)
    generalact.ImgFor3Cdelay1('YTJH\\factoryproduce.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainui()


def shop(shopcoinflag):
    generalact.logger.info('YTJHfun.shop')
    generalact.moveclick_1s(1564, 811)
    generalact.ImgWhile('YTJH\\lizituijian.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(167, 528)
    generalact.moveclick_1s(506, 512)
    generalact.moveclick_1s(1400, 1020)
    generalact.rangeclick01(3, 960, 50)
    if generalact.firstDayOfWeek():
        generalact.moveclick_1s(167, 528)
        generalact.moveclick_1s(506, 512)
        generalact.moveclick_1s(1400, 1020)
        generalact.rangeclick01(3, 960, 50)
    generalact.moveclick_1s(167, 528)
    if shopcoinflag:
        shopcoin(1)
    shopWeek()
    backtomainui()


def shopcoin(shopWeekflag):
    generalact.logger.info('YTJHfun.shopcoin')
    generalact.ImgWhile('YTJH\\lizituijian.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(167, 1064)
    for i in range(8):
        generalact.moveclick_1s(512, 574)
        if generalact.ImgReturn1For3('YTJH\\coin.bmp', 0.8, 1200, 600, 1920, 1080):
            generalact.moveclick_1s(1497, 970)
            generalact.rangeclick01(4, 960, 50)
        else:
            break


def shopcoin_night(shopWeekflag):
    generalact.logger.info('YTJHfun.shopcoin_night')
    generalact.ImgWhile('YTJH\\lizituijian.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(167, 1064)
    for i in range(8):
        generalact.moveclick_1s(512, 574)
        if generalact.ImgReturn1For3('YTJH\\coin.bmp', 0.8, 1200, 600, 1920, 1080):
            generalact.moveclick_1s(1497, 970)
            generalact.rangeclick01(4, 960, 50)
        else:
            break
    backtomainui()


def shopWeek():
    if generalact.firstDayOfWeek() or generalact.firstDayOfWeek5():
        generalact.rangeclick01(4, 157, 1045)
        for i in range(2):
            generalact.dragmouse(150, 990, 200, 400)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\shop_zhuzhan.bmp', 0.8, 0, 0, 1920, 1080)
        for i in range(2):
            generalact.moveclick_1s(445, 551)
            generalact.rangeclick01(5, 1700, 830)
            generalact.moveclick_1s(1600, 970)
        generalact.rangeclick02(5, 1660, 180)


def dormroom():
    generalact.logger.info('YTJHfun.dormroom')
    generalact.moveclick_1s(1580, 930)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\dormroom.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainui()


def guzhangxieyi():
    if generalact.firstDayOfWeek() or generalact.firstDayOfWeek3() or generalact.firstDayOfWeek5():
        generalact.logger.info('YTJHfun.explore')
        generalact.moveclick_1s(1400, 400)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\guzhang.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\guzhang_tansuoxieyi.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_3s(1570, 965)
        generalact.moveclick_3s(1615, 990)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\jihuamoshi.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_3s(600, 850)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\quanchangzuijia.bmp', 0.8, 0, 0, 1920, 1080)
        time.sleep(3)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\quanchangzuijia.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_3s(1530, 960)
        generalact.moveclick_3s(250, 985)
        generalact.rangeclick02(5, 480, 400)
    if generalact.firstDayOfWeek5():
        for i in range(5):
            generalact.rangeclick02(8, 720 + i*240, 910)


def explore(splinter, resource):
    generalact.logger.info('YTJHfun.explore')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_loudong.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1567, 537)
    generalact.ImgWhileCdelay1('YTJH\\explore_loudong_confirm.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1567, 728)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_loudong_finish.bmp', 0.8, 0, 0, 1920, 1080)
    back05()
    if splinter:
        generalact.logger.info('YTJHfun.explore.splinter')
        generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_splinter.bmp', 0.8, 0, 0, 1920, 1080)
        exploreautobatF()
        generalact.moveclick_1s(200, 500)
        exploreautobat2()
        back05()
    if resource:
        generalact.logger.info('YTJHfun.explore.resource')
        for i in range(2):
            generalact.dragmouse(1700, 500, 300, 500)
        time.sleep(1)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_resourcegather.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_resourcegather_double.bmp', 0.8, 0, 0, 1920, 1080)
        exploreautobat2()
        back02()
    back02()
    backtomainui()


def YGXZ():  # 衍构心智
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_05s(729, 1042)
    generalact.dragmouse(1675, 780, 345, 780)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\YGXZ.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 571, 1015)
    backtomainui()


def huodong(huodongflag, mission):
    if huodongflag:
        if mission:
            for i in range(4):
                generalact.moveclick_05s(492, 729)
                generalact.rangeclick02(6, 951, 991)
            backtomainui()
        huodong_PYGZD(mission)
    else:
        if mission:
            for i in range(4):
                generalact.moveclick_05s(492, 729)
                generalact.rangeclick02(6, 951, 991)
            backtomainui()
        generalact.moveclick_1s(1400, 400)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
        for i in range(2):
            generalact.dragmouse(1700, 500, 300, 500)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_algorithm.bmp', 0.8, 0, 0, 1920, 1080)
        if generalact.firstDayOfWeek2() or generalact.firstDayOfWeek6() or generalact.firstDayOfWeek7():
            generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_algorithm_2.bmp', 0.9, 0, 0, 1920, 1080)
            exploreautobatquick()
            pass
        else:
            if generalact.ImgFor3Cdelay1('YTJH\\explore_algorithm_3_3.bmp', 0.9, 0, 0, 1920, 1080):
                exploreautobatquick()
            else:
                generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_algorithm_3.bmp', 0.9, 0, 0, 1920, 1080)
                generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_algorithm_3_3.bmp', 0.9, 0, 0, 1920, 1080)
                exploreautobatquick()
    backtomainui()


def exploreautobatF():
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_autobat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_05s(1400, 600)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_prebat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\explore_autobat2.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_autobat2.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(12)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_loudong_confirm.bmp', 0.8, 0, 0, 1920, 1080)


def exploreautobat2():
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_autobat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_05s(1400, 600)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_prebat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\explore_autobat2.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_autobat2.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(12)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_loudong_confirm.bmp', 0.8, 0, 0, 1920, 1080)


def exploreautobatquick():
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_autobat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1400, 700)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_startbat.bmp', 0.8, 0, 0, 1920, 1080)
    if generalact.ImgFor3Cdelay1('YTJH\\explore_algorithm_max.bmp', 0.8, 0, 0, 1920, 1080):
        generalact.rangeclick02(4, 1533, 224)
    else:
        if generalact.ImgFor3Cdelay1('YTJH\\explore_batdouble.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.ImgFor3Cdelay1('YTJH\\explore_startbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_quickcon.bmp', 0.8, 0, 0, 1920, 1080)
    blockclick()


def backtomainui1():
    while 1:
        if generalact.ImgReturn1For5('YTJH\\UID.bmp', 0.8, 350, 200, 1920, 1080):
            back05()
            break
        else:
            generalact.moveclick_1s(1759, 255)
            back05()
            back05()
            back05()


def backtomainui():
    while 1:
        if generalact.ImgReturn1For5('YTJH\\UID.bmp', 0.8, 350, 200, 1920, 1080):
            back05()
            break
        else:
            back05()


def blockclick():
    generalact.rangeclick01(4, 952, 1071)


def back02():
    generalact.moveclick_02s(100, 90)


def back05():
    generalact.moveclick_05s(100, 90)


def back1():
    generalact.moveclick_1s(100, 90)


def back2():
    generalact.moveclick_2s(100, 90)


def back3():
    generalact.moveclick_3s(100, 90)


def autobatH():
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\autobatH.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\get.bmp', 0.8, 0, 0, 1920, 1080)
    if generalact.ImgReturn1For3('YTJH\\huodong\\XGSB\\getTX.bmp', 0.8, 0, 0, 1920, 1080):
        # generalact.rangeclick02(4, 1037, 951)
        # generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\get.bmp', 0.8, 0, 0, 1920, 1080)
        # blockclick()
        generalact.rangeclick02(4, 435, 951)
        generalact.rangeclick02(4, 1306, 787)
    blockclick()


def huodong_WLBF(mission):  # 无律背反
    generalact.logger.info('YTJHfun.huodong_XGSB')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(4, 807, 1036)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\WLBF\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\huodong\\WLBF\\ZFHW.bmp', 0.8, 0, 0, 1920, 1080, 220, 0)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\WLBF\\BXEN.bmp', 0.9, 0, 0, 1920, 1080)
    autobatH()
    if mission:
        generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\WLBF\\BXEN.bmp', 0.9, 0, 0, 1920, 1080)
        autobatH()


def huodong_PYGZD(mission):  # 普影归终
    generalact.logger.info('YTJHfun.huodong_PYGZD')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(4, 807, 1036)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\fs.bmp', 0.8, 0, 0, 1920, 1080, 220, 0)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\18.bmp', 0.8, 0, 0, 1920, 1080)
    autobatH()
    if mission:
        generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\18.bmp', 0.8, 0, 0, 1920, 1080)
        autobatH()


def huodong_PYGZ(mission):  # 普影归终
    generalact.logger.info('YTJHfun.huodong_PYGZ')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(4, 807, 1036)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\fs.bmp', 0.8, 0, 0, 1920, 1080, 220, 0)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\18.bmp', 0.8, 0, 0, 1920, 1080)
    autobatH()
    if mission:
        generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\PYGZ\\18.bmp', 0.8, 0, 0, 1920, 1080)
        autobatH()


def huodong_ZGT(mission):  # 致光态
    generalact.logger.info('YTJHfun.huodong_ZGT')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(4, 807, 1036)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\ZGT\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\huodong\\ZGT\\ZYCS.bmp', 0.8, 0, 0, 1920, 1080, 220, 0)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\ZGT\\16.bmp', 0.8, 0, 0, 1920, 1080)
    autobatH()
    if mission:
        generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\ZGT\\16.bmp', 0.8, 0, 0, 1920, 1080)
        autobatH()


def huodong_ZMJD(mission):  # 致密静点
    generalact.logger.info('YTJHfun.huodong_ZMJD')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(4, 807, 1036)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\ZMJD\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\huodong\\ZMJD\\XYCT.bmp', 0.8, 0, 0, 1920, 1080, 220, 0)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\ZMJD\\HBXW.bmp', 0.8, 0, 0, 1920, 1080)
    autobatH()
    if mission:
        generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\ZMJD\\HBXW.bmp', 0.8, 0, 0, 1920, 1080)
        autobatH()


def huodong_XGSB(mission):  # 悬光升变
    generalact.logger.info('YTJHfun.huodong_XGSB')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(4, 807, 1036)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhile('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\quick.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgShiftWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\ZYFP.bmp', 0.8, 0, 0, 1920, 1080, 220, 0)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\BXZH.bmp', 0.8, 0, 0, 1920, 1080)
    autobatH()
    if mission:
        generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\XGSB\\BXZH.bmp', 0.8, 0, 0, 1920, 1080)
        autobatH()


def STMliandong():
    generalact.logger.info('YTJHfun.STMliandong')
    generalact.moveclick_1s(1400, 400)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\exploreresource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(4, 807, 1036)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\STMliandong\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(10)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\STMliandong\\iphone.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('YTJH\\huodong\\STMliandong\\coffee.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay2('YTJH\\huodong\\STMliandong\\coffee_5.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1245, 957)
    generalact.moveclick_1s(1254, 612)
    generalact.moveclick_1s(1350, 626)
    generalact.moveclick_1s(598, 789)  # 快速作战
    # time.sleep(3)
    if generalact.ImgFor3Cdelay1('YTJH\\explore_startbat.bmp', 0.8, 0, 0, 1920, 1080):
        pass
        # generalact.ImgWhile('YTJH\\explore_loudong_confirm.bmp', 0.8, 0, 0, 1920, 1080)
        # generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_autobat2.bmp', 0.8, 0, 0, 1920, 1080)
        # generalact.ImgWhileDelay1Cdelay1('YTJH\\explore_loudong_confirm.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainui()


