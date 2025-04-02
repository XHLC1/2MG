import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag, resourceflag, jiyifengbaoflag):
    entergamefun()
    time.sleep(5)
    backtomainui()
    qingxuguanli(AFTD)
    management(AFTD)
    supervise(AFTD)
    disichen(AFTD, jiyifengbaoflag, resourceflag)
    if AFTD:
        signin()
        guild()
        shop()
    else:
        friends()
        mission()
    generalact.MUMUclose1()
    generalact.MUMUdrag2()


def mission():
    generalact.logger.info('wuqimituFun.mission')
    generalact.rangeclick01(5, 1445, 980)  # 危机管理
    generalact.rangeclick02(4, 1750, 832)
    generalact.rangeclick02(4, 575, 1030)

    generalact.rangeclick02(4, 1612, 922)
    generalact.rangeclick02(10, 1750, 832)
    generalact.rangeclick02(5, 600, 450)
    generalact.rangeclick02(10, 1750, 905)
    generalact.rangeclick02(5, 600, 560)
    generalact.rangeclick02(1, 1750, 905)
    backtomainui()


def shop():
    generalact.logger.info('wuqimituFun.shop')
    generalact.rangeclick01(5, 1445, 980)  # 危机管理
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop.bmp', 0.9, 0, 0, 1920, 1080)
    ###########################################################daily shop gift##########################################
    generalact.imgcorrdinatefunde1('wuqimitu\\picture\\shop_jingxuan.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('wuqimitu\\picture\\shop_jingxuan_changgui.bmp', 0.8, 0, 0, 1920, 1080)
    if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_jingxuan_daily.bmp',
                                              0.8, 0, 0, 1920, 1080):
        pass
    else:
        generalact.dragmouse_count(1840, 550, 550, 550, 5)
        generalact.imgcorrdinatefunde1('wuqimitu\\picture\\shop_jingxuan_daily.bmp', 0.8, 0, 0, 1920, 1080)
    shop_buy()
    ###########################################################daily shop gift##########################################
    if generalact.firstDayOfMonth3():
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin.bmp',
                                                      0.8, 0, 0, 1920, 1080):
                break
            generalact.dragmouse(195, 960, 195, 780)
            time.sleep(1)
        for i in range(4):
            generalact.rangeclick01(5, 625, 308)
            shop_buy()
        # 兑换中心 战勋兑换
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_zhanxun.bmp',
                                                      0.9, 0, 0, 1920, 1080):
                generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_zhanxun.bmp',
                                                       0.9, 0, 0, 1920, 1080)
                break
            generalact.dragmouse(195, 960, 195, 780)
            time.sleep(1)
        generalact.rangeclick01(5, 625, 308)
        shop_buy()
        # 兑换中心 样本兑换
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_yangben.bmp',
                                                      0.9, 0, 0, 1920, 1080):
                generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_yangben.bmp',
                                                       0.9, 0, 0, 1920, 1080)
                break
            generalact.dragmouse(195, 960, 195, 780)
            time.sleep(1)
        for i in range(3):
            generalact.rangeclick01(5, 625, 308)
            shop_buy()
        # 兑换中心 联盟兑换
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_lianmeng.bmp',
                                                      0.9, 0, 0, 1920, 1080):
                generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_lianmeng.bmp',
                                                       0.9, 0, 0, 1920, 1080)
                break
            generalact.dragmouse(195, 960, 195, 780)
            time.sleep(1)
        for i in range(4):
            generalact.rangeclick01(5, 625, 308)
            shop_buy()
        generalact.rangeclick01(5, 970, 212)  # 中阶密盟兑换
        for i in range(2):
            generalact.rangeclick01(5, 625, 308)
            shop_buy()
        for i in range(4):
            generalact.rangeclick01(5, 725, 915)
            shop_buy()
        generalact.rangeclick01(5, 1230, 212)  # 高阶密盟兑换
        for i in range(2):
            generalact.rangeclick01(5, 625, 308)
            shop_buy()
        for i in range(6):
            generalact.rangeclick01(5, 725, 915)
            shop_buy()
        # 兑换中心 友情兑换
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_youqing.bmp',
                                                      0.9, 0, 0, 1920, 1080):
                generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_youqing.bmp',
                                                       0.9, 0, 0, 1920, 1080)
                break
            generalact.dragmouse(195, 960, 195, 780)
            time.sleep(1)
        for i in range(2):
            generalact.rangeclick01(5, 625, 308)
            shop_buy()
    if generalact.firstDayOfWeek():
        if not generalact.firstDayOfMonth3():
            while 1:
                if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin.bmp',
                                                          0.8, 0, 0, 1920, 1080):
                    break
                generalact.dragmouse(195, 960, 195, 780)
                time.sleep(1)
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_youqing.bmp',
                                                      0.9, 0, 0, 1920, 1080):
                generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_youqing.bmp',
                                                       0.9, 0, 0, 1920, 1080)
                break
            generalact.dragmouse(195, 960, 195, 780)
            time.sleep(1)
        for i in range(3):
            generalact.rangeclick01(5, 625, 308)
            shop_buy()
    if not generalact.firstDayOfMonth3() and not generalact.firstDayOfWeek():
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin.bmp',
                                                      0.8, 0, 0, 1920, 1080):
                break
            generalact.dragmouse(195, 960, 195, 780)
            time.sleep(1)
    while 1:
        if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_youqing.bmp',
                                                  0.9, 0, 0, 1920, 1080):
            generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_duihuanzhongxin_youqing.bmp',
                                                   0.9, 0, 0, 1920, 1080)
            break
        generalact.dragmouse(195, 960, 195, 780)
        time.sleep(1)
    for i in range(3):
        generalact.rangeclick01(5, 625, 308)
        shop_buy()
    backtomainui()


def shop_buy():
    generalact.rangeclick01(5, 1463, 735)
    generalact.rangeclick01(5, 1523, 737)
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\shop_buy.bmp', 0.9, 0, 0, 1920, 1080)
    clickblock()
    clickblock()


# resourceflag 1 狄斯币 2 狂乱精粹 3 污染之巢 7 各个三倍 > 10 帕尔玛废墟
def disichen(AFTD, jiyifengbaoflag, resourceflag):
    generalact.logger.info('wuqimituFun.disichen')
    if AFTD:
        ######################################################zhuoanzhijin##############################################
        enterdisichen(0)
        generalact.rangeclick01(4, 586, 647)  # 浊暗之井
        while 1:
            if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\zhuoanzhijin.bmp', 0.9, 0, 0, 1920, 1080):
                generalact.rangeclick01(4, 1800, 795)
                break
            generalact.moveclick_2s(960, 940)
        backtomainui()
        ######################################################zhuoanzhijin##############################################
        if jiyifengbaoflag:
            ###########################################################jiyifengbao######################################
            enterdisichen(1)
            generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\jisicheng_jiyifengbao.bmp', 0.9, 0, 0, 1920, 1080)
            generalact.moveclick_1s(1575, 915)
            quickbat()
            backtomainui()
            ###########################################################jiyifengbao######################################
    if resourceflag == 1:
        ##############################################################disibi############################################
        enterdisichen(1)
        generalact.rangeclick01(4, 1175, 170)
        quickbat()
        backtomainui()
        ##############################################################disibi############################################
    if resourceflag == 2:
        #####################################################kuangluanjincui############################################
        enterdisichen(1)
        generalact.rangeclick01(4, 1345, 190)
        quickbat()
        backtomainui()
        #####################################################kuangluanjincui############################################
    if resourceflag == 3:
        ######################################################wuranzhicaho##############################################
        enterdisichen(1)
        generalact.rangeclick01(4, 900, 640)
        quickbat()
        backtomainui()
        ######################################################wuranzhicaho##############################################
    if resourceflag == 7:
        ######################################################wuranzhicaho##############################################
        if AFTD:
            enterdisichen(1)
            generalact.rangeclick01(4, 1175, 170)  # 狄斯币
            quickbat()
            backtomainui()
        else:
            enterdisichen(1)
            generalact.rangeclick01(4, 1345, 190)
            quickbat3()
            backtomainui()

            enterdisichen(1)
            generalact.rangeclick01(4, 900, 640)  # 污染之巢
            quickbat()
            backtomainui()
        ######################################################wuranzhicaho##############################################


def quickbat3():
    generalact.rangeclick01(4, 1620, 710)
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\quickbat.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 555, 717)
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\quickbat_start.bmp', 0.9, 0, 0, 1920, 1080)


def quickbat():
    generalact.rangeclick01(4, 1620, 710)
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\quickbat.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\quickbat_start.bmp', 0.9, 0, 0, 1920, 1080)


# where 0 内海 1 绣河
def enterdisichen(where):
    generalact.logger.info('wuqimituFun.enterdisichen')
    generalact.rangeclick01(5, 1445, 980)  # 危机管理
    generalact.rangeclick01(5, 1740, 280)  # 狄斯城
    time.sleep(1)
    if where:
        generalact.rangeclick01(5, 375, 990)
    else:
        generalact.rangeclick01(5, 1630, 995)


def guild():
    generalact.logger.info('wuqimituFun.guild')
    generalact.rangeclick01(5, 1580, 1000)  # 整备中心
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\guild.bmp', 0.9, 0, 0, 1920, 1080)
    clickblock()
    backtomainui()
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\guild.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('wuqimitu\\picture\\guild_donate.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(5, 540, 900)
    clickblock()
    if generalact.firstDayOfWeek6():
        back1()
        generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\guild_help.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(15, 250, 1020)
    backtomainui()


def friends():
    generalact.logger.info('wuqimituFun.friends')
    generalact.rangeclick01(5, 1580, 1000)  # 整备中心
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\friends.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1715, 950)
    clickblock()
    backtomainui()


def supervise(AFTD):
    generalact.logger.info('wuqimituFun.supervise')
    generalact.rangeclick01(5, 1580, 1000)  # 整备中心
    generalact.imgcorrdinatefunde1('wuqimitu\\picture\\supervise.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.rangeclick01(5, 295, 535)
    clickblock()
    if not AFTD:
        generalact.rangeclick01(5, 315, 330)
        generalact.rangeclick01(5, 1710, 650)
        for i in range(5):
            generalact.rangeclick01(25, 1680, 960)
            generalact.rangeclick01(25, 1680, 900)
    backtomainui()


def management(AFTD):
    generalact.logger.info('wuqimituFun.management')
    generalact.rangeclick01(5, 1445, 980)  # 危机管理
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\management.bmp', 0.9, 0, 0, 1920, 1080)
    if not AFTD:
        generalact.moveclick_1s(313, 512)
        generalact.rangeclick01(6, 1408, 535)
        generalact.rangeclick01(6, 1050, 920)
        generalact.rangeclick01(6, 1410, 825)
        clickblock()
    generalact.imgcorrdinatefunde1('wuqimitu\\picture\\management_errand.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('wuqimitu\\picture\\management_errand_get.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1670, 830)
    backtomainui()


def qingxuguanli(AFTD):
    if AFTD:
        generalact.moveclick_1s(200, 495)
        generalact.rangeclick02(15, 1425, 590)
        if generalact.firstDayOfMonth2():
            generalact.rangeclick02(10, 860, 915)
        if generalact.firstDayOfMonth8():
            generalact.rangeclick02(10, 1065, 915)
        if generalact.firstDayOfMonth15():
            generalact.rangeclick02(10, 1285, 915)
        if generalact.firstDayOfMonth25():
            generalact.rangeclick02(10, 1505, 915)
        backtomainui()


def signin():
    generalact.logger.info('wuqimituFun.signin')
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\signin.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(4, 1374, 631)
    clickblock()
    backtomainui()


def entergamefun():
    generalact.logger.info('wuqimituFun.entergamefun')
    n = 0
    generalact.imgcorrdinatefunenter('wuqimitu\\picture\\wuqimitu.bmp', 0.9, 42, 181, 1780, 1000, 0, -40)
    time.sleep(10)
    while 1:
        time.sleep(1)
        n += 1
        if generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\login.bmp', 0.7, 0, 0, 1920, 1080):
            generalact.moveclick_1s(818, 616)
            CSauto.typewrite('a1181266134', interval=0.1)
            generalact.rangeclick02(4, 1200, 777)
        generalact.moveclick_1s(62, 1061)
        generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\entergame.bmp', 0.7, 0, 0, 1920, 1080)
        generalact.rangeclick02(4, 1764, 120)
        generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\sure.bmp', 0.7, 0, 0, 1920, 1080)
        if generalact.imgcorrdinatefuncount3('wuqimitu\\picture\\XHL.bmp', 0.7, 0, 0, 1920, 1080):
            generalact.rangeclick02(4, 1764, 120)
            time.sleep(1)
            generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\sure.bmp', 0.7, 0, 0, 1920, 1080)
            generalact.rangeclick02(4, 1764, 120)
            break
        if n > 60:
            generalact.MUMUclose1()
            entergamefun()
            break


def backtomainui():
    while 1:
        if generalact.imgcorrdinatefuncount('wuqimitu\\picture\\supervise.bmp', 0.9, 0, 0, 1920, 1080):
            break
        if generalact.imgcorrdinatefuncount('wuqimitu\\picture\\role.bmp', 0.9, 0, 0, 1920, 1080):
            break
        back1()


def back05():
    generalact.moveclick_05s(94, 92)


def back1():
    generalact.moveclick_1s(94, 92)


def back2():
    generalact.moveclick_2s(94, 92)


def back3():
    generalact.moveclick_3s(94, 92)


def clickblock():
    generalact.rangeclick01(6, 941, 1064)


def fortest():
    enterdisichen(1)
    generalact.imgcorrdinatefunclickcount3('wuqimitu\\picture\\jisicheng_jiyifengbao.bmp', 0.9, 0, 0, 1920, 1080)
    generalact.moveclick_1s(1575, 915)
    quickbat()
    backtomainui()

