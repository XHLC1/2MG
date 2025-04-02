import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag, huodongflag_stage, resourceflag, xinmaoflag):
    entergamefun()
    normal_shop(AFTD)
    recruit()
    YXJQ()
    getenergy()
    if huodongflag:
        huodong1_3(AFTD, huodongflag_stage)
    else:
        dabat(resourceflag)
    dabattebie(AFTD, xinmaoflag)
    mission(AFTD)
    gamecommunity(AFTD)
    theroom(AFTD)
    RZHY(AFTD)
    generalact.MUMUclose1()
    generalact.MUMUdrag2()


def entergamefun():
    generalact.logger.info('YXHSFun.entergamefun')
    n = 0
    m = 0
    generalact.imgcorrdinatefunenter('YXHS\\picture\\YXHS.bmp', 0.9, 0, 0, 1920, 1080, 0, -40)
    time.sleep(10)
    while 1:
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\update.bmp', 0.7, 990, 0, 1920, 1080)
        if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\close.bmp', 0.7, 990, 0, 1920, 1080):
            break
        time.sleep(1)
        n += 1
        if n > 60:
            generalact.MUMUclose1()
            m += 1
            if m > 3:
                CSauto.hotkey('alt', 'f4')
                generalact.startupMUMU(45)
            entergamefun()
            break
    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\register.bmp', 0.7, 0, 0, 1920, 1080):
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\logoin.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\logoin_account.bmp', 0.8, 0, 0, 1920, 1080)
        CSauto.typewrite('15317871835', interval=0.1)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\logoin_password.bmp', 0.8, 0, 0, 1920, 1080)
        CSauto.typewrite('a1181266134', interval=0.1)
        generalact.moveclick_1s(905, 605)
        generalact.rangeclick02(3, 1122, 700)
        time.sleep(3)
        if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\logoin1.bmp', 0.7, 0, 0, 1920, 1080):
            generalact.MUMUclose1()
            entergamefun()
        generalact.rangeclick02(3, 960, 680)
    while 1:
        generalact.moveclick_1s(940, 810)
        if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\user_agreement.bmp', 0.7, 0, 0, 1920, 1080):
            generalact.moveclick_1s(962, 623)
            generalact.moveclick_1s(678, 898)
            generalact.rangeclick02(3, 940, 810)
        if ~generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\age_limit.bmp', 0.7, 0, 0, 1920, 1080):
            break
    backtomainui()
    # generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\enter_download.bmp', 0.8, 0, 0, 1920, 1080)
    # generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\enter_download.bmp', 0.8, 0, 0, 1920, 1080)
    # backtomainui()


def theroom(AFTD):
    generalact.logger.info('YXHSFun.theroom')
    ypos = 0
    revalue = 0
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\theroom.bmp', 0.7, 0, 0, 1920, 1080)
    time.sleep(10)
    clickblock()
    generalact.rangeclick02(5, 1830, 200)
    generalact.rangeclick02(4, 1780, 1020)  # 解读
    for i in range(30):
        if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\theroom_zhuijia_A.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.rangeclick02(4, 1242, 780)
            if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\theroom_zhuijia_B.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.rangeclick02(4, 740, 780)
                break
        generalact.rangeclick02(4, 650, 270)
        generalact.rangeclick02(5, 1745, 400)  # 1
        if theroom_jiedu('YXHS\\picture\\theroom_lichademan.bmp'):  # 理查德曼
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_annita.bmp'):  # 安妮塔
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_libeika.bmp'):  # 莉贝卡
            continue
        generalact.rangeclick02(5, 1745, 510)  # 2
        if theroom_jiedu('YXHS\\picture\\theroom_lichademan.bmp'):  # 理查德曼
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_annita.bmp'):  # 安妮塔
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_libeika.bmp'):  # 莉贝卡
            continue
        generalact.rangeclick02(5, 1745, 630)  # 3
        if theroom_jiedu('YXHS\\picture\\theroom_lichademan.bmp'):  # 理查德曼
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_annita.bmp'):  # 安妮塔
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_libeika.bmp'):  # 莉贝卡
            continue
        generalact.rangeclick02(5, 1745, 760)  # 4
        if theroom_jiedu('YXHS\\picture\\theroom_lichademan.bmp'):  # 理查德曼
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_annita.bmp'):  # 安妮塔
            continue
        if theroom_jiedu('YXHS\\picture\\theroom_libeika.bmp'):  # 莉贝卡
            continue

        for j in range(5):
            if theroom_jiedu('YXHS\\picture\\theroom_beilasike.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_fuluolunsi.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_laola.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_linfang.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_wulaniya.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_zuitu.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_weilian.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_laina.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_chihu.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_xiangnan.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_sidier.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_linmei.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_aoweila.bmp'):
                revalue = 1
                break
            if theroom_jiedu('YXHS\\picture\\theroom_jiamila.bmp'):
                revalue = 1
                break
            generalact.dragmouse(1550, 500, 500, 500)
        if not revalue:
            for j in range(5):
                if theroom_jiedu('YXHS\\picture\\theroom_yeyin.bmp'):
                    revalue = 1
                    break
                if theroom_jiedu('YXHS\\picture\\theroom_xueli.bmp'):
                    revalue = 1
                    break
                if theroom_jiedu('YXHS\\picture\\theroom_bosipingxiaojie.bmp'):
                    revalue = 1
                    break
                if theroom_jiedu('YXHS\\picture\\theroom_yide.bmp'):
                    revalue = 1
                    break
                if theroom_jiedu('YXHS\\picture\\theroom_aoziman.bmp'):
                    revalue = 1
                    break
                generalact.dragmouse(500, 500, 1550, 500)
        if revalue:
            revalue = 0
        else:
            back3()
            break
    back3()
    if not AFTD:
        generalact.imgcorrdinatefunde1('YXHS\\picture\\theroom_inventory.bmp ', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\theroom_inventory.bmp', 0.8, 0, 0, 1920, 1080)
        for i in range(4):
            generalact.moveclick_1s(1250, 200 + ypos)
            generalact.moveclick_1s(1450, 1028)  # 分解
            generalact.dragmouse_count(673, 584, 1051, 578, 2)
            generalact.rangeclick02(8, 1225, 710)
            # clickblock()
            ypos += 200
        clickblock()
    backtomainui()


def theroom_jiedu(addr):
    if generalact.imgcorrdinatefunshiftclickcount3(addr, 0.8, 0, 0, 1920, 1080, 0, 500):
        clickblock()
        return 1


def dabat(resourceflag):
    # resourceflag 1 money 2 exp 3 心锚exp
    generalact.logger.info('YXHSFun.dabat')
    if resourceflag:
        enterzuozhan()
        generalact.rangeclick02(5, 1500, 1028)  # 资源筹备
        if resourceflag == 1:
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\dabat_money.bmp', 0.8, 0, 0, 1920, 1080)
        if resourceflag == 2:
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\dabat_exp.bmp', 0.8, 0, 0, 1920, 1080)
        if resourceflag == 3:
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\dabat_xinmao_exp.bmp', 0.8, 0, 0, 1920, 1080)
        quickbat()
        backtomainui()


def dabattebie(AFTD, xinmaoflag):
    # xinmaoflag 1 混合体 2 奇点列车 3洛伦佐 4 乐园梦魇 5 总控一号
    if AFTD:
        if xinmaoflag:
            enterzuozhan()
            generalact.rangeclick02(5, 1040, 1025)  # 特别行动
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\dabat_xinmao.bmp', 0.8, 0, 0, 1920, 1080)
            if xinmaoflag == 1:
                generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\dabat_xinmao_hunheti.bmp', 0.8, 0, 0, 1920, 1080)
            if xinmaoflag == 2:
                dabat_xinmaochoose('YXHS\\picture\\dabat_xinmao_qidianlieche.bmp')
            if xinmaoflag == 3:
                dabat_xinmaochoose('YXHS\\picture\\dabat_xinmao_luolunzuo.bmp')
            if xinmaoflag == 4:
                dabat_xinmaochoose('YXHS\\picture\\dabat_xinmao_leyuanmengyan.bmp')
            if xinmaoflag == 5:
                generalact.rangeclick02(5, 400, 185)  # 特级行动
                generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\dabat_xinmao_zongkongyihao.bmp', 0.8, 0, 0, 1920, 1080)
            quickbat()
            backtomainui()


def dabat_xinmaochoose(src):
    while 1:
        if generalact.imgcorrdinatefunclickcount3(src, 0.8, 0, 0, 1920, 1080):
            break
        else:
            generalact.dragmouse(370, 750, 370, 450)


def YXJQ():  # 周本
    generalact.logger.info('YXHSFun.YXJQ')
    if generalact.firstDayOfWeek6():
        enterzuozhan()
        generalact.rangeclick02(5, 826, 1017)
        generalact.moveclick_3s(1385, 580)
        generalact.moveclick_3s(1410, 1010)
        generalact.moveclick_3s(1290, 857)  # 出发
        backtomainui()


def getenergy():
    generalact.logger.info('YXHSFun.getenergy')
    generalact.rangeclick02(5, 543, 971)  # 活动
    if (generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\huodong_getenergy1.bmp', 0.8, 0, 0, 1920, 1080)
            or generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\huodong_getenergy2.bmp', 0.8, 0, 0, 1920, 1080)):
        generalact.rangeclick02(4, 646, 877)
        clickblock()
        generalact.rangeclick02(4, 1078, 883)
        clickblock()
        backtomainui()
        time.sleep(3)
        backtomainui()
    else:
        generalact.rangeclick01(2, 1755, 176)
        backtomainui()


def RZHY(AFTD):  # 认知海域 半月本
    if not AFTD:
        if generalact.firstDayOfWeek5() or generalact.firstDayOfWeek6():
        # if generalact.firstDayOfWeek5():
            generalact.logger.info('YXHSFun.RZHY')
            enterzuozhan()
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY.bmp', 0.8, 0, 0, 1920, 1080)
            n = 1
            if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_ABY13.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_3s(1700, 970)
                generalact.moveclick_3s(1270, 550)
                generalact.rangeclick02(5, 1560, 900)
                generalact.moveclick_3s(590, 690)
                while 1:
                    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_buff.bmp', 0.8, 0, 0, 1920, 1080):
                        if n == 1:
                            RZHY_buff('YXHS\\picture\\RZHY_buff_yingjihudun.bmp')
                        if n == 2:
                            RZHY_buff('YXHS\\picture\\RZHY_buff_shenxintiaohe.bmp')
                        if n == 3:
                            RZHY_buff('YXHS\\picture\\RZHY_buff_dikangqingshi.bmp')
                        if n == 4:
                            RZHY_buff('YXHS\\picture\\RZHY_buff_huanjingzhebi.bmp')
                        if n == 5:
                            RZHY_buff('YXHS\\picture\\RZHY_buff_shenmimoke.bmp')
                        n += 1
                    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_jifa.bmp', 0.8, 0, 0, 1920, 1080):
                        generalact.rangeclick02(4, 600, 550)
                        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_jifa.bmp', 0.8, 0, 0, 1920, 1080)
                        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_jifa.bmp', 0.8, 0, 0, 1920, 1080)
                        generalact.rangeclick02(4, 1816, 980)
                    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\bat_skip.bmp', 0.8, 0, 0, 1920, 1080)
                    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_continue.bmp', 0.8, 0, 0, 1920, 1080)
                    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_wangluozhongduan.bmp', 0.7, 0, 0, 1920, 1080)
                    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_success.bmp', 0.8, 0, 0, 1920, 1080):
                        clickblock()
                        clickblock()
                        clickblock()
                    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_stop.bmp', 0.8, 0, 0, 1920, 1080):
                        generalact.rangeclick02(10, 1085, 616)
                        backtomainui()
                        break
                    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\RZHY_finish.bmp', 0.8, 0, 0, 1920, 1080):
                        clickblock()
                        clickblock()
                        backtomainui()
                        break


def RZHY_buff(image):
    while 1:
        if generalact.imgcorrdinatefunclickcount3(image, 0.8, 0, 0, 1920, 1080):
            generalact.rangeclick02(4, 960, 1010)
            break
        else:
            generalact.dragmouse(1660, 540, 1200, 540)


def enterzuozhan():
    generalact.moveclick_3s(1248, 591)


def gamecommunity(AFTD):
    generalact.logger.info('YXHSFun.gamecommunity')
    if AFTD:
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\menu.bmp', 0.7, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\menu_community.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunde1('YXHS\\picture\\menu_community_signin.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 970, 700)
        generalact.imgcorrdinatefunde1('YXHS\\picture\\menu_community_signin_signin.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\menu_community_signin_signin.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 1250, 600)
        generalact.rangeclick01(20, 585, 870)  # 第二天
        generalact.rangeclick01(20, 585, 610)  # 第四天
        generalact.rangeclick01(20, 585, 355)  # 第六天
        backdown1()
        generalact.rangeclick02(5, 89, 74)
        backtomainui()
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mail.bmp', 0.7, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 315, 990)
        backtomainui()


def normal_shop(AFTD):
    generalact.logger.info('YXHSFun.entergamefun')
    if AFTD:
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_zhiyuanhuogui.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(4, 540, 418)
        clickblock()
        if generalact.firstDayOfMonth():
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan.bmp', 0.8, 0, 0, 1920,
                                                   1080)
            generalact.dragmouse_count(1800, 630, 400, 630, 2)
            if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_voucher.bmp', 0.8, 0, 0,
                                                   1920, 1080):
                generalact.rangeclick01(20, 1385, 610)
                generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_buy.bmp', 0.8, 0, 0,
                                                       1920,1080)
                clickblock()  # 1
            if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_waibuzhaopinshu.bmp', 0.8, 0,
                                                      0, 1920, 1080):
                generalact.rangeclick01(20, 1385, 610)
                generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_buy.bmp', 0.8, 0, 0,
                                                       1920, 1080)
                clickblock()  # 2
            ##紫心奖章
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_P.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_P1.bmp', 0.8, 0, 0, 1920, 1080)
            if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_voucher.bmp', 0.8, 0, 0,
                                                   1920, 1080):
                generalact.rangeclick01(20, 1385, 610)
                generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_buy.bmp', 0.8, 0, 0,
                                                       1920,1080)
                clickblock()  # 1
    backtomainui()


def recruit():
    generalact.logger.info('YXHSFun.recruit')
    generalact.imgcorrdinatefunde1('YXHS\\picture\\recruit.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunde1('YXHS\\picture\\recruit_extern.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick02(5, 1476, 827)
    while 1:
        if generalact.imgcorrdinatefuncount3P('YXHS\\picture\\recruit_extern_start.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.imgcorrdinatefunde1('YXHS\\picture\\recruit_extern_start.bmp', 0.8, 0, 0, 1920, 1080)
            break
        else:
            clickblock()
    generalact.rangeclick02(5, 1237, 577)
    generalact.rangeclick02(5, 1168, 733)
    backtomainui()


def mission_city_patrol(x, y, n):
    generalact.moveclick_1s(x, y)
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission_city_patrol_buy.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission_city_patrol_buy.bmp', 0.8, 0, 0, 1920, 1080)
    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission_city_patrol_buy.bmp', 0.8, 0, 0, 1920, 1080):
        clickblock()
        generalact.moveclick_1s(1577, 1013)  # 好友互助
        if n == 0:
            for i in range(4):
                for j in range(4):
                    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission_city_patrol_friend.bmp', 0.8, 0, 0,
                                                           1920, 1080)
                generalact.dragmouse(920, 900, 920, 300)
            generalact.rangeclick02(4, 1600, 335)
        else:
            generalact.rangeclick02(4, 1591, 912)
        clickblock()
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\close.bmp', 0.7, 990, 0, 1920, 1080)
        generalact.moveclick_1s(x, y)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission_city_patrol_buy.bmp', 0.8, 0, 0, 1920, 1080)
        n += 1
    clickblock()
    return n


def mission(AFTD):
    generalact.logger.info('YXHSFun.mission')
    if not AFTD:
        n = 0
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission.bmp', 0.8, 0, 0, 1920, 1080)
    #####################################################mission_city_patrol############################################
        generalact.imgcorrdinatefunde1('YXHS\\picture\\mission_city_patrol.bmp', 0.8, 0, 0, 1920, 1080)
        n = mission_city_patrol(1161, 294, n)  # 埃文钮维尔
        n = mission_city_patrol(1560, 347, n)  # 里湾区
        n = mission_city_patrol(808, 370, n)  # 旧镇区
        n = mission_city_patrol(1400, 520, n)  # 盾牌广场
        n = mission_city_patrol(866, 567, n)  # 东城区
        n = mission_city_patrol(1216, 662, n)  # 辛德区
        n = mission_city_patrol(1594, 756, n)  # 伊莱克兰
        n = mission_city_patrol(838, 791, n)  # 多尔区
        if n < 2:
            generalact.moveclick_1s(1577, 1013)  # 好友互助
            generalact.rangeclick02(4, 1591, 912)
            clickblock()
            generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\close.bmp', 0.7, 990, 0, 1920, 1080)
        generalact.rangeclick02(4, 1683, 875)
        clickblock()
    #####################################################mission_city_patrol############################################

    ###########################################################daily_mission############################################
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission_daily.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 1670, 1018)
        clickblock()
    ###########################################################daily_mission############################################

    ###########################################################week_mission#############################################
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\mission_week.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.rangeclick02(5, 1670, 1018)
        clickblock()
    ###########################################################week_mission#############################################
        backtomainui()
    if generalact.firstDayOfWeek7() and not AFTD:
        if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\passmission.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.rangeclick02(5, 1666, 977)
            clickblock()
            generalact.rangeclick02(5, 235, 555)
            generalact.rangeclick02(5, 1666, 977)
            clickblock()
            backtomainui()


def quickbat():
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\quickbat_complete.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.rangeclick01(10, 1475, 710)
    time.sleep(3)
    generalact.rangeclick01(5, 530, 640)  # blcok
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\quickbat_complete_start.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(3)
    clickblock()
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\quickbat_complete_end.bmp', 0.8, 0, 0, 1920, 1080)


def huodong1_3(AFTD, stage):  # 谜案回首
    generalact.moveclick_3s(1700, 500)
    generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 1:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\up1.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 2:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\up2.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 3:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\up3.bmp', 0.8, 0, 0, 1920, 1080)
    quickbat()
    backtomainui()
    if ~AFTD:
        generalact.moveclick_3s(1700, 500)
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\shop.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\shop_get.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_3\\shop_get.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.moveclick_1s(1525, 608)
        generalact.moveclick_1s(1400, 795)
        clickblock()
        backtomainui()


def huodong1_2(stage):  # 在月光之下
    generalact.moveclick_3s(1700, 500)
    generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_2\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_2\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 1:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_2\\up1.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 2:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_2\\up2.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 3:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_2\\up3.bmp', 0.8, 0, 0, 1920, 1080)
    quickbat()
    backtomainui()


def huodong1_1(stage):  # 处理时间奇物的三项建议
    generalact.moveclick_3s(1700, 500)
    generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_1\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_1\\enter.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 0:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_1\\up3.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 1:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_1\\up3.bmp', 0.8, 0, 0, 1920, 1080)
    if stage == 2:
        generalact.imgcorrdinatefunclickcount3('YXHS\\huodong\\1_1\\up3.bmp', 0.8, 0, 0, 1920, 1080)
    quickbat()
    backtomainui()


def backtomainui():
    generalact.logger.info('YXHSFun.backtomainui')
    n = 0
    while 1:
        if generalact.imgcorrdinatefuncount('YXHS\\picture\\XHL.bmp', 0.8, 320, 145, 1371, 868):
            back3()
            break
        else:
            n += 1
            if n > 100:
                CSauto.hotkey('alt', 'f4')
                generalact.startupMUMU(60)
                entergamefun()
            # break
            back1()
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\close.bmp', 0.7, 990, 0, 1920, 1080)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\update.bmp', 0.7, 990, 0, 1920, 1080)


def back1():
    generalact.moveclick_1s(185, 88)


def back2():
    generalact.moveclick_2s(185, 88)


def back3():
    generalact.moveclick_3s(185, 88)


def backdown1():
    generalact.moveclick_1s(64, 1050)


def backdown2():
    generalact.moveclick_2s(64, 1050)


def backdown3():
    generalact.moveclick_3s(64, 1050)


def clickblock():
    generalact.rangeclick02(5, 1030, 1060)


def test():
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_P.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_P1.bmp', 0.8, 0, 0, 1920, 1080)
    if generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_voucher.bmp', 0.8, 0, 0,
                                              1920, 1080):
        generalact.rangeclick01(20, 1385, 610)
        generalact.imgcorrdinatefunclickcount3('YXHS\\picture\\normal_shop_jiajiangduihuan_buy.bmp', 0.8, 0, 0,
                                               1920, 1080)
        clickblock()  # 1
