import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag):
    if AFTD:
        enterBlueArchiveFun()
        TeamAndShop()
        coffeeshop()
        businessareaxuanshangtongji()
        businessarearenwu(AFTD, huodongflag, 3, 4, 0, 0, 0)
        # manufacture()
    else:
        enterBlueArchiveFun()
        businessarearenwu(AFTD, huodongflag, 1, 1, 0, 0, 0)
        # manufacture()
    generalact.MUMUmain()
    generalact.MUMUdrag2()


def enterBlueArchiveFun():
    n = 0
    generalact.logger.info('BlueArchiveFun.enterBlueArchiveFun')
    generalact.imgcorrdinatefunenter('BlueArchive\\BlueArchiveIco.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    generalact.imgcorrdinatefunwhile('BlueArchive\\Menu.bmp', 0.9, 0, 0, 1920, 1080)
    while 1:
        if generalact.imgcorrdinatefuncount3P('BlueArchive\\Menu.bmp', 0.9, 0, 0, 1920, 1080) == 1:
            generalact.moveclick_1s(55, 71)
            break
        else:
            time.sleep(1)
            n += 1
            if n % 60 == 0:
                generalact.MUMUclose1()
                generalact.MUMUclose1()
                generalact.imgcorrdinatefunenter('BlueArchive\\BlueArchiveIco.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    while 1:
        if generalact.imgcorrdinatefuncount3('BlueArchive\\xingheluo.bmp', 0.9, 0, 0, 1920, 1080) == 1:
            back3()
            break
        else:
            n += 1
            generalact.imgcorrdinatefun3('BlueArchive\\update.bmp', 0.8, 0, 0, 1920, 1080)
            back2()
            if n % 60 == 0:
                generalact.MUMUclose1()
                generalact.MUMUclose1()
                generalact.imgcorrdinatefunenter('BlueArchive\\BlueArchiveIco.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
                generalact.imgcorrdinatefunwhile('BlueArchive\\Menu.bmp', 0.9, 0, 0, 1920, 1080)
                generalact.moveclick_1s(55, 71)


def TeamAndShop():
    generalact.logger.info('BlueArchiveFun.TeamAndShop')
    generalact.imgcorrdinatefunshiftde1('BlueArchive\\Team.bmp', 0.8, 0, 900, 1920, 1080, 0, -30)
    backtomainui()
    generalact.imgcorrdinatefunshiftde1('BlueArchive\\shop.bmp', 0.8, 0, 900, 1920, 1080, 0, -30)
    x = 0
    time.sleep(1)
    generalact.moveclick_1s(1714, 760)
    generalact.dragmouse(1387, 900, 1387, 220)
    time.sleep(1)
    for i in range(4):
        generalact.moveclick_05s(1057 + x, 450)
        x += 200
    for i in range(3):
        CSauto.scroll(-200)
        time.sleep(0.5)
    x = 0
    time.sleep(1)
    for i in range(4):
        generalact.moveclick_05s(1057 + x, 322)
        x += 200
    x = 0
    for i in range(4):
        generalact.moveclick_05s(1057 + x, 722)
        x += 200
    generalact.moveclick_1s(1692, 989)
    generalact.moveclick_05s(1094, 749)
    generalact.rangeclick02(3, 94, 92)
    backtomainui()


def coffeeshop():
    generalact.logger.info('BlueArchiveFun.coffeeshop')
    generalact.imgcorrdinatefunshiftde1('BlueArchive\\coffee.bmp', 0.8, 0, 900, 1920, 1080, 0, -30)
    backtomainui()
    generalact.imgcorrdinatefunshiftde1('BlueArchive\\coffee.bmp', 0.8, 0, 900, 1920, 1080, 0, -30)
    generalact.imgcorrdinatefun('BlueArchive\\coffeecollect.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(999, 795)
    generalact.rangeclick02(5, 90, 90)
    backtomainui()


def queren():
    while 1:
        if generalact.imgcorrdinatefun3('BlueArchive\\queren.bmp', 0.9, 0, 0, 1920, 1080):
            break
        else:
            generalact.moveclick_1s(1379, 620)  # 开始扫荡


def querensaodang():
    generalact.imgcorrdinatefun3('BlueArchive\\saodangqueren.bmp', 0.9, 0, 0, 1920, 1080)


def saodangqueren():
    for i in range(10):
        generalact.moveclick_01s(940, 771)
    querensaodang()
    generalact.moveclick_02s(965, 993)
    generalact.moveclick_02s(965, 993)
    generalact.moveclick_02s(965, 993)


def businessareaxuanshangtongji():
    generalact.logger.info('BlueArchiveFun.businessareaxuanshangtongji')
    generalact.moveclick_3s(1766, 872)  # 业务区
    xuanshangtongji()
    skywaywhile()
    generalact.moveclick_2s(1380, 429)  # 高架公路
    xuanshangtongjirufchang()
    skywaywhile()
    generalact.moveclick_1s(1400, 631)  # 沙漠铁路
    xuanshangtongjirufchang()
    skywaywhile()
    generalact.moveclick_1s(1517, 860)  # 讲堂
    # generalact.moveclick_1s(1650, 810)
    # kaishishaodang()
    xuanshangtongjirufchang()
    xuanshangtongjiback()


def xuanshangtongji():
    generalact.imgcorrdinatefunde1('BlueArchive\\xuanshangtongji.bmp', 0.9, 980, 600, 1220, 800)


def xuanshangtongjiwhile():
    generalact.imgcorrdinatefunwhile('BlueArchive\\xuanshangtongji.bmp', 0.9, 994, 600, 1220, 800)


def xuanshangtongjiback():
    generalact.imgcorrdinatefunmovenoclick('BlueArchive\\xuanshangtongji.bmp', 0.9, 980, 600, 1220, 800, 94, 92)


def skyway():
    generalact.imgcorrdinatefun('BlueArchive\\skyway.bmp', 0.9, 0, 0, 1920, 1080)


def skywaywhile():
    generalact.imgcorrdinatefunwhile('BlueArchive\\skyway.bmp', 0.9, 0, 0, 1920, 1080)


def xuanshangtongjirufchang():
    generalact.moveclick_1s(1650, 964)
    kaishishaodang()


def kaishishaodang():
    generalact.rangeclick01(8, 1550, 482)
    generalact.moveclick_1s(1379, 620)  # 开始扫荡
    queren()
    saodangqueren()


def kaishishaodang20():
    CSauto.moveTo(1550, 482)
    for i in range(60):
        CSauto.doubleClick()
        time.sleep(0.01)
    # generalact.rangeclick01(20, 1550, 482)
    generalact.moveclick_1s(1379, 620)  # 开始扫荡
    queren()
    saodangqueren()


def kaishishaodang1():
    generalact.moveclick_1s(1379, 620)  # 开始扫荡
    queren()
    saodangqueren()


def businessarearenwu(AFTD, huodongflag, huodongflag_sui3, huodongflag_shop, qingnai, youxiang, baizi):
    generalact.logger.info('BlueArchiveFun.businessarearenwu')
    if AFTD:
        generalact.rangeclick02(10, 1191, 449)  # 任务
        generalact.rangeclick02(5, 1560, 269)
        for i in range(18):
            generalact.moveclick_01s(89, 561)
        for i in range(12):
            generalact.moveclick_01s(1835, 565)
        renwusaodang1()  # 春香
        for i in range(1):
            generalact.moveclick_01s(1835, 565)
        renwusaodang3()  # 伊织
        for i in range(1):
            generalact.moveclick_01s(1835, 565)
        renwusaodang1()  # 春香
        # renwusaodang2()  # 椿
        for i in range(2):
            generalact.moveclick_01s(1835, 565)
        # renwusaodang3()  # 花凛
        pass
    if huodongflag:
        backtomainui()
        huodong(AFTD, huodongflag_sui3, huodongflag_shop)
    elif AFTD:
        generalact.moveclick_2s(1191, 449)  # 任务
        generalact.moveclick_05s(1560, 269)
        #  白子
        if baizi:
            for i in range(18):
                generalact.moveclick_01s(89, 561)
            for i in range(2):
                generalact.moveclick_01s(1835, 565)
            renwusaodang3()
            for i in range(6):
                generalact.moveclick_01s(1835, 565)
            renwusaodang3()
        #  晴奈
        if qingnai:
            for i in range(18):
                generalact.moveclick_01s(89, 561)
            for i in range(7):
                generalact.moveclick_01s(1835, 565)
            renwusaodang3()
            for i in range(4):
                generalact.moveclick_01s(1835, 565)
            renwusaodang3()
        #  邮箱
        if youxiang:
            for i in range(18):
                generalact.moveclick_01s(89, 561)
            # renwusaodang1()
            for i in range(3):
                generalact.moveclick_01s(1835, 565)
            renwusaodang3()
            for i in range(8):
                generalact.moveclick_01s(1835, 565)
            renwusaodang2()
        back2()
    # xuanshangtongjiwhile()
    # generalact.moveclick_1s(1087, 867)
    # generalact.moveclick_1s(1483, 423)
    # generalact.moveclick_1s(1644, 961)
    # kaishishaodang1()
    backtomainui()


def huodong(AFTD, huodongflag_sui3, huodongflag_shop):
    huodongflag_shopcount = 1
    if AFTD:
        if huodongflag_sui3:
            generalact.moveclick_1s(931, 94)
            if huodongflag_sui3 == 3:
                generalact.moveclick_1s(1309, 545)
            generalact.moveclick_1s(1145, 770)
            generalact.moveclick_1s(1145, 770)
            generalact.rangeclick01(10, 1578, 1011)
        if huodongflag_shop:
            generalact.imgcorrdinatefunshiftde1('BlueArchive\\shop.bmp', 0.8, 0, 900, 1920, 1080, 0, -30)
            generalact.imgcorrdinatefunde1('BlueArchive\\shop_zhanshu.bmp', 0.8, 0, 0, 1920, 1080)
            if huodongflag_shop == 4:
                huodongflag_shopcount = 4
            for i in range(huodongflag_shopcount):
                generalact.moveclick_05s(1039, 765)  # 21
                generalact.moveclick_05s(1227, 744)  # 22
                generalact.moveclick_05s(1692, 989)
                generalact.moveclick_05s(1094, 749)
                blockclick()
                if huodongflag_shopcount == 4:
                    generalact.moveclick_05s(1739, 993)  # 刷新
                    generalact.moveclick_05s(1183, 730)
            generalact.rangeclick02(3, 94, 92)
            backtomainui()
    else:
        coffeeshop()
    huodong_TNL()


def huodong_TNL():
    generalact.moveclick_3s(1766, 872)  # 业务区
    xuanshangtongjiwhile()
    generalact.moveclick_2s(162, 275)
    generalact.imgcorrdinatefunwhile('BlueArchive\\huodong\\yongzhuang2\\wanfazhiyin.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1393, 207)
    generalact.movemouse(1400, 520)
    while 1:
        # if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\TNL\\07.bmp',
        #                                                0.9, 850, 100, 1980, 1080, 450, 0):  # 6
        # if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\library\\11.bmp',
        #                                                0.9, 850, 100, 1980, 1080, 450, 0):  # 6
        if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\TNL\\09.bmp',
                                                       0.9, 850, 100, 1980, 1080, 450, 0):  # 6
            break
        CSauto.scroll(-100)
        time.sleep(1)
    kaishishaodang20()


def huodong_library():
    generalact.moveclick_3s(1766, 872)  # 业务区
    xuanshangtongjiwhile()
    generalact.moveclick_2s(162, 275)
    generalact.imgcorrdinatefunwhile('BlueArchive\\huodong\\yongzhuang2\\wanfazhiyin.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1393, 207)
    generalact.movemouse(1400, 520)
    while 1:
        # if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\library\\09.bmp',
        #                                                0.8, 850, 100, 1980, 1080, 450, 0):  # 6
        # if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\library\\10.bmp',
        #                                                0.8, 850, 100, 1980, 1080, 420, 0):  # 8
        # if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\library\\11.bmp',
        #                                                0.9, 850, 100, 1980, 1080, 450, 0):  # 6
        if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\library\\12.bmp',
                                                       0.9, 850, 100, 1980, 1080, 420, 0):  # 8
            break
        CSauto.scroll(-100)
        time.sleep(1)
    kaishishaodang20()


def huodong_214():
    generalact.moveclick_3s(1766, 872)  # 业务区
    xuanshangtongjiwhile()
    generalact.moveclick_2s(162, 275)
    generalact.imgcorrdinatefunwhile('BlueArchive\\huodong\\yongzhuang2\\wanfazhiyin.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1393, 207)
    generalact.movemouse(1400, 520)
    while 1:
        # if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\214\\10.bmp',
        #                                                0.8, 850, 100, 1980, 1080, 420, 0):
        if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\214\\11.bmp',
                                                       0.8, 850, 100, 1980, 1080, 450, 0):
            break
        CSauto.scroll(-100)
        time.sleep(1)
    kaishishaodang20()


def huodong_newyear():
    generalact.moveclick_3s(1766, 872)  # 业务区
    xuanshangtongjiwhile()
    generalact.moveclick_2s(162, 275)
    generalact.imgcorrdinatefunwhile('BlueArchive\\huodong\\yongzhuang2\\wanfazhiyin.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1393, 207)
    generalact.movemouse(1400, 520)
    while 1:
        # if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\newyear\\12.bmp',
        #                                                0.8, 850, 100, 1980, 1080, 450, 0):
        if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\newyear\\12.bmp',
                                                       0.8, 850, 100, 1980, 1080, 450, 0):
            break
        CSauto.scroll(-100)
        time.sleep(1)
    kaishishaodang20()


def huodong_227():
    generalact.moveclick_2s(1775, 350)
    generalact.imgcorrdinatefunwhile('BlueArchive\\huodong\\227\\jiangli.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1400, 205)  # 任务
    generalact.movemouse(1400, 520)
    while 1:
        if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\227\\12.bmp',
                                                       0.8, 850, 100, 1980, 1080, 450, 0):
            break
        CSauto.scroll(-100)
        time.sleep(1)
    kaishishaodang20()


def huodong_yongzhuang2():
    generalact.moveclick_3s(1766, 872)  # 业务区
    xuanshangtongjiwhile()
    generalact.moveclick_2s(162, 275)
    generalact.imgcorrdinatefunwhile('BlueArchive\\huodong\\yongzhuang2\\wanfazhiyin.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1393, 207)
    generalact.movemouse(1400, 520)
    while 1:
        if generalact.imgcorrdinatefunshiftclickcount3('BlueArchive\\huodong\\yongzhuang2\\10.bmp',
                                                       0.8, 850, 100, 1980, 1080, 450, 0):
            break
        CSauto.scroll(-100)
        time.sleep(1)
    kaishishaodang20()


def renwusaodang1():
    generalact.moveclick_1s(1650, 412)
    kaishishaodang()


def renwusaodang2():
    generalact.moveclick_1s(1650, 573)
    kaishishaodang()


def renwusaodang3():
    generalact.moveclick_1s(1650, 729)
    kaishishaodang()


def manufacture():
    generalact.logger.info('BlueArchiveFun.manufacture')
    generalact.imgcorrdinatefunshiftde1('BlueArchive\\manufacture.bmp', 0.8, 0, 900, 1920, 1080, 0, -30)
    for i in range(4):
        generalact.imgcorrdinatefun3('BlueArchive\\manufacture_get.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.rangeclick02(4, 800, 1050)
    generalact.moveclick_3s(1440, 440)
    generalact.moveclick_1s(1350, 350)
    generalact.moveclick_3s(1600, 980)
    manufacture_make()


def manufacture_make():
    man0x, man0y = 1, 1
    man1x, man1y = 860, 440
    man2x, man2y = 760, 600
    man3x, man3y = 635, 720
    man4x, man4y = 466, 808
    man5x, man5y = 275, 845
    manx, many = 1, 1
    Vhighitemx, Vhighitemy = 1, 1
    giftx, gifty = 1, 1
    highitemx, highitemy = 1, 1
    giftflag = 0
    highitemflag = 0
    while 1:
        if generalact.imgcorrdinatefuncount('BlueArchive\\manufacture_see.bmp', 0.9, 0, 0, 1920, 1080) == 1:
            break
        else:
            generalact.moveclick_02s(1240, 440)
    for i in range(5):
        if i == 0:
            man0x, man0y = man1x, man1y
        if i == 1:
            man0x, man0y = man2x, man2y
        if i == 2:
            man0x, man0y = man3x, man3y
        if i == 3:
            man0x, man0y = man4x, man4y
        if i == 4:
            man0x, man0y = man5x, man5y
        generalact.moveclick_05s(man0x, man0y)
        if generalact.imgcorrdinatefuncount('BlueArchive\\manufacture_Vhighitem.bmp', 0.8, 0, 0, 1920, 1080) == 1:
            Vhighitemflag = 1
            Vhighitemx, Vhighitemy = man0x, man0y
        else:
            Vhighitemflag = 0
        if generalact.imgcorrdinatefuncount('BlueArchive\\manufacture_gift.bmp', 0.8, 0, 0, 1920, 1080) == 1:
            giftflag = 1
            giftx, gifty = man0x, man0y
        else:
            # giftflag = 0
            pass
        if generalact.imgcorrdinatefuncount('BlueArchive\\manufacture_highitem.bmp', 0.8, 0, 0, 1920, 1080) == 1:
            highitemflag = 1
            highitemx, highitemy = man0x, man0y
        else:
            # highitemflag = 0
            pass
        if Vhighitemflag == 1:
            manx, many = Vhighitemx, Vhighitemy
            break
        if i == 4:
            if giftflag == 1:
                manx, many = giftx, gifty
                break
        if i == 4:
            if highitemflag == 1:
                manx, many = highitemx, highitemy
                break
        # generalact.logger.info(highitemx, highitemy)
    if manx == 1 and many == 1:
        pass
    else:
        generalact.moveclick_05s(manx, many)
    generalact.moveclick_1s(1630, 990)
    generalact.imgcorrdinatefunde1('BlueArchive\\manufacture_make.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('BlueArchive\\manufacture_man.bmp', 0.9, 0, 0, 1920, 1080)


def backtomainui():
    while 1:
        if generalact.imgcorrdinatefuncount('BlueArchive\\xingheluo.bmp', 0.9, 0, 0, 1920, 1080) == 1:
            back3()
            break
        else:
            back1()


def back1():
    generalact.moveclick_1s(94, 92)


def back2():
    generalact.moveclick_2s(94, 92)


def back3():
    generalact.moveclick_3s(94, 92)


def blockclick():
    generalact.rangeclick01(5, 932, 1065)


def backtomain():
    generalact.moveclick_1s(1821, 74)
