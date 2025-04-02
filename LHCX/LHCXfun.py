import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag):
    if AFTD:
        entergamefun()
        signin()
        character()
        shop()
        homeland()
        explore(2)
        guild(AFTD, 0)
        if huodongflag:
            huodong3_0()
        dailymission()
        generalact.MUMUclose1()
        generalact.MUMUdrag2()
    else:
        entergamefun()
        homelandN()
        guild(AFTD, 1)
        YXZG()
        if huodongflag:
            huodong3_0()
        dailymission()
        generalact.MUMUmain()
        generalact.MUMUdrag2()


def entergamefun():
    generalact.logger.info('YXHSFun.entergamefun')
    n = 0
    m = 0
    generalact.imgcorrdinatefunenter('LHCX\\LHCX.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    time.sleep(10)
    while 1:
        generalact.imgcorrdinatefunclickcount3('LHCX\\startconfirm.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('LHCX\\startdownload.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('LHCX\\enterconfirm.bmp', 0.9, 0, 0, 1920, 1080)
        if generalact.imgcorrdinatefunclickcount3('LHCX\\register.bmp', 0.9, 0, 0, 1920, 1080):
            generalact.rangeclick05(2, 960, 695)
            generalact.moveclick_1s(775, 417)
            CSauto.typewrite('13512182584', interval=0.1)
            generalact.moveclick_1s(792, 514)
            CSauto.typewrite('a1181266134', interval=0.1)
            generalact.moveclick_1s(828, 606)
        n += 1
        if n > 60:
            generalact.MUMUclose1()
            m += 1
            if m > 3:
                CSauto.hotkey('alt', 'f4')
                generalact.startupMUMU(45)
            entergamefun()
            break
        generalact.rangeclick05(2, 996, 804)
        time.sleep(1)
        if (generalact.imgcorrdinatefunclickcount3('LHCX\\enterbreak1.bmp', 0.9, 0, 0, 1920, 1080)
                or generalact.imgcorrdinatefunclickcount3('LHCX\\enterbreak2.bmp', 0.9, 0, 0, 1920, 1080)):
            break
    backtomainui()


def signin():
    generalact.logger.info('LHCXfun.signin')
    generalact.moveclick_1s(1827, 176)
    generalact.imgcorrdinatefunde1('LHCX\\signin.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('LHCX\\signin2.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 612, 936)
    generalact.rangeclick02(4, 90, 90)
    backtomainui()


def backtomainui():
    flag = 0
    while 1:
        if generalact.imgcorrdinatefuncount('LHCX\\ID.bmp', 0.9, 1200, 250, 1920, 1080):
            generalact.moveclick_1s(1708, 264)
            break
        else:
            if flag:
                back1()
                flag = 0
            else:
                back1R()
                flag = 1


def character():
    generalact.logger.info('LHCXfun.character')
    # generalact.moveclick_1s(851, 409)  # 祈愿
    generalact.moveclick_1s(1143, 670)  # 相伴
    generalact.imgcorrdinatefunwhile('LHCX\\concomitant.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick3(6, 959, 321)
    for i in range(7):
        generalact.dragmouse(1000, 1000, 277, 1000)
    generalact.moveclick_1s(962, 985)
    generalact.moveclick_2s(1370, 985)
    generalact.rangeclick02(2, 1720, 710)  # 4L4R
    # for i in range(4):
    #     generalact.dragmouse(1480, 750, 1480, 220)
    # generalact.imgcorrdinatefunde1('LHCX\\giftH.bmp', 0.9, 1000, 120, 1920, 1080)
    # generalact.imgcorrdinatefun('LHCX\\giftH.bmp', 0.9, 1000, 120, 1920, 1080)
    generalact.moveclick_05s(1477, 965)
    if generalact.firstDayOfWeek7():
        generalact.rangeclick1(3, 1477, 965)
    backtomainui()


def CYSY(choice, ov):
    generalact.logger.info('LHCXfun.CYSY')
    if choice == 1:  # 巨木森林
        generalact.rangeclick02(4, 232, 332)  # 探索
        generalact.rangeclick02(4, 1752, 848)  # 次元深渊
        generalact.imgcorrdinatefunwhile('LHCX\\CYSY.bmp', 0.7, 0, 0, 1920, 1080)
        time.sleep(1)
        for i in range(3):
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin.bmp', 0.9, 0, 0, 1920, 1080):
                generalact.moveclick_5s(960, 1000)
                generalact.moveclick_5s(1800, 815)
                generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_biandui.bmp', 0.9, 0, 0, 1920, 1080)
                generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_biandui2.bmp', 0.9, 0, 0, 1920, 1080)
                generalact.moveclick_5s(1725, 1000)
                break
            else:
                generalact.moveclick_5s(1650, 580)
        generalact.rangeclick02(4, 738, 678)
        time.sleep(3)
        CYSY_MOVE(1333, 807)
        if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_quick.bmp', 0.9, 0, 0, 1920, 1080):
            generalact.moveclick_1s(814, 600)
            generalact.moveclick_1s(1142, 684)
        CYSY_BUFF(choice)
        CYSY_MOVE(1250, 525)
        CYSY_MOVE(1267, 660)
        CYSY_BUFF(choice)
        CYSY_MOVE(957, 937)
        CYSY_BUFF(choice)
        CYSY_MOVE(675, 820)
        CYSY_MOVE(655, 823)
        CYSY_BUFF(choice)
        CYSY_MOVE(668, 812)
        CYSY_BUFF(choice)
        CYSY_MOVE(1262, 818)
        CYSY_MOVE(1272, 822)
        generalact.rangeclick02(8, 920, 865)
        generalact.rangeclick02(8, 1600, 545)
        back3()
        CYSY_MOVE(1248, 814)
        CYSY_MOVE(1568, 888)
        CYSY_BUFF(choice)
        CYSY_MOVE(1241, 735)
        CYSY_MOVE(1257, 593)
        CYSY_BUFF(choice)
        CYSY_MOVE(1558, 660)  # BOSS
        while 1:
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_success.bmp', 0.8, 0, 0, 1920, 1080):
                clickblock()
                break
        CYSY_BUFF(choice)
        CYSY_MOVE(1258, 525)
        CYSY_MOVE(690, 525)
        back3()
        CYSY_MOVE(665, 530)
        CYSY_BUFF(choice)
        CYSY_MOVE(1257, 538)
        CYSY_MOVE(1262, 523)
        CYSY_BUFF(choice)
        CYSY_MOVE(1543, 676)
        CYSY_BUFF(choice)
        CYSY_MOVE(1258, 673)
        CYSY_MOVE(1278, 670)
        generalact.rangeclick02(8, 1591, 870)  # 紫
        generalact.rangeclick02(8, 948, 870)  # 蓝
        generalact.rangeclick02(8, 1272, 530)  # 绿
        back3()
        CYSY_MOVE(1548, 525)
        CYSY_BUFF(choice)
        CYSY_MOVE(1250, 810)
        CYSY_MOVE(1263, 540)
        CYSY_BUFF(choice)
        CYSY_MOVE(1545, 666)
        CYSY_BUFF(choice)
        CYSY_MOVE(1250, 815)
        CYSY_MOVE(1270, 822)
        back3()
        CYSY_MOVE(1551, 676)
        while 1:
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_success.bmp', 0.8, 0, 0, 1920, 1080):
                clickblock()
                break
        CYSY_MOVE(1263, 663)
        if ov:
            CYSY_MOVE(1332, 668)
            CYSY_MOVE(638, 920)
            generalact.rangeclick02(10, 960, 1018)
            backtomainui()
        else:
            generalact.moveclick_1s(132, 95)
            generalact.moveclick_1s(1100, 628)


def CYSY_MOVE(x, y):
    generalact.rangeclick02(2, x, y)
    time.sleep(5)


def CYSY_BUFF(choice):
    n = 0
    while 1:
        if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_BUFF.bmp', 0.8, 0, 0, 1920, 1080):
            n = 1
            break
        if choice == 1:
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_1.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(1325, 915)  # 2
                generalact.rangeclick02(5, 970, 915)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_2.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.moveclick_3s(970, 915)
                CYSY_BUFF(choice)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_3.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.rangeclick02(5, 970, 915)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_4.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.moveclick_3s(970, 915)
                CYSY_BUFF(choice)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_5.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.rangeclick02(5, 970, 915)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_6.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(1325, 915)  # 2
                generalact.rangeclick02(5, 970, 915)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_7.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.moveclick_3s(970, 915)
                CYSY_BUFF(choice)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_8.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.moveclick_3s(970, 915)
                CYSY_BUFF(choice)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_9.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.moveclick_3s(970, 915)
                CYSY_BUFF(choice)
                break
            if generalact.imgcorrdinatefunclickcount3('LHCX\\CYSY_jumusenlin_10.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(635, 915)  # 1
                generalact.moveclick_3s(970, 915)
                CYSY_BUFF(choice)
                break
    while 1:
        if n == 1:
            if generalact.imgcorrdinatefunshiftclickcount3P('LHCX\\CYSY_BUFF_duoduan.bmp', 0.9, 0, 0, 1920, 1080,
                                                            80, 80):
                pass
            else:
                if generalact.imgcorrdinatefunshiftclickcount3P('LHCX\\CYSY_BUFF_gandian.bmp', 0.9, 0, 0, 1920, 1080,
                                                                80, 80):
                    pass
                else:
                    if generalact.imgcorrdinatefunshiftclickcount3P('LHCX\\CYSY_BUFF_leidian.bmp', 0.9, 0, 0, 1920, 1080,
                                                                    80, 80):
                        pass
                    else:
                        if generalact.imgcorrdinatefunshiftclickcount3P('LHCX\\CYSY_BUFF_baofa.bmp', 0.9, 0, 0, 1920, 1080,
                                                                        80, 80):
                            pass
                        else:
                            if generalact.imgcorrdinatefunshiftclickcount3P('LHCX\\CYSY_BUFF_qunti.bmp', 0.9, 0, 0, 1920, 1080,
                                                                            80, 80):
                                pass
                            else:
                                if generalact.imgcorrdinatefunshiftclickcount3P('LHCX\\CYSY_BUFF_danti.bmp', 0.9, 0, 0, 1920, 1080,
                                                                                80, 80):
                                    pass
                                else:
                                    if generalact.imgcorrdinatefunshiftclickcount3P('LHCX\\CYSY_BUFF_H.bmp', 0.9, 0, 0, 1920, 1080, 80, 80):
                                        pass
                                    else:
                                        generalact.moveclick_1s(525, 465)
            generalact.moveclick_1s(1220, 820)
            break
        else:
            break


def shop():
    generalact.logger.info('LHCXfun.shop')
    generalact.moveclick_3s(1812, 1024)
    # generalact.imgcorrdinatefunde1('LHCX\\Redemptionshop.bmp', 0.8, 0, 0, 1920, 1080)
    # generalact.imgcorrdinatefunde1('LHCX\\shop.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunshiftde1('LHCX\\shop.bmp', 0.8, 0, 0, 1920, 1080, 0, 5)
    generalact.imgcorrdinatefunde1('LHCX\\supplypack.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('LHCX\\dailysupplypack.bmp', 0.8, 0, 0, 1920, 1080)
    # generalact.imgcorrdinatefunde1('LHCX\\buy.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1139, 788)
    generalact.rangeclick02(4, 90, 90)
    backtomainui()
    if generalact.firstDayOfWeek():
        generalact.moveclick_1s(1812, 1024)
        generalact.imgcorrdinatefunshiftde1('LHCX\\shop_change.bmp', 0.8, 0, 0, 1920, 1080, 0, 5)
        generalact.imgcorrdinatefunde1('LHCX\\shop_change_gaojishangjuan.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(885, 450)  # 1L2R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
        generalact.moveclick_1s(520, 818)  # 2L1R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
    if generalact.firstDayOfMonth():
        generalact.moveclick_1s(1812, 1024)
        generalact.imgcorrdinatefunshiftde1('LHCX\\shop_change.bmp', 0.8, 0, 0, 1920, 1080, 0, 5)
        # generalact.imgcorrdinatefunde1('LHCX\\supplypack.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(520, 450)  # 1L1R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
        generalact.imgcorrdinatefunde1('LHCX\\shop_change_gaojishangjuan.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(520, 450)  # 1L1R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
        generalact.dragmouse_count(190, 963, 210, 343, 3)
        generalact.imgcorrdinatefunde1('LHCX\\shop_change_yingmishangpu.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(520, 450)  # 1L1R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
        generalact.moveclick_1s(885, 450)  # 1L2R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
        generalact.moveclick_1s(1333, 450)  # 1L3R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
        generalact.moveclick_1s(1855, 450)  # 1L5R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
        generalact.moveclick_1s(895, 818)  # 2L2R
        generalact.moveclick_1s(1393, 676)  # MAX
        generalact.moveclick_1s(1139, 788)
        clickblock()
    backtomainui()


def homeland():
    generalact.logger.info('LHCXfun.homeland')
    generalact.moveclick_02s(717, 600)
    generalact.imgcorrdinatefunwhile('LHCX\\homeland.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('LHCX\\get.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 932, 745)
    clickblock()
    generalact.moveclick_1s(100, 413)
    for i in range(3):
        generalact.imgcorrdinatefunde1('LHCX\\receive.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 976, 926)
    generalact.imgcorrdinatefun3('LHCX\\receive.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 976, 926)
    plant()
    for i in range(2):
        generalact.rangeclick01(10, 976, 926)
        generalact.rangeclick01(2, 1476, 926)
    generalact.rangeclick01(10, 976, 926)
    back1()
    homelandback()
    generalact.moveclick_1s(100, 413)
    generalact.moveclick_1s(315, 900)  # 事务中心
    while 1:
        if generalact.imgcorrdinatefuncount('LHCX\\affairs3.bmp', 0.8, 100, 280, 320, 110) == 1:
            break
        else:
            generalact.moveclick_1s(250, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 440, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250 + 300, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 780, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250+300+300, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 1130, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250+300+300+320, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 1480, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250+300+300+320+400, 873)
    generalact.imgcorrdinatefunde1('LHCX\\yijianpaiqian.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 176, 87)
    backtomainui()
    generalact.moveclick_02s(717, 600)
    generalact.imgcorrdinatefunwhile('LHCX\\homeland.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(106, 603)
    generalact.imgcorrdinatefunde1('LHCX\\visit.bmp', 0.8, 0, 0, 1920, 1080)
    count = 0
    while 1:
        time.sleep(7)
        if generalact.imgcorrdinatefunclickcount3('LHCX\\box.bmp', 0.7, 0, 0, 1920, 1080):
            count += 1
            generalact.rangeclick01(4, 1024, 100)
        if generalact.imgcorrdinatefunclickcount3('LHCX\\box1.bmp', 0.7, 0, 0, 1920, 1080):
            count += 1
            generalact.rangeclick01(4, 1024, 100)
        generalact.rangeclick01(4, 116, 1047)
        if count >= 5:
            break
    generalact.rangeclick02(4, 176, 87)
    backtomainui()


def homelandN():
    generalact.logger.info('LHCXfun.homelandN')
    generalact.moveclick_02s(717, 600)
    generalact.imgcorrdinatefunwhile('LHCX\\homeland.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(100, 413)
    for i in range(3):
        generalact.imgcorrdinatefunde1('LHCX\\receive.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 976, 926)
    generalact.imgcorrdinatefun3('LHCX\\receive.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 976, 926)
    plant()
    for i in range(2):
        generalact.rangeclick01(10, 976, 926)
        generalact.rangeclick01(2, 1476, 926)
    generalact.rangeclick01(10, 976, 926)
    back1()
    homelandback()
    generalact.moveclick_1s(100, 413)
    generalact.moveclick_1s(315, 900)  # 事务中心
    while 1:
        if generalact.imgcorrdinatefuncount('LHCX\\affairs3.bmp', 0.8, 100, 280, 320, 110) == 1:
            break
        else:
            generalact.moveclick_1s(250, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 440, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250 + 300, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 780, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250+300+300, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 1130, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250+300+300+320, 873)
    while 1:
        if generalact.imgcorrdinatefuncount1('LHCX\\affairs3.bmp', 0.8, 1480, 280, 320, 110):
            break
        else:
            generalact.moveclick_1s(250+300+300+320+400, 873)
    generalact.imgcorrdinatefunde1('LHCX\\yijianpaiqian.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 176, 87)
    backtomainui()


def plant():
    generalact.imgcorrdinatefunde1('LHCX\\plant.bmp', 0.8, 0, 0, 1920, 1080)


def homelandback():
    generalact.imgcorrdinatefunmovenoclick('LHCX\\homeland.bmp', 0.8, 0, 0, 1920, 1080, 90, 90)


def explore(shilian):
    generalact.logger.info('LHCXfun.explore')
    # generalact.moveclick_1s(433, 426)
    # generalact.moveclick_1s(433, 426)
    # generalact.moveclick_1s(695, 415)  # 18-4
    # sweep()
    # generalact.rangeclick02(5, 90, 90)
    backtomainui()
    if shilian:
        generalact.moveclick_1s(433, 426)
        generalact.imgcorrdinatefun('LHCX\\explore_shilian.bmp', 0.8, 0, 0, 1920, 1080)
        if shilian == 1:  # 烙印
            generalact.imgcorrdinatefun('LHCX\\explore_laoying.bmp', 0.8, 0, 0, 1920, 1080)
            sweep3()
        if shilian == 2:  # 经验
            generalact.imgcorrdinatefun('LHCX\\explore_jingyan.bmp', 0.8, 0, 0, 1920, 1080)
            sweep3()


def YXZG():
    if generalact.firstDayOfWeek5():
        generalact.logger.info('LHCXfun.YXZG')
        generalact.moveclick_1s(433, 426)
        generalact.imgcorrdinatefun('LHCX\\explore_shilian.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('LHCX\\YXZG.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1825, 860)
        for i in range(2):
            generalact.dragmouse(1375, 800, 1400,330)
        generalact.imgcorrdinatefunde1('LHCX\\YXZGteam.bmp', 0.8, 0, 0, 1920, 1080)
        for i in range(10):
            generalact.imgcorrdinatefunde1('LHCX\\YXZGstart.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.imgcorrdinatefunde1('LHCX\\YXZGend.bmp', 0.8, 0, 0, 1920, 1080)
        backtomainui()


def sweep():
    generalact.imgcorrdinatefunde1('LHCX\\quicksettlement.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(5, 1135, 555)
    generalact.imgcorrdinatefun('LHCX\\confirm.bmp', 0.8, 0, 0, 1920, 1080)


def sweep2():
    generalact.imgcorrdinatefun3('LHCX\\quicksettlement2.bmp', 0.6, 1300, 900, 1920, 1080)
    generalact.rangeclick01(5, 1135, 555)
    generalact.imgcorrdinatefun3('LHCX\\confirm.bmp', 0.8, 0, 0, 1920, 1080)


def sweep3():
    generalact.moveclick_05s(1400, 1000)
    generalact.imgcorrdinatefun('LHCX\\explore_max.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_05s(950, 730)
    generalact.rangeclick02(5, 90, 90)
    backtomainui()


def guild(AFTD, guild6):
    generalact.logger.info('LHCXfun.guild')
    generalact.moveclick_1s(1647, 1020)
    generalact.imgcorrdinatefunwhile('LHCX\\guild3.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.moveclick_1s(900, 663)  # 悬赏卷
    generalact.rangeclick02(5, 176, 87)
    backtomainui()
    generalact.moveclick_1s(1647, 1020)
    generalact.imgcorrdinatefunwhile('LHCX\\guild3.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(8, 1411, 296)
    guildback()
    generalact.moveclick_1s(1411, 296)
    if AFTD == 0 and (generalact.firstDayOfWeek() or generalact.firstDayOfWeek2()):
        for i in range(3):
            generalact.moveclick_1s(1672, 1021)
            generalact.imgcorrdinatefun('LHCX\\bat_getitem.bmp', 0.8, 0, 0, 1920, 1080)
            clickblock()
    if guild6:
        generalact.moveclick_1s(219, 686)
    sweep2()
    guildback()
    generalact.moveclick_1s(1671, 1013)

    generalact.rangeclick01(8, 737, 914)
    generalact.rangeclick01(8, 1628, 916)
    generalact.rangeclick02(3, 176, 87)
    backtomainui()


def dailymission():
    generalact.moveclick_1s(1360, 1024)
    generalact.rangeclick01(8, 400, 900)
    backtomainui()


def huodong3_0():
    generalact.logger.info('LHCXfun.huodong3_0')
    generalact.confirm_nocilck3('LHCX\\huodong\\tansuo.bmp', 290, 400)
    generalact.dragmouse_count(126, 840, 126, 192, 3)
    generalact.imgcorrdinatefun('LHCX\\huodong\\3_0\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun('LHCX\\huodong\\3_0\\enter1.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefun('LHCX\\huodong\\3_0\\get.bmp', 0.8, 0, 0, 1920, 1080)
    clickblock()
    backtomainui()


def guildback():
    generalact.imgcorrdinatefunmovenoclick('LHCX\\guild3.bmp', 0.8, 0, 0, 1920, 1080, 90, 90)


def back1():
    generalact.moveclick_1s(90, 90)


def back2():
    generalact.moveclick_2s(90, 90)


def back3():
    generalact.moveclick_3s(90, 90)


def back1R():
    generalact.moveclick_1s(148, 76)


def back2R():
    generalact.moveclick_2s(148, 76)


def back3R():
    generalact.moveclick_3s(148, 76)


def clickblock():
    generalact.rangeclick01(6, 941, 1064)

