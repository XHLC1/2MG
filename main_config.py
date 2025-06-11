import win32gui
import win32print
import win32api
import win32con
import base64
import os
import sys
import threading
import keyboard
import pyautogui
import yaml
import datetime
import time
import pyautogui

import CWCX.CWCXFun
import CounterSideUI.CounterSide.CounterSideFun
import NIKKE.nikkefun
import RE1999.RE1999Fun
import general_actions as generalact
from CWCX import CWCXFun
from CounterSide import CounterSideFun
from NIKKE import nikkefun
from LHCX import LHCXfun
from RE1999 import RE1999Fun
from YTJH import YTJHfun
from wuqimitu import wuqimituFun
from YXHS import YXHSFun

sys.path.append(r"C:\\Code\\PythonCode\\withUI\\LO\\PC")
import LOPCFun

time.sleep(3)


def time_config(AFTD):
    if AFTD == 1:
        fixedtimethreadTEM = generalact.fixedtimeThreadAMgener()
        fixedtimethreadTEM.setParameters("03:40", -1)
        fixedtimethreadTEM.start()
        fixedtimethreadNIKKE = generalact.fixedtimeThreadAMgener()
        fixedtimethreadNIKKE.setParameters("07:20", 2)
        fixedtimethreadNIKKE.start()
        fixedtimethreadAM = generalact.fixedtimeThreadAMgener()
        fixedtimethreadAM.setParameters("06:10", 0)
        fixedtimethreadAM.start()
        fixedtimethreadAM1 = generalact.fixedtimeThreadAMgener()
        fixedtimethreadAM1.setParameters("07:00", 1)
        fixedtimethreadAM1.start()

    if AFTD == 0:
        fixedtimethreadPM = generalact.fixedtimeThreadAMgener()
        fixedtimethreadPM.setParameters("17:10", 0)
        # fixedtimethreadPM.setParameters("18:23", 0)
        fixedtimethreadPM.start()
        fixedtimethreadPM1 = generalact.fixedtimeThreadAMgener()
        fixedtimethreadPM1.setParameters("17:59", 1)
        # fixedtimethreadPM1.setParameters("18:25", 1)
        fixedtimethreadPM1.start()


LHCXFunhuodongflag = 0
RE1999huodongflag, RE1999resourceflag = 0, 3
wuqimituhuodongflag, wuqimitujiyifengbaoflag, wuqimituresourceflag = 0, 1, 4  # 1 金币 2 狂乱精粹 3 污染之巢 4 极域搜寻 7 3>10 帕尔玛废墟
YTJHhuodongflag, YTJHshopflag = 0, 2
CWCXFunhuodongflag, CWCXFunjinjie, CWCXFunbatflag = 0, 2, 2  # jinjie 2=赤噬 3=裂鳄     2 核心制作 3 队员特训
YXHShuodongflag, YXHShuodongflag_stage, YXHSresourceflag_stage, YXHSxinmaoflag_stage = 1, 1, 2, 2
# resourceflag 1 money 2 exp 3 心锚exp
# xinmaoflag 1 混合体 2 奇点列车 3洛伦佐 4 乐园梦魇 5 总控一号


def game_amup(AFTD):
    print('good morning')
    generalact.startupMUMU(60)
    generalact.settimeGflag0()

    RE1999Fun.dailytaskst(AFTD, RE1999huodongflag, RE1999resourceflag)
    wuqimituFun.dailytaskst(AFTD, wuqimituhuodongflag, wuqimituresourceflag, wuqimitujiyifengbaoflag)
    YXHSFun.dailytaskst(AFTD, YXHShuodongflag, YXHShuodongflag_stage, YXHSresourceflag_stage, YXHSxinmaoflag_stage)
    pyautogui.hotkey('alt', 'f4')
    generalact.startupMUMU(30)
    LHCXfun.dailytaskst(AFTD, LHCXFunhuodongflag)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(3)


def game_amdown(AFTD):
    print('hello world')
    generalact.settimeGflag0_1()
    generalact.startupMUMU(60)

    YTJHfun.dailytaskst(AFTD, YTJHhuodongflag, YTJHshopflag)
    CWCXFun.dailytaskst(AFTD, CWCXFunhuodongflag, CWCXFunjinjie, CWCXFunbatflag)


def game_pmup(AFTD):
    print('good morning')
    generalact.startupMUMU(60)
    generalact.settimeGflag0()

    RE1999Fun.dailytaskst(AFTD, RE1999huodongflag, RE1999resourceflag)
    wuqimituFun.dailytaskst(AFTD, wuqimituhuodongflag, wuqimituresourceflag, wuqimitujiyifengbaoflag)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(3)


def game_pmdown(AFTD):
    print('hello world')
    generalact.settimeGflag0_1()
    generalact.startupMUMU(60)

    YTJHfun.dailytaskst(AFTD, YTJHhuodongflag, YTJHshopflag)
    YXHSFun.dailytaskst(AFTD, YXHShuodongflag, YXHShuodongflag_stage, YXHSresourceflag_stage, YXHSxinmaoflag_stage)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(5)
    generalact.startupMUMU(60)
    CWCXFun.dailytaskst(AFTD, CWCXFunhuodongflag, CWCXFunjinjie, CWCXFunbatflag)
    LHCXfun.dailytaskst(AFTD, LHCXFunhuodongflag)


def startdailytast(timeflag, ):
    if timeflag == 0:
        nikkefun.dailytaskst(nikkefun.LJ_BOSS.克拉肯)

    AFTD = generalact.AMorPM()
    print("AFTD = ", AFTD)
    # AFTD = 0
    if timeflag != 0:
        time_config(AFTD)
        generalact.escpyautoguifun()
        CounterSideFun.completeup()
        while 1:
            if generalact.gl_timeflag == 1:
                CounterSideFun.backtomainui()
                CounterSideFun.shengkai(6)
                CounterSideFun.MUMUBACK1()
                pyautogui.hotkey('alt', 'f4')
                if AFTD:
                    game_amup(AFTD)
                else:
                    game_pmup(AFTD)
                break
        CounterSideFun.CSBACK()
        # pyautogui.hotkey('alt', 'tab')
        # generalact.startup_time('C:\\MobileGame\\YiJieShiWuSuo\\Launcher\\PDLauncher.exe', 10)
        CounterSideFun.completeup()
        CounterSideFun.MUMUBACK1()
        pyautogui.hotkey('alt', 'f4')
        while 1:
            if generalact.gl_timeflag1 == 1:
                if AFTD:
                    game_amdown(AFTD)
                    # pyautogui.hotkey('alt', 'f4')
                else:
                    game_pmdown(AFTD)
                    pyautogui.hotkey('alt', 'tab')
                break
        CounterSideFun.CSBACK()
        CounterSideFun.completeup()
        if AFTD == 1:
            while 1:
                if generalact.gl_timeflag2 == 1:
                    nikkefun.startwholegame()
                    nikkefun.dailytaskst(nikkefun.LJ_BOSS.克拉肯)
                    nikkefun.closegame()
                    generalact.settimeGflag0_1()
                    break
        CounterSideFun.CSBACK()
        CounterSideFun.completeup()


AFTD = 0
# nikkefun.ark(nikkefun.LJ_BOSS.克拉肯)
# LOPCFun.ZZZD_B(0)
# nikkefun.danrentuji()
# for i in range(1):
#     LHCXfun.CYSY(1, 1)
# time.sleep(3)
# game_amup(1)
# game_amdown(1)
# game_pmup(0)
# game_pmdown(0)
# nikkefun.startwholegame()
# nikkefun.dailytaskst(nikkefun.LJ_BOSS.克拉肯)
# nikkefun.closegame()
# while 1:
#     generalact.click_02s()
# for i in range(50):
#     generalact.moveclick_1s(1270, 777)
#     generalact.moveclick_1s(1180, 725)
#     generalact.moveclick_2s(955, 933)
#     generalact.rangeclick02(2, 1333, 990)



