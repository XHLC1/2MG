import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


# imgcoordinate = CSauto.locateCenterOnScreen('vectory.bmp', confidence=0.9, region=(1145, 130, 1610, 300))
# generalact.logger.info(imgcoordinate)
# generalact.imgcorrdinatefun('vectory.bmp', 0.9, 1145, 130, 1610, 300)


def dailytaskst(AFTD, huodongflag, jinjie, battleflag):
    enterCWCXfun()
    exerciesfun(AFTD)
    commandroom(AFTD)
    if AFTD:
        friend()
        supply()
    if (generalact.firstDayOfWeek() or generalact.firstDayOfWeek2()) and AFTD:
        battle_jinjie(jinjie)
    if huodongflag:
        # SYJKDDF(AFTD)
        YQWDXYS(AFTD)
    else:
        battle(AFTD, battleflag)
    if AFTD:
        pass
    else:
        mission()
        passport()
        mall()
        mall_month()
    generalact.MUMUclose1()
    generalact.MUMUdrag2()


def enterCWCXfun():
    generalact.logger.info('CWCXFun.enterCWCXfun')
    generalact.imgcorrdinatefunenter('CWCX\\picture\\CWCX.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    time.sleep(10)
    generalact.imgcorrdinatefunclickcount3('CWCX\\picture\\enter_download.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\picture\\enter_download.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainui()


def exerciesfun(AFTD):
    generalact.logger.info('CWCXFun.exerciesfun')
    if generalact.firstDayOfWeek() and AFTD:
        pass
    else:
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Exercise.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Exercise_Complete.bmp', 0.8, 0, 0, 1920, 1080)
        surefun()
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Exercise_pre.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 936, 837)
        clickblock()
        backtomainui()


def surefun():
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Sure.bmp', 0.8, 0, 0, 1920, 1080)
    clickblock()


def commandroom(AFTD):
    generalact.logger.info('CWCXFun.commandroom')
    generalact.imgcorrdinatefunde1('CWCX\\picture\\CommandRoom.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\picture\\CommandRoom_get.bmp', 0.8, 0, 0, 1920, 1080)
    clickblock()
    generalact.rangeclick02(3, 1045, 340)
    generalact.rangeclick02(3, 1485, 911)
    generalact.rangeclick02(3, 1250, 900)
    clickblock()
    if AFTD:
        generalact.moveclick_3s(1600, 745)
        # generalact.imgcorrdinatefunwhile('CWCX\\picture\\CommandRoom_maintenance.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(415, 560)
        time.sleep(50)
        clickblock()
        generalact.moveclick_1s(415, 560)
        generalact.rangeclick02(50, 1475, 785)
        generalact.moveclick_1s(415, 560)
        generalact.rangeclick02(50, 435, 540)
    backtomainui()


def friend():
    generalact.logger.info('CWCXFun.friend')
    generalact.imgcorrdinatefunde1('CWCX\\picture\\friend.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunwhile('CWCX\\picture\\friend_good.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 280, 980)
    backtomainui()


def supply():
    generalact.logger.info('CWCXFun.supply')
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Supply.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunwhile('CWCX\\picture\\Supply_equip.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Supply_equip.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Supply_equip_get.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(3)
    clickblock()
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Supply_equip_sure.bmp', 0.8, 0, 0, 1920, 1080)
    backtomainui()


def mission():
    generalact.logger.info('CWCXFun.mission')
    generalact.imgcorrdinatefunde2('CWCX\\picture\\Mission.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 1645, 1000)
    clickblock()
    generalact.rangeclick02(5, 1337, 958)
    clickblock()
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Mission_week.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 1645, 1000)
    clickblock()
    generalact.rangeclick02(5, 987, 956)
    clickblock()
    generalact.rangeclick02(5, 1337, 958)
    clickblock()
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Mission_month.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 1645, 1000)
    clickblock()
    generalact.rangeclick02(5, 890, 955)
    clickblock()
    generalact.rangeclick02(5, 1105, 950)
    clickblock()
    generalact.rangeclick02(5, 1337, 958)
    clickblock()
    backtomainui()


def passport():
    generalact.logger.info('CWCXFun.passport')
    generalact.imgcorrdinatefunde2('CWCX\\picture\\Passport.bmp', 0.8, 0, 0, 1920, 1080)
    while 1:
        if generalact.imgcorrdinatefuncount3('CWCX\\picture\\Passport_reward.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            generalact.moveclick_1s(1340, 1000)
    generalact.rangeclick02(5, 1615, 1000)
    clickblock()
    generalact.moveclick_1s(285, 468)
    generalact.rangeclick02(5, 1615, 1000)
    clickblock()
    generalact.moveclick_1s(265, 600)
    generalact.rangeclick02(5, 1615, 1000)
    clickblock()
    backtomainui()


def mall():
    if generalact.firstDayOfWeek():
        generalact.logger.info('CWCXFun.mall')
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Mall.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Mall_change.bmp', 0.8, 0, 0, 1920, 1080)
        mall_buy_drug(510, 476)
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Mall_change_logistics.bmp', 0.8, 0, 0, 1920, 1080)
        x = 0
        for i in range(3):
            generalact.rangeclick05(2, 700 + x, 465)
            mall_buy()
            x += 400
        x -= 100
        generalact.rangeclick05(2, 700 + x, 465)
        mall_buy()
        x = 0
        for i in range(3):
            generalact.rangeclick05(2, 700 + x, 865)
            mall_buy()
            x += 400
        x -= 100
        generalact.rangeclick05(2, 700 + x, 865)
        mall_buy()
        mall_buy_drug(1240, 500)  # 1 3
        mall_buy_drug(1240, 840)  # 2 3
        mall_buy_drug(1670, 500)  # 1 4
        backtomainui()


def mall_month():
    if generalact.firstDayOfMonth():
        generalact.logger.info('CWCXFun.mall_month')
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Mall.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Mall_change.bmp', 0.8, 0, 0, 1920, 1080)
        x = 0
        for i in range(3):
            generalact.rangeclick05(2, 700 + x, 465)
            mall_buy()
            x += 400
        x -= 100
        generalact.rangeclick05(2, 700 + x, 465)
        mall_buy()
        x = 0
        for i in range(3):
            generalact.rangeclick05(2, 700 + x, 865)
            mall_buy()
            x += 400
        x -= 100
        generalact.rangeclick05(2, 700 + x, 865)
        mall_buy()
        mall_buy_drug(875, 500)  # 1 2
        mall_buy_drug(1240, 500)  # 1 3
        mall_buy_drug(520, 840)  # 2 1
        mall_buy_drug(875, 840)  # 2 1
        while 1:
            if generalact.imgcorrdinatefuncount3('CWCX\\picture\\Mall_elite_hexinblue.bmp', 0.8, 0, 0, 1920, 660):
                generalact.imgcorrdinatefunde1('CWCX\\picture\\Mall_elite_hexinblue.bmp', 0.8, 0, 0, 1920, 660)
                mall_buy()
                break
            else:
                generalact.dragmouse_count(1050, 660, 510, 660, 1)
            time.sleep(1)
        while 1:
            if generalact.imgcorrdinatefuncount3('CWCX\\picture\\Mall_elite_hexinblue.bmp', 0.8, 0, 660, 1920, 1080):
                generalact.imgcorrdinatefunde1('CWCX\\picture\\Mall_elite_hexinblue.bmp', 0.8, 0, 660, 1920, 1080)
                mall_buy()
                break
            else:
                generalact.dragmouse_count(1050, 660, 510, 660, 1)
            time.sleep(1)
        backtomainui()


def mall_buy():
    generalact.rangeclick05(2, 1215, 604)
    generalact.rangeclick05(2, 1183, 777)
    clickblock()


def mall_buy_drug(x, y):
    generalact.dragmouse_count(1750, 660, 510, 660, 3)
    generalact.rangeclick05(2, x, y)
    mall_buy()


def battle(AFTD, battleflag):
    generalact.logger.info('CWCXFun.battle')
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 435, 250)
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle_resource.bmp', 0.8, 0, 0, 1920, 1080)
    if (not generalact.firstDayOfWeek() and not generalact.firstDayOfWeek2() and not generalact.firstDayOfWeek6() and not generalact.firstDayOfWeek7()) and AFTD:
        generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle_resource_mingyunshilian.bmp', 0.8, 0, 0, 1920, 1080)
        quickbat()
    else:
        if battleflag == 2:  # 核心制作
            generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle_resource_hexinzhizhao.bmp', 0.8, 0, 0, 1920, 1080)
            quickbat()
        if battleflag == 3:  # 队员特训
            generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle_resource_duiyuantexun.bmp', 0.8, 0, 0, 1920, 1080)
            quickbat()


def battle_jinjie(jinjie):
    generalact.logger.info('CWCXFun.battle')
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 435, 250)
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle_resource.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\picture\\Battle_resource_zhuangjiajinjie.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_3s(1500, 685)
    if jinjie == 2:
        generalact.moveclick_1s(108, 432)
    if jinjie == 3:
        generalact.moveclick_1s(125, 583)
    quickbat()


def LHTFcancel():
    generalact.rangeclick02(4, 770, 845)


def SYJKDDF(AFTD):  # 山樱将开的地方
    generalact.logger.info('CWCXFun.SYJKDDF')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\SYJKDDF\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\SYJKDDF\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\SYJKDDF\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\SYJKDDF\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    for i in range(2):
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\SYJKDDF\\a.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\SYJKDDF\\a.bmp', 0.9, 0, 0, 1920, 1080)

        generalact.imgcorrdinatefunde1('CWCX\\huodong\\SYJKDDF\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\SYJKDDF\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 960, 840)
        generalact.rangeclick02(8, 970, 940)
        generalact.rangeclick02(4, 754, 845)
        clickblock()
    back1()
    if AFTD == 0:
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\SYJKDDF\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\SYJKDDF\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 768, 358)
        generalact.rangeclick02(5, 1191, 619)
        generalact.rangeclick02(10, 1275, 775)
        back1()
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\SYJKDDF\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\SYJKDDF\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.rangeclick02(5, 1700, 1000)
        back1()
    backtomainui()


def KYESNDYD(AFTD):  # 跨越二十年的约定
    generalact.logger.info('CWCXFun.QSDHZ')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\KYESNDYD\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\KYESNDYD\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\KYESNDYD\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\KYESNDYD\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    for i in range(2):
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\KYESNDYD\\b.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\KYESNDYD\\b.bmp', 0.9, 0, 0, 1920, 1080)

        generalact.imgcorrdinatefunde1('CWCX\\huodong\\KYESNDYD\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\KYESNDYD\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 960, 840)
        generalact.rangeclick02(8, 970, 940)
        generalact.rangeclick02(4, 754, 845)
        clickblock()
    back1()
    if AFTD == 0:
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\KYESNDYD\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\KYESNDYD\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 768, 358)
        generalact.rangeclick02(5, 1191, 619)
        generalact.rangeclick02(5, 1158, 772)
        clickblock()
        back1()
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\KYESNDYD\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\KYESNDYD\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.rangeclick02(5, 1700, 1000)
        back1()
    backtomainui()


def QSDHZ(AFTD):  # 情书夺还战
    generalact.logger.info('CWCXFun.QSDHZ')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\QSDHZ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\QSDHZ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\QSDHZ\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\QSDHZ\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    for i in range(2):
        # generalact.imgcorrdinatefunde1('CWCX\\huodong\\QSDHZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\QSDHZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\QSDHZ\\b.bmp', 0.9, 0, 700, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\QSDHZ\\b.bmp', 0.9, 700, 0, 1920, 1080)

        generalact.imgcorrdinatefunde1('CWCX\\huodong\\QSDHZ\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\QSDHZ\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 960, 840)
        generalact.rangeclick02(8, 970, 940)
        generalact.rangeclick02(4, 754, 845)
        clickblock()
    back1()
    if AFTD == 0:
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\QSDHZ\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\QSDHZ\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 768, 358)
        generalact.rangeclick02(5, 1191, 619)
        generalact.rangeclick02(5, 1158, 772)
        clickblock()
        back1()
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\QSDHZ\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\QSDHZ\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.rangeclick02(5, 1700, 1000)
        back1()
    backtomainui()


def YQWDXYS(AFTD):  # 一千万的幸运石
    generalact.logger.info('CWCXFun.YQWDXYS')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\YQWDXYS\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\YQWDXYS\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    for i in range(1):
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\YQWDXYS\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\b.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\b.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.dragmouse_count(1450, 850, 1450, 250, 3)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\YQWDXYS\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\YQWDXYS\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 960, 840)
        generalact.rangeclick02(8, 970, 940)
        generalact.rangeclick02(4, 754, 845)
        clickblock()
    back1()
    backtomainui()


def PAYJY(AFTD):  # 平安夜记忆
    generalact.logger.info('CWCXFun.PAYJY')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\PAYJY\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\PAYJY\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\PAYJY\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\PAYJY\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    for i in range(1):
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\PAYJY\\b.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\b.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\b.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.dragmouse_count(1450, 850, 1450, 250, 3)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\PAYJY\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\PAYJY\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 960, 840)
        generalact.rangeclick02(8, 970, 940)
        generalact.rangeclick02(4, 754, 845)
        clickblock()
    back1()
    if AFTD == 0:
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\PAYJY\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\PAYJY\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 768, 358)
        generalact.rangeclick02(5, 1191, 619)
        generalact.rangeclick02(5, 1158, 772)
        clickblock()
        back1()
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\PAYJY\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\PAYJY\\mission.bmp', 0.8, 0, 700, 1920, 1080)
        generalact.rangeclick02(5, 1700, 1000)
        back1()
    backtomainui()


def XJYS(AFTD):  # 峡间轶事
    generalact.logger.info('CWCXFun.XJYS')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    for i in range(1):
        generalact.dragmouse_count(1450, 850, 1450, 250, 3)
        # generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\b.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\b.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.dragmouse_count(1450, 850, 1450, 250, 3)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 960, 840)
        generalact.rangeclick02(8, 970, 940)
        generalact.rangeclick02(4, 754, 845)
        clickblock()
    # back1()
    if AFTD == 0:
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 768, 358)
        generalact.rangeclick02(5, 1191, 619)
        generalact.rangeclick02(5, 1158, 772)
        clickblock()
        back1()
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\XJYS\\mission.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\XJYS\\mission.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 1700, 1000)
        back1()
    backtomainui()


def MMBZ(AFTD):  # 美梦不在
    generalact.logger.info('CWCXFun.MMBZ')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\tiaozhan.bmp', 0.8, 0, 0, 1920, 1080)
    for i in range(2):
        # generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        # generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\a.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\b.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\b.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(3, 1190, 378)
        generalact.rangeclick02(3, 960, 840)
        generalact.rangeclick02(8, 970, 940)
        generalact.rangeclick02(4, 754, 845)
        clickblock()
    back1()
    if AFTD == 0:
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 768, 358)
        generalact.rangeclick02(5, 1191, 619)
        generalact.rangeclick02(5, 1158, 772)
        clickblock()
        back1()
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\MMBZ\\mission.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('CWCX\\huodong\\MMBZ\\mission.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 1700, 1000)
        back1()
    backtomainui()


def XXZQ(AFTD):  # 雪消之前
    generalact.logger.info('CWCXFun.XXZQ')
    # generalact.confirm_cilck3('CWCX\\huodong\\XXZQ\\tiaozhan.bmp', 275, 200)
    generalact.confirm_cilck3('CWCX\\huodong\\XXZQ\\tiaozhan.bmp', 275, 300)
    generalact.dragmouse_count(1520, 960, 1485, 245, 3)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\XXZQ\\10.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1520, 960, 1485, 245, 3)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\XXZQ\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 1190, 378)
    generalact.rangeclick02(3, 960, 840)
    generalact.rangeclick02(8, 970, 940)
    generalact.rangeclick02(4, 754, 845)
    clickblock()
    if AFTD == 0:
        generalact.rangeclick02(3, 540, 990)
        generalact.rangeclick02(3, 1710, 975)
        back1()
    backtomainui()


def HSNMSD(AFTD):  # 海少女迷失地
    generalact.logger.info('CWCXFun.HSNMSD')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\HSNMSD\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    # generalact.confirm_cilck3('CWCX\\huodong\\HSNMSD\\tiaozhan.bmp', 275, 200)
    generalact.confirm_cilck3('CWCX\\huodong\\HSNMSD\\tiaozhan.bmp', 275, 300)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\HSNMSD\\90.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 1105, 900)
    # generalact.imgcorrdinatefunde1('CWCX\\huodong\\SHYSZC\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 1190, 378)
    generalact.rangeclick02(3, 960, 840)
    generalact.rangeclick02(8, 970, 940)
    generalact.rangeclick02(4, 754, 845)
    clickblock()
    backtomainui()


def SHYSZC(AFTD):  # 珊瑚叶生之处
    generalact.logger.info('CWCXFun.XSCY')
    generalact.confirm_cilck3('CWCX\\huodong\\SHYSZC\\tiaozhan.bmp', 275, 200)
    generalact.dragmouse_count(1520, 960, 1485, 245, 3)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\SHYSZC\\10.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1520, 960, 1485, 245, 3)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\SHYSZC\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 1190, 378)
    generalact.rangeclick02(3, 960, 840)
    generalact.rangeclick02(8, 970, 940)
    generalact.rangeclick02(4, 754, 845)
    clickblock()
    if AFTD == 0:
        generalact.rangeclick02(3, 540, 990)
        generalact.rangeclick02(3, 1710, 975)
        back1()
    backtomainui()


def XSCY(AFTD):  # 心神倘佯
    generalact.logger.info('CWCXFun.XSCY')
    generalact.confirm_cilck3('CWCX\\huodong\\XSCY\\tiaozhan.bmp', 275, 200)
    generalact.dragmouse_count(1520, 960, 1485, 245, 3)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\XSCY\\15.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1520, 960, 1485, 245, 3)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\XSCY\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 1190, 378)
    generalact.rangeclick02(3, 960, 840)
    generalact.rangeclick02(8, 960, 940)
    generalact.rangeclick02(4, 744, 845)
    clickblock()
    if AFTD == 0:
        generalact.rangeclick02(3, 530, 970)
        generalact.rangeclick02(3, 1710, 975)
        back1()
    backtomainui()


def LZL(AFTD):  # 林中落
    generalact.logger.info('CWCXFun.LZL')
    generalact.confirm_cilck3('CWCX\\huodong\\LZL\\tiaozhan.bmp', 290, 325)
    generalact.rangeclick02(3, 1490, 175)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\LZL\\1_9.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\LZL\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 1190, 378)
    generalact.rangeclick02(3, 960, 840)
    generalact.rangeclick02(8, 960, 940)
    generalact.rangeclick02(4, 744, 845)
    clickblock()
    if AFTD == 0:
        generalact.rangeclick02(3, 570, 975)
        generalact.rangeclick02(3, 1710, 975)
        back1()
    backtomainui()


def BYLDZQ(AFTD, LHTF):  # 珀因雷德之桥
    generalact.logger.info('CWCXFun.BYLDZQ')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\BYLDZQ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\BYLDZQ\\YXZZ.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\BYLDZQ\\LV90.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1070, 880)
    generalact.rangeclick02(3, 1190, 378)
    generalact.rangeclick02(3, 960, 840)
    generalact.rangeclick02(8, 960, 940)
    clickblock()
    if LHTF:
        LHTFcancel()
    backtomainui()
    if AFTD == 0:
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\BYLDZQ\\enter.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CWCX\\huodong\\BYLDZQ\\mission.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 1430, 1000)
        backtomainui()


def YZGBNS():  # 影之国编年史
    generalact.logger.info('CWCXFun.YZGBNS')
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\YZGBNS\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\YZGBNS\\dreamworld.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\YZGBNS\\6.bmp', 0.8, 0, 0, 1920, 1080)
    quickbat()
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\YZGBNS\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('CWCX\\huodong\\YZGBNS\\boss.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1457, 738)
    generalact.moveclick_1s(1525, 230)
    for i in range(8):
        generalact.rangeclick02(3, 1183, 885)
        generalact.rangeclick02(3, 1177, 380)
        generalact.rangeclick02(3, 987, 833)
        generalact.rangeclick02(8, 960, 940)
    backtomainui()


def quickbat():
    generalact.imgcorrdinatefunde1('CWCX\\picture\\quickbat.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(3, 1190, 378)
    generalact.rangeclick02(3, 960, 840)
    generalact.rangeclick02(8, 960, 940)
    generalact.rangeclick02(8, 720, 830)
    clickblock()
    generalact.rangeclick02(3, 444, 240)
    backtomainui()


def backtomainui():
    generalact.logger.info('CWCXFun.backtomainui')
    n = 0
    while 1:
        if generalact.imgcorrdinatefuncount('CWCX\\picture\\XHL.bmp', 0.8, 50, 600, 1371, 868) == 1:
            back3()
            break
        else:
            n += 1
            if n > 100:
                CSauto.hotkey('alt', 'f4')
                time.sleep(1)
                generalact.startupMUMU(60)
                generalact.imgcorrdinatefunenter('CWCX\\picture\\CWCX.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
                time.sleep(10)
                generalact.imgcorrdinatefunclickcount3('CWCX\\picture\\enter_download.bmp', 0.8, 0, 0, 1920, 1080)
                generalact.imgcorrdinatefunclickcount3('CWCX\\picture\\enter_download.bmp', 0.8, 0, 0, 1920, 1080)
                n = 0
            # break
            back1()


def back1():  # 返回
    generalact.moveclick_1s(46, 86)


def back2():  # 返回
    generalact.moveclick_2s(46, 86)


def back3():  # 返回
    generalact.moveclick_3s(46, 86)


def clickblock():
    generalact.rangeclick01(6, 941, 1064)


def test():
    generalact.imgcorrdinatefunde1('CWCX\\picture\\CommandRoom_maintenance.bmp', 0.8, 0, 0, 1920, 1080)


