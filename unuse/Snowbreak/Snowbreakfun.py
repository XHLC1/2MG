import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


# imgcoordinate = CSauto.locateCenterOnScreen('vectory.bmp', confidence=0.9, region=(1145, 130, 1610, 300))
# generalact.logger.info(imgcoordinate)
# generalact.imgcorrdinatefun('vectory.bmp', 0.9, 1145, 130, 1610, 300)


def dailytaskst(AFTD, huodongflag, resourceflag):
    startwholegame()
    if huodongflag:
        huodong2_2()
    if AFTD:
        levelup()
        weaponlevel()
        payshop()
        battle()
        battle_JSNJ()
    else:
        friends()
        shop()
        mission()
        gamepass()
    closegame()


def startwholegame():
    CSauto.hotkey('winleft', 'd')
    generalact.startup_time('C:\\Software\\op\\opstart.exe', 10)
    time.sleep(5)
    while 1:
        if generalact.imgcorrdinatefunclickcount3('Snowbreak\\picture\\CBJQOP_L.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            generalact.moveclick_1s(961, 731)
    # generalact.imgcorrdinatefunde1('Snowbreak\\picture\\op_jiasu.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(5)
    generalact.imgcorrdinatefunde1('Snowbreak\\picture\\op_start.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(20)
    for i in range(3):
        if generalact.imgcorrdinatefunclickcount3('Snowbreak\\picture\\CBJQ_update.bmp', 0.8, 0, 0, 1980, 1080) == 1:
            generalact.moveclick_1s(1100, 670)
    generalact.imgcorrdinatefunde1('Snowbreak\\picture\\CBJQ_start.bmp', 0.9, 0, 0, 1920, 1080)
    enter()


def closegame():
    CSauto.hotkey('alt', 'f4')
    generalact.killprocess("snow_launcher.exe")
    CSauto.hotkey('winleft', 'd')
    generalact.startup_time('C:\\Software\\op\\opstart.exe', 10)
    time.sleep(5)
    generalact.imgcorrdinatefunshiftde1('Snowbreak\\picture\\op_start.bmp', 0.9, 0, 0, 1920, 1080, 0, 66)


def enter():
    generalact.logger.info('Snowbreak.enter')
    while 1:
        if generalact.imgcorrdinatefuncount('Snowbreak\\picture\\pick.bmp', 0.8, 0, 0, 1980, 1080) == 1:
            clickblock()
            backtomainui()
            break
        else:
            generalact.moveclick_1s(966, 944)
            time.sleep(1)


def levelup():
    generalact.logger.info('Snowbreak.levelup')
    confirmcilck('Snowbreak\\picture\\character.bmp', 1764, 712)
    generalact.dragmouse_count(120, 738, 77, 250, 1)
    for i in range(50):
        CSauto.scroll(-100)
        time.sleep(0.2)
    generalact.moveclick_1s(104, 844)
    generalact.imgcorrdinatefunde1('Snowbreak\\picture\\character_levelup.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun3('Snowbreak\\picture\\character_levelup.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1391, 702)
    generalact.moveclick_1s(1672, 1000)
    backtohome()
    backtomainui()


def weaponlevel():
    generalact.logger.info('Snowbreak.weaponlevel')
    confirmcilck('Snowbreak\\picture\\bag.bmp', 1634, 1034)
    # confirmcilck('Snowbreak\\picture\\bag_weapon_level.bmp', 1385, 350)
    confirmcilck('Snowbreak\\picture\\bag_weapon_level.bmp', 1385, 500)  # 3/4
    generalact.imgcorrdinatefun3('Snowbreak\\picture\\bag_weapon_level.bmp', 0.9, 0, 0, 1920, 1080)  # 3/4
    generalact.moveclick_1s(182, 286)
    generalact.moveclick_1s(1394, 704)
    generalact.moveclick_1s(118, 183)
    generalact.moveclick_1s(1677, 993)
    backtohome()
    backtomainui()


def mission():
    generalact.logger.info('Snowbreak.mission')
    confirmcilck('Snowbreak\\picture\\mission_get.bmp', 1500, 350)
    # while 1:
    #     if generalact.imgcorrdinatefunclickcount3('Snowbreak\\picture\\mission_get.bmp', 0.9, 0, 0, 1920, 1080):
    #         break
    #     else:
    #         generalact.moveclick_1s(1582, 390)
    generalact.rangeclick01(5, 126, 993)
    generalact.rangeclick01(5, 100, 264)
    generalact.rangeclick01(5, 126, 993)
    backtohome()
    backtomainui()


def gamepass():
    generalact.logger.info('Snowbreak.gamepass')
    for i in range(3):
        if confirmcilckfun('Snowbreak\\picture\\gamepass_daily.bmp', 315, 575):
            generalact.imgcorrdinatefun3('Snowbreak\\picture\\gamepass_daily.bmp', 0.9, 0, 0, 1920, 1080)
            generalact.rangeclick01(5, 145, 1015)
            if generalact.firstDayOfWeek7():
                generalact.rangeclick01(5, 1528, 1015)
                generalact.rangeclick01(5, 145, 1015)
                generalact.rangeclick01(5, 1786, 1015)
                generalact.rangeclick01(5, 145, 1015)
    backtohome()
    backtomainui()


def friends():
    generalact.logger.info('Snowbreak.friends')
    generalact.moveclick_1s(328, 477)
    generalact.imgcorrdinatefunwhile('Snowbreak\\picture\\friends_get.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(6, 1780, 1025)
    backtohome()
    backtomainui()


def payshop():
    generalact.logger.info('Snowbreak.payshop')
    generalact.moveclick_1s(90, 550)
    generalact.imgcorrdinatefunde1('Snowbreak\\picture\\payshop_supply.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('Snowbreak\\picture\\payshop_supply_daily.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun3('Snowbreak\\picture\\payshop_supply_daily.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('Snowbreak\\picture\\payshop_buy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun3('Snowbreak\\picture\\payshop_buy.bmp', 0.9, 0, 0, 1920, 1080)
    CSauto.press("ESC")
    backtohome()
    backtomainui()


def shop():
    generalact.logger.info('Snowbreak.shop')
    confirmcilck('Snowbreak\\picture\\shop.bmp', 1798, 1018)
    generalact.imgcorrdinatefun3('Snowbreak\\picture\\shop.bmp', 0.9, 0, 0, 1920, 1080)  # 3/4
    generalact.moveclick_1s(788, 938)
    generalact.moveclick_1s(1770, 1015)
    CSauto.press("ESC")
    backtohome()
    backtomainui()


def clickblock():
    generalact.rangeclick01(6, 941, 1064)


def battle():
    generalact.logger.info('Snowbreak.battle')
    generalact.moveclick_1s(1715, 517)
    generalact.imgcorrdinatefunde1('Snowbreak\\picture\\battle_fragment.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun3('Snowbreak\\picture\\battle_fragment.bmp', 0.9, 0, 0, 1920, 1080)
    battle_fragment(231, 903)
    battle_fragment(572, 903)
    backtohome()


def battle_fragment(x, y):
    generalact.moveclick_1s(x, y)
    generalact.moveclick_1s(1277, 711)
    generalact.moveclick_1s(1020, 845)
    CSauto.press("ESC")


def battle_JSNJ():  # 精神拟镜
    if generalact.firstDayOfWeek5():
        generalact.logger.info('Snowbreak.battle_JSNJ')
        generalact.moveclick_1s(1715, 517)
        generalact.imgcorrdinatefunde1('Snowbreak\\picture\\TBPQ.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunshiftde1('Snowbreak\\picture\\TBPQ_JSNJ.bmp', 0.9, 0, 0, 1920, 1080, 0, -200)
        generalact.imgcorrdinatefunshiftclickcount3('Snowbreak\\picture\\TBPQ_JSNJ.bmp', 0.9, 0, 0, 1920, 1080, 0, -200)
        for i in range(4):
            generalact.rangeclick02(4, 1444, 997)
            generalact.rangeclick02(4, 1347, 775)
            CSauto.press("ESC")
        time.sleep(1)
        generalact.rangeclick02(4, 225, 380)
        for i in range(4):
            generalact.rangeclick02(4, 1444, 997)
            generalact.rangeclick02(4, 1347, 775)
            CSauto.press("ESC")
        time.sleep(1)
        generalact.moveclick_05s(137, 906)
        generalact.rangeclick02(4, 1700, 992)
        backtohome()


def backtohome():
    generalact.rangeclick02(4, 1652, 71)


def backtomainui():
    while 1:
        if generalact.imgcorrdinatefuncount('Snowbreak\\picture\\pick.bmp', 0.8, 0, 0, 1980, 1080) == 1:
            break
        else:
            CSauto.press("ESC")
            time.sleep(1)


def back1():  # 返回
    generalact.moveclick_1s(105, 103)


def back2():  # 返回
    generalact.moveclick_2s(105, 103)


def back3():  # 返回
    generalact.moveclick_3s(105, 103)


def confirmcilck(imgstr, x, y):
    while 1:
        if generalact.imgcorrdinatefunclickcount3(imgstr, 0.9, 0, 0, 1920, 1080):
            break
        else:
            generalact.moveclick_1s(x, y)


def confirmcilckfun(imgstr, x, y):
    if generalact.imgcorrdinatefunclickcount3(imgstr, 0.9, 0, 0, 1920, 1080):
        time.sleep(1)
        return 1
    else:
        generalact.moveclick_1s(x, y)


def huodong2_2():  # 碧水假日
    generalact.logger.info('Snowbreak.huodong2_2')
    confirmcilck('Snowbreak\\huodong\\2_2\\enter.bmp', 1390, 474)
    time.sleep(1)
    generalact.imgcorrdinatefunclickcount3('Snowbreak\\huodong\\2_2\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('Snowbreak\\huodong\\2_2\\6.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('Snowbreak\\huodong\\2_2\\6.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1488, 1006)  # 速战
    generalact.moveclick_1s(1288, 717)
    generalact.moveclick_1s(1228, 844)
    CSauto.press("ESC")
    backtohome()
    backtomainui()


def huodong2_1():  # 极夜行动
    generalact.logger.info('Snowbreak.huodong2_1')
    confirmcilck('Snowbreak\\huodong\\2_1\\enter.bmp', 1390, 474)
    time.sleep(1)
    generalact.imgcorrdinatefunclickcount3('Snowbreak\\huodong\\2_1\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('Snowbreak\\huodong\\2_1\\6.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('Snowbreak\\huodong\\2_1\\6.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1488, 1006)  # 速战
    generalact.moveclick_1s(1288, 717)
    generalact.moveclick_1s(1228, 844)
    CSauto.press("ESC")
    backtohome()
    backtomainui()


def huodong2_0():  # 空都演绎
    generalact.logger.info('Snowbreak.huodong2_0')
    confirmcilck('Snowbreak\\huodong\\2_0\\enter.bmp', 1488, 550)
    generalact.imgcorrdinatefunde1('Snowbreak\\huodong\\2_0\\6.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1488, 1006)  # 速战
    generalact.moveclick_1s(1288, 717)
    generalact.moveclick_1s(1228, 844)
    CSauto.press("ESC")
    backtohome()
    backtomainui()


def huodong1_8():  # 素影遗痕
    generalact.logger.info('Snowbreak.huodong1_8')
    confirmcilck('Snowbreak\\huodong\\1_8\\enter.bmp', 1488, 550)
    generalact.imgcorrdinatefunde1('Snowbreak\\huodong\\1_8\\6.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1488, 1006)  # 速战
    generalact.moveclick_1s(1288, 717)
    generalact.moveclick_1s(1228, 844)
    CSauto.press("ESC")
    backtohome()
    backtomainui()


def huodong1_7():  # 素影遗痕
    generalact.logger.info('Snowbreak.huodong1_7')
    confirmcilck('Snowbreak\\huodong\\1_7\\enter.bmp', 1488, 550)
    generalact.imgcorrdinatefunde1('Snowbreak\\huodong\\1_7\\6.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1488, 1006)  # 速战
    generalact.moveclick_1s(1288, 717)
    generalact.moveclick_1s(1228, 844)
    CSauto.press("ESC")
    backtohome()
    backtomainui()