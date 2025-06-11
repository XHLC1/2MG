import time
import general_actions as generalact
import pyautogui as CSauto
import pywinio

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]


def dailytaskst(AFTD, huodongflag, huodongflag_stage, resourceflag, xinmaoflag):
    entergamefun()


def entergamefun():
    pass


def expedition(huodong):
    count = 0
    generalact.ImgFor3Cdelay1('LO\\PC\\picture\\expedition_com3.bmp', 0.8, 0, 0, 1920, 1080)
    back_world()
    ZZZD_B(huodong)
    while 1:
        count += 1
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\reconnect.bmp', 0.8, 0, 0, 1920, 1080)
        if generalact.ImgShiftFor3Cdelay1('LO\\PC\\picture\\expedition_com1.bmp', 0.8, 0, 0, 1920, 1080, 0, -50):
            if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\expedition_com2.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.ImgFor3Cdelay1('LO\\PC\\picture\\expedition_com3.bmp', 0.8, 0, 0, 1920, 1080)
            else:
                generalact.ImgShiftFor3Cdelay1('LO\\PC\\picture\\expedition_com1.bmp', 0.8, 0, 0, 1920, 1080, 0, -50)
                generalact.ImgFor3Cdelay1('LO\\PC\\picture\\expedition_com2.bmp', 0.8, 0, 0, 1920, 1080)
                generalact.ImgFor3Cdelay1('LO\\PC\\picture\\expedition_com3.bmp', 0.8, 0, 0, 1920, 1080)
        else:
            break
        if count > 20:
            break
    back1()
    generalact.moveclick_1s(242, 95)
    generalact.ImgFor3Cdelay1('LO\\PC\\picture\\menu_base.bmp', 0.8, 0, 0, 1920, 1080)
    base(0)


def base(gongfangflag):
    while 1:
        if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\base_resource.bmp', 0.8, 0, 0, 1920, 1080):
            time.sleep(1)
            generalact.ImgFor3Cdelay1('LO\\PC\\picture\\base_continue.bmp', 0.8, 0, 0, 1920, 1080)
            time.sleep(3)
        else:
            break
    generalact.moveclick_1s(242, 95)
    if gongfangflag:
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\menu_gongfang.bmp', 0.8, 0, 0, 1920, 1080)
        time.sleep(3)
        gongfang_base()
        # gongfang_equip()
    else:
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\menu_world.bmp', 0.8, 0, 0, 1920, 1080)
        time.sleep(3)
        generalact.moveclick_1s(1260, 675)


def gongfang_equip():
    generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_equip.bmp', 0.8, 0, 0, 1920, 1080)
    generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_equip.bmp', 0.8, 0, 0, 1920, 1080)
    while 1:
        if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_complete.bmp', 0.8, 0, 0, 1920, 1080):
            time.sleep(3)
            generalact.rangeclick05(2, 1550, 960)
        else:
            break
    while 1:
        if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_build.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.moveclick_1s(1550, 960)
            time.sleep(3)
            if generalact.ImgReturn1For3('LO\\PC\\picture\\gongfang_build.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_build.bmp', 0.8, 0, 0, 1920, 1080)
                generalact.moveclick_1s(1571, 964)
            else:
                time.sleep(3)
                break
        else:
            break
    generalact.moveclick_1s(242, 95)
    generalact.ImgFor3Cdelay1('LO\\PC\\picture\\menu_world.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(3)
    generalact.moveclick_1s(1260, 675)


def gongfang_base():
    generalact.rangeclick02(5, 1766, 736)
    while 1:
        if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_complete.bmp', 0.8, 0, 0, 1920, 1080):
            while 1:
                if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_complete1.bmp', 0.8, 0, 0, 1920, 1080):
                    time.sleep(3)
                    if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_complete1.bmp', 0.8, 0, 0,
                                                              1920, 1080):
                        pass
                    else:
                        break
                else:
                    generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_complete.bmp', 0.8, 0, 0, 1920,
                                                           1080)
        else:
            break
    while 1:
        if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_build.bmp', 0.8, 0, 0, 1920, 1080):
            generalact.moveclick_1s(1550, 960)
            time.sleep(3)
            if generalact.ImgReturn1For3('LO\\PC\\picture\\gongfang_build.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.ImgFor3Cdelay1('LO\\PC\\picture\\gongfang_build.bmp', 0.8, 0, 0, 1920, 1080)
                generalact.moveclick_1s(1571, 964)
            else:
                time.sleep(3)
                break
        else:
            break
    generalact.moveclick_1s(242, 95)
    generalact.ImgFor3Cdelay1('LO\\PC\\picture\\menu_world.bmp', 0.8, 0, 0, 1920, 1080)
    time.sleep(3)
    generalact.moveclick_1s(1260, 675)


def ZZZD_A(huodong):
    if (generalact.ImgFor3Cdelay1('LO\\PC\\picture\\zizhuzhandou_complete.bmp', 0.8, 0, 0, 1920, 1080)
            or generalact.ImgFor3Cdelay1('LO\\PC\\picture\\zizhuzhandou_complete1.bmp', 0.8, 0, 0, 1920, 1080)):
        time.sleep(3)
        generalact.rangeclick02(4, 1650, 950)
        backtomainui()
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\world.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\world.bmp', 0.8, 0, 0, 1920, 1080)
        if huodong:
            generalact.rangeclick02(4, 1037, 385)
            generalact.rangeclick02(4, 1852, 884)
        else:
            generalact.ImgFor3Cdelay1('LO\\PC\\picture\\world_bat.bmp', 0.8, 0, 0, 1920, 1080)
            generalact.ImgFor3Cdelay1('LO\\PC\\picture\\world_bat.bmp', 0.8, 0, 0, 1920, 1080)
        return 1


def ZZZD_B(huodong):
    if ZZZD_A(huodong):
    # if 1:
        if huodong:
            generalact.moveclick_1s(1800, 180)
            # generalact.moveclick_1s(1382, 586)
            generalact.moveclick_1s(1115, 450)
            if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\zizhuzhandou.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.moveclick_1s(1485, 412)  # C S
                generalact.moveclick_1s(1357, 412)  # C SS
                generalact.moveclick_1s(1485, 685)  # W S
                generalact.moveclick_1s(1357, 685)  # W SS
                # generalact.moveclick_1s(480, 485)  # T1
                generalact.moveclick_1s(388, 625)  # T2
                generalact.moveclick_1s(1500, 1005)
                generalact.moveclick_1s(1077, 795)
                generalact.moveclick_1s(1077, 795)
                generalact.moveclick_3s(1115, 933)  # START
                generalact.moveclick_1s(122, 144)
        else:
            generalact.ImgFor3Cdelay1('LO\\PC\\picture\\region_5.bmp', 0.9, 0, 0, 1920, 1080)
            if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\region_5_58ex.bmp', 0.8, 0, 0, 1920, 1080):
                if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\zizhuzhandou.bmp', 0.8, 0, 0, 1920, 1080):
                    generalact.moveclick_1s(1485, 412)  # C S
                    generalact.moveclick_1s(1357, 412)  # C SS
                    generalact.moveclick_1s(1485, 685)  # W S
                    generalact.moveclick_1s(1357, 685)  # W SS
                    # generalact.moveclick_1s(480, 485)  # T1
                    generalact.moveclick_1s(388, 625)  # T2
                    generalact.moveclick_1s(1500, 1005)
                    generalact.moveclick_1s(1077, 795)
                    generalact.moveclick_1s(1077, 795)
                    generalact.moveclick_3s(1115, 933)  # START
                    generalact.moveclick_1s(122, 144)


def back_world():
    if generalact.ImgReturn1For3('LO\\PC\\picture\\biangengfuguan.bmp', 0.8, 0, 0, 1920, 1080):
        generalact.moveclick_1s(1850, 70)
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\world.bmp', 0.8, 0, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\world_bat.bmp', 0.8, 0, 0, 1920, 1080)


def backtomainui():
    while 1:
        if generalact.ImgReturn1For5('LO\\PC\\picture\\world.bmp', 0.8, 0, 0, 1920, 1080):
            break
        else:
            generalact.rangeclick05(2, 52, 63)
            generalact.moveclick_1s(1820, 170)
        generalact.ImgFor3Cdelay1('LO\\PC\\picture\\expedition_com3.bmp', 0.8, 0, 0, 1920, 1080)


def back1():
    generalact.moveclick_1s(103, 139)


def back2():
    generalact.moveclick_2s(103, 139)


def back3():
    generalact.moveclick_3s(103, 139)


def backdown1():
    generalact.moveclick_1s(64, 1050)


def backdown2():
    generalact.moveclick_2s(64, 1050)


def backdown3():
    generalact.moveclick_3s(64, 1050)


def clickblock():
    generalact.rangeclick02(5, 1570, 1060)


def test():
    while 1:
        if generalact.ImgFor3Cdelay1('LO\\PC\\picture\\base_resource.bmp', 0.8, 0, 0, 1920, 1080):
            time.sleep(1)
            generalact.ImgFor3Cdelay1('LO\\PC\\picture\\base_continue.bmp', 0.8, 0, 0, 1920, 1080)
            time.sleep(3)
        else:
            break
    pass

