import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag, resourceflag, QXZLflag):
    if AFTD:
        # huodongflag = 0
        enterQNZLfun()
        KLLMX()
        shop()
        division()
        batattack(huodongflag)
        if huodongflag:
            huodong_JDDS(AFTD)
    else:
        enterQNZLfun()
        division()
        startrace()
        mission()
        if QXZLflag:
            QXZL(1)
            if huodongflag:
                huodong_JDDS(AFTD)
            else:
                resource(resourceflag)
                pass
            QXZL(1)
        if huodongflag:
            huodong_JDDS(AFTD)
        else:
            resource(resourceflag)
            pass
        guild()
        if generalact.firstDayOfWeek6():
            HMZJ()
    generalact.MUMUclose1()
    generalact.MUMUdrag2()


def enterQNZLfun():
    generalact.logger.info('QNZLfun.enterQNZLfunF')
    generalact.ImgShiftWhileDelay1Cdelay1('QNZL\\QNZL.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    n = 0
    a = 1
    while a:
        if generalact.ImgFor3Cdelay1('QNZL\\StartQNZL.bmp', 0.8, 0, 0, 1920, 1080):
            time.sleep(20)
            back1()
            if generalact.ImgReturn1For3('QNZL\\eventnotice.bmp', 0.9, 800, 0, 1920, 1080):
                generalact.moveclick_1s(1826, 160)
            time.sleep(5)
            generalact.rangeclick02(5, 1690, 260)
            while 1:
                if generalact.ImgReturn1For5('QNZL\\UID.bmp', 0.9, 0, 0, 1920, 1080):
                    time.sleep(1)
                    a = 0
                    break
                else:
                    back1()
                    if n % 3 == 0:
                        generalact.moveclick_1s(1835, 158)
                    n += 1
                    if n >= 60:
                        generalact.MUMUclose1()
                        generalact.ImgShiftFor3Cdelay1('QNZL\\QNZL.bmp', 0.8, 0, 0, 1920, 1080, 0, -40)
                        n = 0
                        break
        else:
            time.sleep(1)
            n += 1
            if n >= 60:
                generalact.ImgShiftFor3Cdelay1('QNZL\\QNZL.bmp', 0.8, 0, 0, 1920, 1080, 0, -40)
                n = 0
    backtomainui()


def KLLMX():
    generalact.moveclick_1s(102, 427)
    generalact.ImgWhile('QNZL\\KLLMX.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1712, 866)
    generalact.ImgWhile('QNZL\\KLLMX_item.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(950, 900)
    backtomainui()


def shop():
    generalact.logger.info('QNZLfun.shop')
    generalact.moveclick_1s(1428, 960)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\shopgift.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(900, 400)
    generalact.ImgWhileCdelay1('QNZL\\buy.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 980, 150)
    if generalact.firstDayOfWeek():
        generalact.moveclick_1s(900, 400)
        generalact.ImgWhileCdelay1('QNZL\\buy.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.rangeclick02(4, 980, 150)
    if generalact.firstDayOfMonth():
        generalact.moveclick_1s(900, 400)
        generalact.ImgWhileCdelay1('QNZL\\buy.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.rangeclick02(4, 980, 150)
    generalact.moveclick_1s(1473, 1031)  # 兌換商店
    for i in range(8):
        generalact.moveclick_1s(900, 400)
        if generalact.ImgReturn1For3('QNZL\\coin.bmp', 0.9, 800, 200, 1920, 1080):
            generalact.moveclick_1s(1287, 876)
            generalact.rangeclick02(4, 980, 150)
        else:
            generalact.rangeclick02(4, 980, 100)
            break
    generalact.moveclick_1s(600, 750)  # 友情商店
    generalact.moveclick_1s(1750, 165)
    if generalact.firstDayOfMonth():
        generalact.ImgWhileCdelay1('QNZL\\shop_blue.bmp', 0.9, 0, 0, 1920, 1080)
        for i in range(2):
            generalact.moveclick_1s(900, 400)
            generalact.moveclick_1s(1170, 760)  # MAX
            generalact.moveclick_1s(1287, 876)
            generalact.rangeclick02(4, 980, 150)
    if generalact.firstDayOfWeek():
        generalact.moveclick_1s(900, 835)
        generalact.moveclick_1s(1287, 876)
        generalact.rangeclick02(4, 980, 150)
    if generalact.firstDayOfWeek():
        generalact.ImgWhileCdelay1('QNZL\\MYshop.bmp', 0.9, 0, 0, 1920, 1080)
        for i in range(2):
            generalact.moveclick_1s(1150, 425)
            generalact.moveclick_1s(1170, 760)  # MAX
            generalact.moveclick_1s(1287, 876)
            generalact.rangeclick02(4, 980, 150)
    backtomainui()


def shop_t():
    generalact.ImgWhileCdelay1('QNZL\\MYshop.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1150, 425)
    generalact.moveclick_1s(1170, 760)  # MAX
    generalact.moveclick_1s(1287, 876)
    generalact.rangeclick02(4, 980, 150)


def mission():
    generalact.logger.info('QNZLfun.mission')
    generalact.moveclick_1s(115, 242)
    generalact.rangeclick01(15, 1746, 657)
    backtomainui()
    # generalact.moveclick_1s(115, 242)
    # generalact.rangeclick01(5, 1750, 850)
    # backtomainui()
    KLLMX()
    backtomainui()


def batattack(huodongflag):
    generalact.logger.info('QNZLfun.batattack')
    if generalact.firstDayOfWeek7():
        generalact.moveclick_1s(1660, 900)
        generalact.rangeclick02(5, 1100, 1040)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_gate.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_2s(1200, 270)
        generalact.moveclick_1s(1800, 435)
        generalact.ImgWhileCdelay1('QNZL\\attack_quick.bmp', 0.8, 0, 0, 1920, 1080)
        if huodongflag:
            generalact.moveclick_05s(1655, 851)
        else:
            generalact.moveclick_05s(1752, 852)  # max
        generalact.moveclick_05s(1640, 1010)
        if generalact.ImgFor3Cdelay1('QNZL\\attack_confirm.bmp', 0.8, 0, 0, 1920, 1080):
            pass
        else:
            generalact.rangeclick02(2, 1816, 915)
        time.sleep(3)
        if generalact.ImgFor3Cdelay1('QNZL\\attack_confirm.bmp', 0.8, 0, 0, 1920, 1080):
            pass
        else:
            generalact.rangeclick02(2, 1816, 915)
        home()
        backtomainui()
    else:
        generalact.moveclick_1s(1660, 900)
        generalact.rangeclick02(5, 1100, 1040)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_gate.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_double.bmp', 0.9, 0, 0, 1920, 1080)
        time.sleep(1)
        generalact.moveclick_1s(1800, 435)
        generalact.ImgWhileCdelay1('QNZL\\attack_quick.bmp', 0.9, 0, 0, 1920, 1080)
        if huodongflag:
            generalact.moveclick_05s(1655, 851)
        else:
            generalact.moveclick_05s(1752, 852)  # max
        generalact.moveclick_05s(1640, 1010)
        generalact.rangeclick02(10, 1654, 1012)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_confirm.bmp', 0.9, 0, 0, 1920, 1080)
        home()
        backtomainui()
        generalact.moveclick_1s(1660, 900)
        generalact.rangeclick02(5, 1100, 1040)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_gate.bmp', 0.9, 0, 0, 1920, 1080)
        for i in range(2):
            generalact.dragmouse(1325, 950, 1325, 170)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\MEETINGPLACE.bmp', 0.9, 0, 0, 1920, 1080)
        time.sleep(1)
        generalact.moveclick_1s(430, 700)  # 2
        # generalact.moveclick_1s(995, 695)  # 4
        # generalact.moveclick_1s(1540, 700)  # 6
        generalact.ImgWhileCdelay1('QNZL\\attack_quick.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(1752, 852)  # max
        generalact.moveclick_05s(1640, 1010)
        generalact.rangeclick02(10, 1654, 1012)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_confirm.bmp', 0.9, 0, 0, 1920, 1080)
        home()
        backtomainui()


def resource(resourceflag):
    generalact.moveclick_1s(1660, 900)
    generalact.rangeclick02(5, 1100, 1040)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_gate.bmp', 0.9, 0, 0, 1920, 1080)
    if resourceflag == 0:  # 钱
        generalact.moveclick_1s(1090, 290)
    if resourceflag == 1:  # 经验
        generalact.moveclick_1s(1090, 635)
    if resourceflag == 2:  # 技能
        generalact.moveclick_1s(1090, 930)
    if resourceflag == 4:  # 符文
        generalact.dragmouse_count(1275, 910, 1275, 190, 2)
        generalact.moveclick_1s(1340, 250)
        time.sleep(1)
        generalact.moveclick_1s(1580, 710)  # 6
    else:
        generalact.moveclick_1s(1800, 435)  # 7
    generalact.ImgWhileCdelay1('QNZL\\attack_quick.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_05s(1752, 852)  # max
    generalact.moveclick_05s(1640, 1010)
    generalact.rangeclick02(10, 1654, 1012)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_confirm.bmp', 0.9, 0, 0, 1920, 1080)
    home()
    backtomainui()


def division():
    generalact.logger.info('QNZLfun.division')
    generalact.moveclick_05s(1211, 963)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\divsion_affirm.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1550, 300)
    generalact.rangeclick02(4, 980, 100)
    generalact.moveclick_1s(1120, 980)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\divsion_activity.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1800, 245)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\divsion_change.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\divsion_change2.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\divsion_change3.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgFor3Cdelay1('QNZL\\divsion_confirm.bmp', 0.9, 0, 0, 1920, 1080)
    time.sleep(2)
    back1()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\divsion_restroom.bmp', 0.9, 1080, 900, 1920, 1080)
    generalact.ImgWhile('QNZL\\divsion_restroom2.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1650, 1010)
    # generalact.ImgWhileDelay1Cdelay1('QNZL\\divsion_playroom.bmp', 0.9, 0, 0, 1920, 1080)
    # generalact.moveclick_1s(1675, 1000)
    home()
    backtomainui()


def divisionwitch():
    generalact.logger.info('QNZLfun.divisionwitch')
    # generalact.moveclick_05s(1211, 963)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\divsionwitch_KURORO.bmp', 0.9, 150, 886, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\divsion_MN_KLL.bmp', 0.7, 0, 0, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\divsion_MN_interact.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(6, 565, 520)
    generalact.rangeclick01(6, 827, 523)
    generalact.rangeclick01(6, 1075, 552)


def startrace():
    generalact.logger.info('QNZLfun.startrace')
    generalact.moveclick_1s(573, 960)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\startrace.bmp', 0.9, 0, 0, 1920, 1080)
    for i in range(5):
        generalact.dragmouse(1752, 613, 223, 613)
    generalact.moveclick_1s(1573, 256)  # 1
    # generalact.moveclick_1s(1573, 827)  # 3
    generalact.ImgWhile('QNZL\\startrace_break.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_2s(290, 1000)
    generalact.moveclick_05s(1171, 702)
    generalact.moveclick_05s(1544, 973)
    home()
    backtomainui()


def guild():
    generalact.logger.info('QNZLfun.guild')
    generalact.ImgWhileDelay1Cdelay1('QNZL\\guild.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 1000, 600)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\guild_doinet.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(20, 1522, 820)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\guild_member.bmp', 0.9, 0, 0, 1920, 1080)
    for i in range(3):
        generalact.ImgWhileDelay1Cdelay1('QNZL\\guild_good.bmp', 0.9, 0, 0, 1920, 1080)
        clickblock()
        generalact.ImgWhileDelay1Cdelay1('QNZL\\guild_member.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.dragmouse_count(1150, 900, 1150, 180, i)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\guild_quest.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(30, 1640, 400)
    for i in range(6):
        generalact.rangeclick01(6, 900 + 165*i, 850)
    if generalact.firstDayOfWeek7():
        generalact.rangeclick02(4, 1550, 170)
        generalact.rangeclick01(30, 1640, 400)
        for i in range(6):
            generalact.rangeclick01(6, 900 + 165 * i, 850)
    backtomainui()


def home():
    generalact.moveclick_1s(281, 86)


def backtomainui():
    while 1:
        if generalact.ImgReturn1For5('QNZL\\UID.bmp', 0.9, 0, 0, 1920, 1080):
            time.sleep(1)
            break
        else:
            back1()


def back1():
    generalact.moveclick_1s(90, 90)


def back2():
    generalact.moveclick_2s(90, 90)


def back3():
    generalact.moveclick_3s(90, 90)


def clickblock():
    generalact.rangeclick01(4, 1030, 1050)


def HMZJ():
    generalact.logger.info('QNZLfun.HMZJ')
    generalact.moveclick_1s(1660, 900)
    generalact.rangeclick02(5, 815, 1033)
    generalact.ImgReturn1For3_Confirm('QNZL\\HMZJ\\mission.bmp', 815, 1030)
    generalact.ImgFor3Cdelay1_Confirm('QNZL\\HMZJ\\MMMY.bmp', 1090, 225)
    generalact.moveclick_3s(1685, 1000)
    generalact.moveclick_1s(1685, 1000)
    generalact.ImgShiftWhileDelay1Cdelay1('QNZL\\HMZJ\\again.bmp', 0.8, 0, 0, 1920, 1080, 200, 0)
    time.sleep(2)
    generalact.ImgFor3Cdelay1('QNZL\\HMZJ\\confirm.bmp', 0.8, 0, 0, 1920, 1080)
    clickblock()
    back3()

    generalact.dragmouse_count(1150, 900, 1150, 100, 2)
    generalact.ImgFor3Cdelay1_Confirm('QNZL\\HMZJ\\HWMY.bmp', 1315, 845)
    generalact.moveclick_3s(1685, 1000)
    generalact.moveclick_1s(1685, 1000)
    generalact.ImgShiftWhileDelay1Cdelay1('QNZL\\HMZJ\\again.bmp', 0.8, 0, 0, 1920, 1080, 200, 0)
    time.sleep(2)
    generalact.ImgFor3Cdelay1('QNZL\\HMZJ\\confirm.bmp', 0.8, 0, 0, 1920, 1080)
    clickblock()
    back3()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\mission.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(10, 495, 825)


def HMZJ_H(choose):
    generalact.logger.info('QNZLfun.HMZJ')
    generalact.moveclick_1s(1660, 900)
    generalact.rangeclick02(5, 815, 1033)
    generalact.ImgReturn1For3_Confirm('QNZL\\HMZJ\\mission.bmp', 815, 1030)
    generalact.moveclick_3s(130, 870)
    if choose == 1:
        generalact.moveclick_3s(1100, 350)  # 1
    if choose == 2:
        generalact.moveclick_3s(1100, 650)  # 2
    if choose == 3:
        generalact.moveclick_3s(1100, 950)  # 3
    generalact.ImgReturn1For3_Confirm('QNZL\\HMZJ\\HMZJ_H.bmp', 815, 1030)
    generalact.ImgFor3Cdelay1_Confirm('QNZL\\HMZJ\\HMZJ_H.bmp', 1090, 225)
    for i in range(4):
        generalact.moveclick_1s(1210 + i*110, 845)
        generalact.moveclick_1s(1030, 840)
    generalact.rangeclick02(8, 1510, 1010)
    # 1
    generalact.ImgWhile('QNZL\\HMZJ\\NAOMI.bmp', 0.9, 0, 0, 1920, 1080)  # 1
    generalact.moveclick_1s(158, 950)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\NAOMI.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\NAOMI_2.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ELENA.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ELENA_3.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\DANY.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\DANY_1.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ANA.bmp', 0.8, 0, 0, 1920, 1080)  # 2
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ANA_2.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\JIYAN.bmp', 0.8, 0, 0, 1920, 1080)  # 3
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\JIYAN_2.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    # 2
    generalact.ImgWhile('QNZL\\HMZJ\\NAOMI.bmp', 0.9, 0, 0, 1920, 1080)  # 1
    generalact.moveclick_1s(158, 950)  # P
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ELENA.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ELENA_3.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\NAOMI.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\NAOMI_1.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\STRANGER.bmp', 0.8, 0, 0, 1920, 1080)  # 2
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\STRANGER_2.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\JIYAN.bmp', 0.8, 0, 0, 1920, 1080)  # 3
    generalact.rangeclick02(5, 310, 830)
    # 3
    generalact.ImgWhile('QNZL\\HMZJ\\NAOMI.bmp', 0.9, 0, 0, 1920, 1080)  # 1
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ELENA.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\ELENA_2.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhile('QNZL\\HMZJ\\NAOMI.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 160, 750)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\YETANIA.bmp', 0.8, 0, 0, 1920, 1080)  # 2
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\YETANIA_2.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\STRANGER.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\STRANGER_1.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\RABIA.bmp', 0.8, 0, 0, 1920, 1080)  # 3
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\RABIA_3.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\RABIA.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\RABIA2_3.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhile('QNZL\\HMZJ\\JIYAN.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(158, 950)  # P
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\JIYAN.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\JIYAN2_2.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    generalact.ImgWhile('QNZL\\HMZJ\\JIYAN.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(158, 950)  # P
    generalact.moveclick_1s(158, 950)  # P
    generalact.moveclick_1s(158, 950)  # P
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\JIYAN.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\HMZJ\\JIYAN2_1.bmp', 0.8, 0, 0, 1920, 1080)
    CSauto.doubleClick()
    # time.sleep(10)
    # generalact.ImgShiftWhileDelay1Cdelay1('QNZL\\HMZJ\\again.bmp', 0.8, 0, 0, 1920, 1080, 200, 0)
    # time.sleep(2)
    # back3()


#  KUROKAMI KURORO RITSU
def Cbattle():
    # round 1
    # generalact.moveclick_1s(400, 977)  # C1
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\Cyetanniya.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\Cyetanniya2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\Cyetanniya2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\Cyetanniya.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KUROKAMI.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\MOMO2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\RITSU.bmp', 0.7, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DANY.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DANY1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\DANY1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\IRENE1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\IRENE1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.rangeclick02(2, 140, 960)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\NAFIE2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\APOPHIS2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\APOPHIS.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\APOPHIS1.bmp', 0.7, 1650, 250, 1920, 1080)
    # round 2
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\DIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\KRSNA.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KRSNA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KRSNA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\KRSNA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO3.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\MOMO3.bmp', 0.7, 1650, 250, 1920, 1080)
    # round 3
    generalact.ImgWhile('QNZL\\battle\\DANY.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KURORO.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(2, 140, 960)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KRSNA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KRSNA2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\KRSNA2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\DANY.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DANY.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DANY1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\DANY1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\NAFIE1.bmp', 0.7, 1650, 250, 1920, 1080)
    # round 4
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DIA2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\DIA2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\DIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\GERALDIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\IRENE2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\IRENE2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\Cyetanniya.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\Cyetanniya1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\Cyetanniya1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.rangeclick02(2, 140, 960)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\MOMO1.bmp', 0.7, 1650, 250, 1920, 1080)
    # round 5
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\DIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\DIA1.bmp', 0.7, 1650, 250, 1920, 1080)

    generalact.ImgWhile('QNZL\\battle\\AIKA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\AIKA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\AIKA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\AIKA1.bmp', 0.7, 1650, 250, 1920, 1080)

    generalact.ImgWhile('QNZL\\battle\\APOPHIS.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\APOPHIS2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\APOPHIS.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\APOPHIS1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\APOPHIS1.bmp', 0.7, 1650, 250, 1920, 1080)
    # round 6
    generalact.ImgWhile('QNZL\\battle\\DANY.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KUROKAMI.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\Cyetanniya.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\Cyetanniya2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\Cyetanniya2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\MOMO2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)

    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\RITSU.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\GERALDIA1.bmp', 0.7, 1650, 250, 1920, 1080)

    generalact.ImgWhile('QNZL\\battle\\KRSNA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KRSNA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\KRSNA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\KRSNA1.bmp', 0.7, 1650, 250, 1920, 1080)

    generalact.ImgWhile('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.rangeclick02(3, 140, 960)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\NAFIE2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\MOMO3.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\MOMO3.bmp', 0.7, 1650, 250, 1920, 1080)
    # round 7
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA2.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\GERALDIA2.bmp', 0.7, 1650, 250, 1920, 1080)

    generalact.ImgWhile('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\IRENE1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\IRENE1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    skip()
    # round 8
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\GERALDIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\GERALDIA1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhile('QNZL\\battle\\IRENE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.rangeclick1(2, 155, 737)

    generalact.ImgWhile('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.rangeclick02(3, 140, 960)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE.bmp', 0.7, 250, 850, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\battle\\NAFIE1.bmp', 0.7, 1650, 250, 1920, 1080)
    generalact.ImgWhileCdelay1('QNZL\\battle\\NAFIE1.bmp', 0.7, 1650, 250, 1920, 1080)


def HMZJmission():
    generalact.moveclick_05s(139, 690)
    generalact.rangeclick01(100, 1600, 350)


def skip():
    generalact.moveclick_1s(309, 824)


def attack():
    generalact.rangeclick1(2, 155, 737)


def quickbatall():
    generalact.ImgWhileCdelay1('QNZL\\attack_quick.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_05s(1752, 852)  # max
    generalact.moveclick_05s(1640, 1010)
    generalact.moveclick_05s(1640, 1010)
    # generalact.moveclick_05s(1660, 730)
    # generalact.moveclick_05s(1380, 830)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\attack_confirm.bmp', 0.9, 0, 0, 1920, 1080)


def QXZL(QXZLFLAG):
    if QXZLFLAG:
        generalact.moveclick_1s(105, 330)
        generalact.ImgWhile('QNZL\\QXZL.bmp', 0.8, 0, 0, 1920, 1080)
        for i in range(4):
            generalact.rangeclick01(4, 1777, 450)
            clickblock()
        backtomainui()


def huodongdailyget():
    generalact.moveclick_1s(1720, 80)
    clickblock()


def huodong_JDDS(dialy):  # 记得的事
    generalact.logger.info('QNZLfun.huodong_JDDS')
    generalact.ImgReturn1For3_Confirm('QNZL\\huodong\\huodongJDDS\\enterup.bmp', 1430, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongJDDS\\enterup.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1750, 550, 100, 550, 2)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongJDDS\\20.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    if dialy == 0:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongJDDS\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()
    backtomainui()


def huodong_YRYCF(dialy):  # 与日月重逢
    generalact.logger.info('QNZLfun.huodong_YRYCF')
    generalact.ImgReturn1For3_Confirm('QNZL\\huodong\\huodongYRYCF\\enterup.bmp', 1430, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongYRYCF\\enterup.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1750, 550, 100, 550, 2)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongYRYCF\\20.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    if dialy == 0:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongYRYCF\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()
    backtomainui()


def huodong_XZMFR(dialy):  # 新枝萌发日
    generalact.ImgReturn1For3_Confirm('QNZL\\huodong\\huodongXZMFR\\enterup.bmp', 1430, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongXZMFR\\enterup.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1750, 550, 100, 550, 2)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongXZMFR\\20.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    if dialy == 0:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongXZMFR\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()
    backtomainui()


def huodong_ZCDWD(dialy):  # 咫尺的温度
    generalact.ImgReturn1For3_Confirm('QNZL\\huodong\\huodongZCDWD\\enterup.bmp', 1430, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongZCDWD\\enterup.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1750, 550, 100, 550, 2)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongZCDWD\\20.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    if dialy == 0:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongZCDWD\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()
    backtomainui()


def huodong_MNZY(dialy):  # 魔女之夜
    generalact.ImgReturn1For3_Confirm('QNZL\\huodong\\huodongMNZY\\enter.bmp', 1430, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongMNZY\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1750, 550, 100, 550, 2)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongMNZY\\28.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    if dialy == 0:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongMNZY\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()
    backtomainui()


def huodong_RHLL(dialy):  # 忍花缭乱
    generalact.ImgReturn1For3_Confirm('QNZL\\huodong\\huodongRHLL\\enter.bmp', 1430, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongRHLL\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.dragmouse_count(1750, 550, 100, 550, 2)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongRHLL\\10.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    if dialy == 0:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongRHLL\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()
    backtomainui()


def huodong_ZGNAHQ(dialy):  # 知更鸟的安魂曲
    generalact.ImgReturn1For3_Confirm('QNZL\\huodong\\huodongZGNAHQ\\enter.bmp', 1430, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongZGNAHQ\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongZGNAHQ\\2.0.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    if dialy == 0:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongZGNAHQ\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()


def huodong_GSDAZS(dialy, huodongshop):  # 瑰色的爱之诗
    generalact.moveclick_1s(1672, 353)
    if huodongshop:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongGSDAZS\\enter.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongGSDAZS\\20.bmp', 0.9, 0, 0, 1920, 1080)
        quickbatall()
        back1()
    if dialy:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongGSDAZS\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()


def huodong_CGBF(dialy, huodongshop):
    generalact.moveclick_1s(1672, 353)
    # generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongCGBF\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    if huodongshop:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongCGBF\\22.bmp', 0.9, 0, 0, 1920, 1080)
        quickbatall()
        back1()
    if dialy:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongCGBF\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()


def huodong_TSML(dialy):
    generalact.moveclick_1s(1672, 353)
    if dialy:
        generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongTSML\\daily.bmp', 0.9, 0, 0, 1920, 1080)
        huodongdailyget()
        back1()
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongTSML\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongTSML\\stage20.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()


def huodong_231214():
    generalact.moveclick_1s(1672, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodong231214\\enter.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodong231214\\enter2.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
    back1()
    generalact.moveclick_1s(1672, 421)
    generalact.rangeclick01(8, 1717, 83)


def huodong_231130():
    generalact.moveclick_1s(1672, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodong231130\\commondown.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodong231130\\commondown14_4.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()


def huodong_MOMO():
    generalact.moveclick_1s(1672, 353)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongMOMO\\wakeup.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.ImgWhileDelay1Cdelay1('QNZL\\huodong\\huodongMOMO\\stage20.bmp', 0.9, 0, 0, 1920, 1080)
    quickbatall()
