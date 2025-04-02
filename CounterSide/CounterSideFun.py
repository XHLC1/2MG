import base64
import time
import general_actions as generalact
import pyautogui as CSauto
from CounterSide.yanhuacanzhao_bmp import img as yanhuacanzhao
import sys

sys.path.append(r"C:\\Code\\PythonCode\\withUI\\LO\\PC")
import LOPCFun

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]

tmp = open('yanhuacanzhao.png', 'wb')  # 创建临时的文件
tmp.write(base64.b64decode(yanhuacanzhao))  # 把这个one图片解码出来，写入文件中去。
tmp.close()


def dailytaskst():
    guild()
    reclaim()
    fight(1, 0, 1, 1, 0, 1, 1, 1, 1, 1,  # 收藏
          1, 0, 0, 1, 1, 0, 0)
    shop(1)
    shopbuyup()
    firm()
    shengkai(1)
    employee()


def guild():
    print('CounterSideFun.guild')
    generalact.moveclick_1s(213, 138)
    time.sleep(2)
    blockmid1()
    blockmid1()
    blockmid1()
    time.sleep(3)
    generalact.moveclick_1s(186, 1011)  # 捐款
    generalact.moveclick_1s(955, 865)
    generalact.moveclick_1s(1148, 672)
    generalact.enterdelay_1s()
    backtomainui()


def reclaim():
    print('CounterSideFun.reclaim')
    generalact.moveclick_3s(1447, 997)  # 管理局
    generalact.moveclick_1s(1791, 1000)
    generalact.moveclick_1s(1584, 1000)
    generalact.moveclick_1s(1584, 1000)
    generalact.moveclick_1s(1791, 1000)
    generalact.enterdelay_1s()
    backtomainui()


def fight(bugeizuozhanflag, bugeizuozhanflag1_8, bugeizuozhanflag1_7, bugeizuozhanflag1_6, bugeizuozhanflag1_5,
          monizhanflag, monizhanflaggongji, monizhanflagfangyu, monizhanflagfangkong, anyingdiantang,
          shoucangflag, shoucangflag1, shoucangflag2, shoucangflag3, shoucangflag4, shoucangflag5, shoucangflag6):
    print('CounterSideFun.fight')
    generalact.moveclick_3s(1432, 689)
    if bugeizuozhanflag:
        generalact.moveclick_3s(1210, 984)  # 委托
        generalact.moveclick_1s(813, 863)
        if bugeizuozhanflag1_8:
            generalact.moveclick_1s(271, 565)
            generalact.moveclick_05s(1273, 1003)
            generalact.moveclick_05s(1057, 590)  # 执行机密作战
            skipbattledw5()
            generalact.escdelay_1s()
        if bugeizuozhanflag1_7:
            generalact.moveclick_1s(271, 565)
            generalact.moveclick_05s(1273, 1003)
            generalact.moveclick_05s(428, 599)  # 执行机密作战
            skipbattledw5()
            generalact.escdelay_1s()
        if bugeizuozhanflag1_6:
            generalact.moveclick_1s(271, 565)
            generalact.moveclick_05s(1273, 1003)
            generalact.moveclick_05s(428, 599)  # 执行机密作战
            generalact.moveclick_05s(428, 599)
            skipbattledw5()
            generalact.escdelay_1s()
        if bugeizuozhanflag1_5:
            generalact.moveclick_1s(271, 565)
            generalact.moveclick_05s(1273, 1003)
            generalact.moveclick_05s(428, 599)  # 执行机密作战
            generalact.moveclick_05s(428, 599)
            generalact.moveclick_05s(428, 599)
            skipbattledw5()
            generalact.escdelay_1s()
        # generalact.escdelay_1s()

    if monizhanflag:
        generalact.moveclick_1s(1545, 988)  # 成长
        if monizhanflaggongji:
            generalact.moveclick_05s(377, 527)
            generalact.moveclick_05s(718, 604)
            skipbattledw5()
            generalact.escdelay_1s()
        if monizhanflagfangyu:
            generalact.moveclick_05s(673, 527)
            generalact.moveclick_05s(718, 604)
            skipbattledw5()
            generalact.escdelay_1s()
        if monizhanflagfangkong:
            generalact.moveclick_05s(952, 527)
            generalact.moveclick_05s(718, 604)
            skipbattledw5()
            generalact.escdelay_1s()
    if anyingdiantang:
        generalact.moveclick_1s(1545, 988)  # 成长
        generalact.moveclick_3s(1435, 357)
        generalact.moveclick_02s(1299, 996)
        for i in range(5):
            generalact.moveclick_02s(1780, 885)
        generalact.moveclick_02s(1625, 1011)
        queren()
        time.sleep(1)
    if shoucangflag:
        generalact.moveclick_1s(1798, 1013)  # ★
        if shoucangflag1:
            generalact.moveclick_4s(1473, 343)
            skipbattleup10()
        if shoucangflag2:
            generalact.moveclick_4s(1473, 461)
            skipbattleup10()
        if shoucangflag3:
            generalact.moveclick_4s(1473, 566)
            skipbattleup10()
        if shoucangflag4:
            generalact.moveclick_4s(1473, 650)
            skipbattleup10()
        if shoucangflag5:
            generalact.moveclick_4s(1473, 750)
            skipbattleup10()
        if shoucangflag6:
            generalact.moveclick_4s(1473, 850)
            skipbattleup10()
        generalact.escdelay_1s()
    backtomainui()


def skipbattledw5():
    generalact.moveclick_02s(1242, 988)
    for i in range(5):
        generalact.moveclick_02s(1695, 848)
    generalact.enterdelay_1s()
    queren()


def skipbattleup10():
    generalact.moveclick_02s(1830, 170)
    for i in range(10):
        generalact.moveclick_02s(1714, 863)
    generalact.moveclick_02s(1572, 998)
    queren()


def queren():
    generalact.imgcorrdinatefunenter('CounterSide\\queren.bmp', 0.9, 0, 0, 1920, 1080, 0, 0)
    for i in range(4):
        generalact.moveclick_02s(1034, 932)


def shop(flashflag):
    print('CounterSideFun.shop')
    generalact.moveclick_3s(170, 842)
    generalact.moveclick_1s(196, 1008)
    generalact.moveclick_1s(590, 620)
    shopbuydw()
    shopbuyup()
    if flashflag:
        for i in range(5):
            generalact.moveclick_05s(1666, 905)
            generalact.moveclick_1s(1122, 824)
            shopbuydw()
            shopbuyup()
    generalact.moveclick_1s(300, 388)
    generalact.imgcorrdinatefun3('CounterSide\\LZZBS.bmp', 0.8, 0, 0, 1980, 1080)
    generalact.moveclick_1s(900, 680)
    generalact.moveclick_1s(1090, 930)
    backtomainui()


def shopbuyup():
    # generalact.imgcorrdinatefunshift('CounterSide\\coinupde.bmp', 0.8, 711, 294, 300, 100, 0, 0)
    # generalact.imgcorrdinatefunwhile('CounterSide\\coinupde.bmp', 0.8, 711, 294, 1060, 425)
    generalact.imgcorrdinatefun3('CounterSide\\coinup.bmp', 0.6, 711, 294, 400, 200)
    generalact.imgcorrdinatefun3('CounterSide\\coinup.bmp', 0.6, 1056, 294, 400, 200)
    generalact.imgcorrdinatefun3('CounterSide\\heipiao.bmp', 0.8, 711, 155, 400, 200)
    generalact.imgcorrdinatefun3('CounterSide\\heipiao.bmp', 0.8, 1056, 155, 400, 200)
    # generalact.moveclick_1s(1127, 801)
    generalact.moveclick_05s(1777, 992)
    generalact.moveclick_05s(1072, 894)


def shopbuydw():
    x = 0
    y = 0
    for i in range(2):
        for j in range(3):
            generalact.moveclick_02s(509 + x, 588 + y)
            x += 350
        x = 0
        y += 280
    # generalact.moveclick_05s(1777, 992)
    # generalact.moveclick_05s(1072, 894)
    # generalact.imgcorrdinatefunenter('CounterSide\\coindw.bmp', 0.9, 350 + x, 280 + y, 1400, 1050, 0, 0)
    # generalact.moveclick_1s(1127, 801)
    # generalact.imgcorrdinatefunenter('CounterSide\\coindw.bmp', 0.9, 350, 750, 1400, 1050, 0, 0)
    # generalact.moveclick_1s(1127, 801)


def shopMW():
    print('CounterSideFun.shopMW')
    if generalact.firstDayOfMonth():
        pass
    #     generalact.imgcorrdinatefunde1('CounterSide\\shop.bmp', 0.9, 0, 0, 1920, 1080)
    #     generalact.imgcorrdinatefunde1('CounterSide\\shoplist.bmp', 0.9, 0, 0, 1920, 1080)
    if generalact.firstDayOfWeek():
        generalact.imgcorrdinatefunde1('CounterSide\\shop.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CounterSide\\shoplist.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_1s(561, 562)  # 交换所
        generalact.moveclick_1s(131, 388)  # 便利道具
        for i in range(20):
            CSauto.press("right")
        generalact.moveclick_1s(1020, 804)  # 融合核心
        if generalact.imgcorrdinatefuncount3('CounterSide\\ronghehexin.bmp', 0.9, 0, 0, 1920, 1080):
            generalact.moveclick_05s(1071, 691)
            generalact.moveclick_05s(1083, 808)
        else:
            generalact.escdelay_1s()
        generalact.moveclick_05s(131, 929)  # 跃入
        for i in range(20):
            CSauto.press("right")
        generalact.moveclick_05s(1709, 430)
        shopMWbuy()
        generalact.moveclick_05s(1357, 430)
        shopMWbuy()
        generalact.moveclick_05s(1000, 430)
        shopMWbuy()
        generalact.moveclick_05s(969, 866)
        shopMWbuy()
        generalact.moveclick_05s(643, 866)
        shopMWbuy()
        generalact.dragmouse(144, 818, 144, 151)
        generalact.imgcorrdinatefun('CounterSide\\shop_AYDT.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(546, 402)
        shopMWbuy()
        generalact.moveclick_05s(524, 817)
        shopMWbuy()
        generalact.moveclick_05s(850, 424)
        shopMWbuy()
        generalact.imgcorrdinatefun('CounterSide\\shop_caituan.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(531, 416)
        shopMWbuy()
        generalact.moveclick_05s(522, 821)
        shopMWbuy()
        CSauto.press("down")
        time.sleep(0.5)
        generalact.moveclick_05s(531, 416)
        shopMWbuy()
        generalact.moveclick_05s(522, 821)
        shopMWbuy()
        generalact.moveclick_05s(895, 438)
        shopMWbuy()
        generalact.moveclick_05s(896, 800)
        shopMWbuy()
        generalact.imgcorrdinatefunde1('CounterSide\\shoplist.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(936, 645)
        generalact.imgcorrdinatefunde1('CounterSide\\changzhuxiandinglibao.bmp', 0.9, 0, 0, 1920, 1080)
        CSauto.press("down")
        generalact.imgcorrdinatefunde1('CounterSide\\mimiguyongzuanshilibao.bmp', 0.9, 0, 0, 1920, 1080)
        generalact.moveclick_05s(1100, 858)
        backtomainui()


def shopMWbuy():
    generalact.moveclick_01s(1071, 691)
    CSauto.mouseDown()
    time.sleep(3)
    CSauto.mouseUp()
    generalact.moveclick_05s(1083, 808)


def firm():
    print('CounterSideFun.firm')
    generalact.moveclick_3s(1107, 988)  # 总公司
    generalact.moveclick_1s(487, 983)
    generalact.moveclick_1s(731, 620)
    generalact.moveclick_1s(1813, 988)
    generalact.moveclick_1s(1452, 899)
    generalact.moveclick_2s(1689, 878)
    generalact.escdelay_1s()
    generalact.escdelay_1s()
    generalact.moveclick_1s(1820, 811)  # 聚餐
    generalact.moveclick_3s(1139, 855)
    generalact.escdelay_1s()
    generalact.escdelay_1s()
    backtomainui()


def shengkai(shengkaiflag):
    print('CounterSideFun.shengkai')
    if shengkaiflag == 0:
        pass
    else:
        if generalact.firstDayOfWeek():
            generalact.moveclick_4s(1411, 822)  # 圣凯
            generalact.imgcorrdinatefunde1('CounterSide\\PVPauto.bmp', 0.8, 0, 0, 1920, 1080)
            time.sleep(2)
            generalact.enterdelay_1s()
            backtomainui()
        generalact.moveclick_4s(1411, 822)  # 圣凯
        generalact.imgcorrdinatefunde1('CounterSide\\PVPauto.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('CounterSide\\PVPnpc.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1238, 649)
        generalact.imgcorrdinatefunde1('CounterSide\\PVPstart.bmp', 0.8, 0, 0, 1920, 1080)
        CSauto.moveTo(1111, 1000)
        generalact.imgcorrdinatefunenter('CounterSide\\zhandoutongji.bmp', 0.9, 0, 0, 1920, 1080, -600, 0)
        time.sleep(2)
        CSauto.click()
        time.sleep(2)
        CSauto.click()
        time.sleep(1)
        if shengkaiflag == 3:
            shengkaibattle(3)
        if shengkaiflag == 6:
            shengkaibattle(6)
        if shengkaiflag == 9:
            shengkaibattle(9)
        backtomainui()


def shengkaibattle(counter):
    for i in range(counter):
        generalact.moveclick_1s(1238, 649)
        generalact.imgcorrdinatefunde1('CounterSide\\PVPstart.bmp', 0.8, 0, 0, 1920, 1080)
        CSauto.moveTo(1111, 1000)
        generalact.imgcorrdinatefunenter('CounterSide\\zhandoutongji.bmp', 0.9, 0, 0, 1920, 1080, -600, 0)
        time.sleep(2)
        CSauto.click()
        time.sleep(2)
        CSauto.click()
        time.sleep(1)


def employee():
    print('CounterSideFun.employee')
    generalact.moveclick_3s(1801, 989)  # 雇佣
    generalact.moveclick_1s(317, 255)
    while 1:
        if generalact.imgcorrdinatefuncount('CounterSide\\suishiguyong.bmp', 0.9, 450, 400, 1100, 900) == 1:
            generalact.moveclick_1s(1238, 1012)
            generalact.moveclick_1s(1118, 821)
            break
        else:
            CSauto.press("down")
            time.sleep(1)


def completeup():  # 探索
    print('CounterSideFun.completeup')
    dispatchflag = 1
    teamflag = 1
    count = 0
    while 1:
        if generalact.gl_timeflag == 1 or generalact.gl_timeflag1 == 1 or generalact.gl_timeflag2 == 1:
            break
        if dispatchflag > 0:
            dispatchflag -= 1
            generalact.moveclick_1s(227, 854)
            if generalact.imgcorrdinatefuncount3('CounterSide\\explore_tuanben.bmp', 0.8, 0, 0, 600, 400):
                if teamflag == 0:
                    generalact.moveclick_1s(1616, 438)
                    generalact.moveclick_1s(1168, 774)
                    generalact.escdelay_1s()
                else:
                    generalact.moveclick_3s(1637, 524)  # 现在就去
                    generalact.moveclick_1s(707, 906)
                    generalact.moveclick_1s(1067, 807)
                    generalact.escdelay_3s()
            if generalact.imgcorrdinatefuncount3('CounterSide\\explore_yueru.bmp', 0.8, 0, 0, 600, 400):
                generalact.moveclick_3s(1637, 524)  # 现在就去
                # generalact.moveclick_1s(1277, 990)  # 强袭
                generalact.moveclick_3s(1538, 1013)
                generalact.moveclick_3s(1538, 1013)
                completeconfirmwhileyueru()
            else:
                generalact.escdelay_1s()
        if dispatchflag > 0:
            pass
        else:
            while 1:
                if generalact.imgcorrdinatefunshiftclickcount3P('CounterSide\\complete_LDS.bmp', 0.9, 40, 300, 200, 100,
                                                               0,
                                                               0):  # LDS
                    dispatchflag = 5
                    time.sleep(30)
                    generalact.moveclick_1s(140, 554)  # LDS
                    generalact.rangeclick02(10, 1111, 1000)
                    break
                if generalact.imgcorrdinatefunshiftclickcount3P('CounterSide\\complete_CLD.bmp', 0.9, 390, 50, 200, 100,
                                                               0,
                                                               0):  # CLD
                    dispatchflag = 5
                    time.sleep(30)
                    generalact.moveclick_1s(470, 265)  # CLD
                    generalact.rangeclick02(10, 1111, 1000)
                    break
                if generalact.imgcorrdinatefunshiftclickcount3P('CounterSide\\complete_ADC.bmp', 0.9, 780, 130, 200, 100,
                                                               0,
                                                               0):  # ADC
                    dispatchflag = 5
                    time.sleep(30)
                    generalact.moveclick_1s(857, 334)  # ADC
                    generalact.rangeclick02(10, 1111, 1000)
                    break
                if generalact.imgcorrdinatefunshiftclickcount3P('CounterSide\\complete_QW.bmp', 0.9, 835, 600, 200, 100,
                                                               0,
                                                               0):  # QW
                    dispatchflag = 5
                    time.sleep(30)
                    generalact.moveclick_1s(921, 845)  # QW
                    generalact.rangeclick02(10, 1111, 1000)
                    break
                if generalact.imgcorrdinatefunshiftclickcount3P('CounterSide\\complete_HYS.bmp', 0.9, 1400, 110, 200,
                                                               100, 0,
                                                               0):  # HYS
                    dispatchflag = 5
                    time.sleep(30)
                    generalact.moveclick_1s(1485, 325)  # HYS
                    generalact.rangeclick02(10, 1111, 1000)
                    break
                if generalact.imgcorrdinatefunshiftclickcount3P('CounterSide\\complete_KPMT.bmp', 0.9, 1750, 440, 200,
                                                               100, 0,
                                                               0):  # KPMT
                    dispatchflag = 5
                    time.sleep(30)
                    generalact.moveclick_1s(1852, 664)  # KPMT
                    generalact.rangeclick02(10, 1111, 1000)
                    break
                break
        if dispatchflag == 5:
            time.sleep(1)
            explore_mission6()
        explore_back()
        if count > 100:
            MUMUBACK1()
            LOPCFun.expedition()
            CSBACK()
            if generalact.imgcorrdinatefuncount3P('CounterSide\\tuanduifubenbianji.bmp', 0.9, 0, 0, 1980, 1080):
                generalact.moveclick_1s(200, 845)
                if generalact.imgcorrdinatefuncount3('CounterSide\\explore_tuanben.bmp', 0.8, 0, 0, 600, 400):
                    if teamflag == 0:
                        generalact.moveclick_1s(1616, 286)
                        generalact.moveclick_1s(1168, 774)
                        generalact.escdelay_1s()
                    else:
                        generalact.moveclick_3s(1637, 524)  # 现在就去
                        generalact.moveclick_1s(707, 906)
                        generalact.moveclick_1s(1067, 807)
                        generalact.escdelay_1s()
                if generalact.imgcorrdinatefuncount3('CounterSide\\explore_yueru.bmp', 0.8, 0, 0, 600, 400):
                    generalact.moveclick_3s(1637, 524)  # 现在就去
                    # generalact.moveclick_1s(1277, 990)  # 强袭
                    generalact.moveclick_3s(1538, 1013)
                    generalact.moveclick_3s(1538, 1013)
                    print("aac")
                    completeconfirmwhileyueru()
                generalact.moveclick_1s(235, 515)
                generalact.rangeclick01(8, 1666, 936)
                # generalact.moveclick_1s(1800, 157)
                generalact.rangeclick01(6, 1800, 157)
                count = 0
            if count > 150:
                back1()
            if count > 300:
                break
        count += 1
        print(count)


def explore_mission6():
    generalact.moveclick_1s(140, 554)  # LDS
    if generalact.imgcorrdinatefuncount3P('CounterSide\\explore_mission_continue.bmp', 0.9, 1200, 600, 1980, 1080):
        back1()
    else:
        # generalact.rangeclick01(5, 1111, 1000)
        # generalact.moveclick_1s(140, 554)  # LDS
        explore_mission()

    generalact.moveclick_1s(470, 265)  # CLD
    if generalact.imgcorrdinatefuncount3P('CounterSide\\explore_mission_continue.bmp', 0.9, 1200, 600, 1980, 1080):
        back1()
    else:
        # generalact.rangeclick01(5, 1111, 1000)
        # generalact.moveclick_1s(470, 265)  # CLD
        explore_mission()

    generalact.moveclick_1s(857, 334)  # ADC
    if generalact.imgcorrdinatefuncount3P('CounterSide\\explore_mission_continue.bmp', 0.9, 1200, 600, 1980, 1080):
        back1()
    else:
        # generalact.rangeclick01(5, 1111, 1000)
        # generalact.moveclick_1s(857, 334)  # ADC
        explore_mission()

    generalact.moveclick_1s(921, 845)  # QW
    if generalact.imgcorrdinatefuncount3P('CounterSide\\explore_mission_continue.bmp', 0.9, 1200, 600, 1980, 1080):
        back1()
    else:
        # generalact.rangeclick01(5, 1111, 1000)
        # generalact.moveclick_1s(921, 845)  # QW
        explore_mission()

    generalact.moveclick_1s(1485, 325)  # HYS
    if generalact.imgcorrdinatefuncount3P('CounterSide\\explore_mission_continue.bmp', 0.9, 1200, 600, 1980, 1080):
        back1()
    else:
        # generalact.rangeclick01(5, 1111, 1000)
        # generalact.moveclick_1s(1485, 325)  # HYS
        explore_mission()

    generalact.moveclick_1s(1852, 664)  # KPMT
    if generalact.imgcorrdinatefuncount3P('CounterSide\\explore_mission_continue.bmp', 0.9, 1200, 600, 1980, 1080):
        back1()
    else:
        # generalact.rangeclick01(5, 1111, 1000)
        # generalact.moveclick_1s(1852, 664)  # KPMT
        explore_mission()

    back1()
    explore_back()


def explore_mission():
    while 1:
        if generalact.imgcorrdinatefunshiftclickcount3('CounterSide\\guyongjuan.bmp', 0.9, 1060, 750, 1900, 950, 0, -200):
            completecfm()
            break
        if generalact.imgcorrdinatefunshiftclickcount3('CounterSide\\diamond.bmp', 0.9, 1481, 750, 1900, 950, 0, -200):
            completecfm()
            break
        if generalact.imgcorrdinatefunshiftclickcount3('CounterSide\\monijuan.bmp', 0.9, 1060, 750, 420, 250, 0, -200):
            completecfm()
            break
        else:
            generalact.moveclick_1s(867, 552)
            completecfm()
        break
    if generalact.imgcorrdinatefuncount3P('CounterSide\\tuanduifubenbianji.bmp', 0.9, 0, 780, 400, 1080):
        pass
    else:
        back1()
        explore_back()


def explore_back():
    if generalact.imgcorrdinatefuncount3P('CounterSide\\explore_back2.bmp', 0.9, 0, 0, 400, 400):
        print("aaa")
        generalact.moveclick_1s(1700, 830)


def completedw():
    generalact.imgcorrdinatefunenterP('CounterSide\\CompleteQW.bmp', 0.9, 0, 0, 1920, 1080, -20, 150)


def completeconfirm():
    while 1:
        if generalact.imgcorrdinatefuncount('CounterSide\\tuanduifubenbianji.bmp', 0.9, 0, 780, 400, 1080) == 1:
            generalact.moveclick_1s(1108, 809)
            break
        else:
            # break
            generalact.moveclick_1s(1108, 809)


def completeconfirmwhile():
    generalact.imgcorrdinatefunwhile('CounterSide\\tuanduifubenbianji.bmp', 0.9, 0, 780, 400, 1080)


def completeconfirmwhileyueru():
    while 1:
        if generalact.imgcorrdinatefuncount3('CounterSide\\tuanduifubenbianji.bmp', 0.9, 0, 780, 400, 1080):
            break
        explore_back()


def completecfm():
    generalact.moveclick_1s(1103, 808)  # 确认
    back1()


def backtomainui():
    while 1:
        # if generalact.imgcorrdinatefuncount('CounterSide\\yanhuacanzhao.bmp', 0.9, 560, 120, 1500, 400) == 1:
        if generalact.imgcorrdinatefuncount('CounterSide\\xingheluo.bmp', 0.9, 0, 0, 1920, 1080) == 1:
            back3()
            break
        else:
            # break
            back02()


def blockmid1():
    generalact.moveclick_1s(1065, 983)


def back02():
    generalact.moveclick_02s(121, 77)


def back1():
    generalact.moveclick_1s(121, 77)


def back2():
    generalact.moveclick_2s(121, 77)


def back3():
    generalact.moveclick_3s(121, 77)


def CSBACK():
    generalact.moveclick_3s(1918, 1078)
    CSauto.press("win")
    generalact.imgcorrdinatefunde1b2('CounterSideUI\\CSBACK.bmp', 0.8, 0, 0, 1920, 1080)


def MUMUBACK1():
    generalact.moveclick_3s(1918, 1078)
    CSauto.press("win")
    generalact.imgcorrdinatefunclickcount3('MUMU\\mumuback.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 325, 20)


def test():
    LOPCFun.expedition()
    pass

# backtomainui()
