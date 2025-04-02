import os
import subprocess
import threading

import keyboard
import psutil
import pyautogui
import time
import pyautogui as CSauto
import win32api
import win32con
import win32gui
import win32print
import datetime
import random
from threading import Timer

import pywintypes
import logging
from logging import handlers


devmode = pywintypes.DEVMODEType()

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]

MUMUpath = 'C:\\Software\\MuMuPlayer-12.0\\shell\\MuMuPlayer.exe'
gl_timeflagtemporary = 0
gl_timeflag = 0
gl_timeflag1 = 99
gl_timeflag2 = 99


def logger_config(log_path, logging_name):
    """
    配置log
    :param log_path: 输出log路径
    :param logging_name: 记录中name，可随意
    :return:
    """
    '''
    logger是日志对象，handler是流处理器，console是控制台输出（没有console也可以，将不会在控制台输出，会在日志文件中输出）
    '''
    # 获取logger对象,取名
    loggers = logging.getLogger(logging_name)
    # 输出DEBUG及以上级别的信息，针对所有输出的第一层过滤
    loggers.setLevel(level=logging.INFO)
    # 获取文件日志句柄并设置日志级别，第二层过滤
    handler = logging.FileHandler(log_path, encoding='UTF-8')
    handler.setLevel(logging.INFO)
    # 往文件里写入#指定间隔时间自动生成文件的处理器
    handler = logging.handlers.RotatingFileHandler(log_path, maxBytes=1024000, backupCount=2, encoding='UTF-8', )
    # 生成并设置文件日志格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    # console相当于控制台输出，handler文件输出。获取流句柄并设置日志级别，第二层过滤
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # 为logger对象添加句柄
    loggers.addHandler(handler)
    loggers.addHandler(console)
    return loggers


logger = logger_config(log_path='log.txt', logging_name='LOG')


def imgcorrdinatefunenterreturn(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    a = 1
    while a:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            return 1, imgcoordinate
        a += 1
        if a == 6:
            return 0, imgcoordinate


def imgcorrdinatefunenterreturnP(imgname, confidence, x1, y1, x2, y2):
    print(imgname)
    a = 1
    while a:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            return 1, imgcoordinate
        a += 1
        if a == 6:
            return 0, imgcoordinate


def imgcorrdinatefun(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            CSauto.click(imgcoordinate)
            time.sleep(1)
            break


def imgcorrdinatefun2(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            CSauto.click(imgcoordinate)
            time.sleep(2)
            break


def imgcorrdinatefunde1(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            time.sleep(1)
            CSauto.click(imgcoordinate)
            time.sleep(1)
            break


def imgcorrdinatefunde2(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            time.sleep(2)
            CSauto.click(imgcoordinate)
            time.sleep(1)
            break


def imgcorrdinatefunde1b2(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            time.sleep(1)
            CSauto.click(imgcoordinate)
            time.sleep(2)
            break


def imgcorrdinatefunshiftde1(imgname, confidence, x1, y1, x2, y2, xshift, yshift):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            time.sleep(1)
            x, y = imgcoordinate
            moveclick_1s(x + xshift, y + yshift)
            time.sleep(1)
            break


def imgcorrdinatefun3(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    for i in range(3):
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            CSauto.click(imgcoordinate)
            time.sleep(1)
            return 1
    return 0


def imgcorrdinatefun3P(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    for i in range(3):
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            CSauto.click(imgcoordinate)
            time.sleep(1)
            return 1
    return 0


def imgcorrdinatefunclickcount3(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    count = 0
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            CSauto.click(imgcoordinate)
            time.sleep(1)
            return 1
        else:
            count += 1
            if count == 3:
                break
    return 0


def confirm_cilck3(imgstr, x, y):
    while 1:
        if imgcorrdinatefunclickcount3(imgstr, 0.9, 0, 0, 1920, 1080):
            time.sleep(1)
            break
        else:
            moveclick_1s(x, y)


def imgcorrdinatefunshiftclickcount3(imgname, confidence, x1, y1, x2, y2, shiftx, shifty):
    logger.info(imgname)
    count = 0
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            x, y = imgcoordinate.x+shiftx, imgcoordinate.y+shifty
            CSauto.click(x, y)
            time.sleep(1)
            return 1
        else:
            count += 1
            if count == 3:
                break
    return 0


def imgcorrdinatefunshiftclickcount3P(imgname, confidence, x1, y1, x2, y2, shiftx, shifty):
    count = 0
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            x, y = imgcoordinate.x+shiftx, imgcoordinate.y+shifty
            CSauto.click(x, y)
            time.sleep(1)
            return 1
        else:
            count += 1
            if count == 3:
                break
    return 0


def imgcorrdinatefuncount1(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            return 1
        else:
            break
    return 0


def imgcorrdinatefuncount3(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    count = 0
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            return 1
        else:
            count += 1
            if count == 3:
                break
    return 0


def confirm_nocilck3(imgstr, x, y):
    while 1:
        if imgcorrdinatefuncount3(imgstr, 0.9, 0, 0, 1920, 1080):
            time.sleep(1)
            break
        else:
            moveclick_1s(x, y)


def imgcorrdinatefuncount3P(imgname, confidence, x1, y1, x2, y2):
    print(imgname)
    count = 0
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            return 1
        else:
            count += 1
            if count == 3:
                break
    return 0


def imgcorrdinatefuncount(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    count = 0
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            return 1
        else:
            count += 1
            if count == 10:
                break
    return 0


def imgcorrdinatefuncountreturn(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    count = 0
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            return 1, imgcoordinate
        else:
            count += 1
            if count == 10:
                break
    return 0, imgcoordinate


def imgcorrdinatefunshift(imgname, confidence, x1, y1, x2, y2, xshift, yshift):
    logger.info(imgname)
    a = 1
    imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
    if imgcoordinate is not None:
        x, y = imgcoordinate
        moveclick_1s(x + xshift, y + yshift)
        time.sleep(1)
        return a


def imgcorrdinatefunwhile(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            time.sleep(1)
            return 0


def imgcorrdinatefunwhilenotime(imgname, confidence, x1, y1, x2, y2):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            break


def imgcorrdinatefunmoveclick(imgname, confidence, x1, y1, x2, y2, x, y):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            time.sleep(1)
            # CSauto.click(imgcoordinate)
            break
        else:
            moveclick_1s(x, y)


def imgcorrdinatefunmovenoclick(imgname, confidence, x1, y1, x2, y2, x, y):
    logger.info(imgname)
    while 1:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            time.sleep(1)
            break
        else:
            moveclick_1s(x, y)


def imgcorrdinatefunenter(imgname, confidence, x1, y1, x2, y2, xp, yp):
    logger.info(imgname)
    a = 1
    while a:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            CSauto.click(imgcoordinate.x + xp, imgcoordinate.y + yp)
            time.sleep(1)
            a = 0


def imgcorrdinatefunenterP(imgname, confidence, x1, y1, x2, y2, xp, yp):
    print(imgname)
    a = 1
    while a:
        imgcoordinate = CSauto.locateCenterOnScreen(imgname, confidence=confidence, region=(x1, y1, x2, y2))
        if imgcoordinate is not None:
            CSauto.click(imgcoordinate.x + xp, imgcoordinate.y + yp)
            time.sleep(1)
            a = 0


def fixedtime(settime1, flag):
    fixtime = datetime.datetime.now().strftime('%H:%M')
    logger.info(settime1)
    if flag == -1:
        settimeGflag0_tem()
    if flag == 0:
        settimeGflag0()
    if flag == 1:
        settimeGflag0_1()
    if flag == 2:
        settimeGflag0_2()
    t = Timer(60, fixedtime, (settime1, flag, ))
    t.start()
    if fixtime == settime1:
        # print('TimeNow:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        # print("aaaaaaaaaaaaaaaaaaaaa")
        t.cancel()
        if flag == -1:
            settimeGflag1_tem()
        if flag == 0:
            settimeGflag1()
        if flag == 1:
            settimeGflag1_1()
        if flag == 2:
            settimeGflag1_2()


class fixedtimeThreadAMgener(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True
        self.usedtime = "1"
        self.timeflag = -2
        # self.fixtimeflag = -1

    def setParameters(self, setusedtime, settimeflag, ):
        self.usedtime = setusedtime
        print(self.usedtime)
        self.timeflag = settimeflag
        print(self.timeflag)

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            fixedtime(self.usedtime, self.timeflag)
            # fixedtime('20:56', 0)
            time.sleep(3)
            self.stop()


def downdelay_1s():
    CSauto.press('down', interval=0.1)
    time.sleep(1)


def downdelay_2s():
    CSauto.press('down', interval=0.1)
    time.sleep(2)


def downdelay_3s():
    CSauto.press('down', interval=0.1)
    time.sleep(3)


def enterdelay_1s():
    CSauto.press('enter', interval=0.1)
    time.sleep(1)


def enterdelay_2s():
    CSauto.press('enter', interval=0.1)
    time.sleep(2)


def enterdelay_3s():
    CSauto.press('enter', interval=0.1)
    time.sleep(3)


def escdelay_1s():
    CSauto.press('esc', interval=0.1)
    time.sleep(1)


def escdelay_2s():
    CSauto.press('esc', interval=0.1)
    time.sleep(2)


def escdelay_3s():
    CSauto.press('esc', interval=0.1)
    time.sleep(3)


def dragmouse_count(x1, y1, x2, y2, n):
    for i in range(n):
        pyautogui.moveTo(x1, y1)
        pyautogui.dragTo(x2, y2, 1, button='left')
        time.sleep(1)


def dragmouse(x1, y1, x2, y2):
    pyautogui.moveTo(x1, y1)
    pyautogui.dragTo(x2, y2, 1, button='left')
    time.sleep(1)


def movemouse(x1, y1):
    pyautogui.moveTo(x1, y1)
    pyautogui.moveTo(x1, y1)
    time.sleep(1)


def moveclick_01s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(0.1)


def moveclick_02s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(0.2)


def moveclick_05s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(0.5)


def moveclick_1s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(1)


def moveclick_2s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(2)


def moveclick_3s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(3)


def moveclick_4s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(4)


def moveclick_5s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(5)


def moveclick_6s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(6)


def moveclick_7s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(7)


def moveclick_8s(x, y):
    CSauto.moveTo(x + randomnumber5(), y + randomnumber5())
    CSauto.click()
    time.sleep(8)


def click_01s():
    CSauto.click()
    time.sleep(0.1)


def click_02s():
    CSauto.click()
    time.sleep(0.2)


def click_05s():
    CSauto.click()
    time.sleep(0.5)


def click_1s():
    CSauto.click()
    time.sleep(1)


def click_2s():
    CSauto.click()
    time.sleep(2)


def click_3s():
    CSauto.click()
    time.sleep(3)


def click_4s():
    CSauto.click()
    time.sleep(4)


def click_5s():
    CSauto.click()
    time.sleep(5)


def click_6s():
    CSauto.click()
    time.sleep(6)


def click_7s():
    CSauto.click()
    time.sleep(7)


def click_8s():
    CSauto.click()
    time.sleep(8)


def rangeclick001(n, x, y):
    for i in range(1):
        moveclick_01s(x + randomnumber5(), y + randomnumber5())
    for i in range(n):
        pyautogui.click()


def rangeclick01(n, x, y):
    for i in range(n):
        moveclick_01s(x + randomnumber5(), y + randomnumber5())


def rangeclick02(n, x, y):
    for i in range(n):
        moveclick_02s(x + randomnumber5(), y + randomnumber5())


def rangeclick05(n, x, y):
    for i in range(n):
        moveclick_05s(x + randomnumber5(), y + randomnumber5())


def rangeclick1(n, x, y):
    for i in range(n):
        moveclick_1s(x + randomnumber5(), y + randomnumber5())


def rangeclick2(n, x, y):
    for i in range(n):
        moveclick_2s(x + randomnumber5(), y + randomnumber5())


def rangeclick3(n, x, y):
    for i in range(n):
        moveclick_3s(x + randomnumber5(), y + randomnumber5())


def randomnumber5():
    return random.randint(1, 5)
    # logger.info(random_int)


def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def set_used_resolution():
    # screenSize = (1280, 800)
    # screenSize = (1600, 1024)
    UseScreenSize = (1920, 1080)
    CurScreenSize = get_real_resolution()
    # UseScreenSize = (1600, 1024)
    if CurScreenSize == UseScreenSize:
        logger.info('CurScreenSize')
        logger.info(CurScreenSize)
        logger.info('UseScreenSize')
        logger.info(UseScreenSize)
    else:
        devmode.PelsWidth = UseScreenSize[0]
        devmode.PelsHeight = UseScreenSize[1]
        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
        win32api.ChangeDisplaySettings(devmode, 0)


def set_aft_resolution(UseScreenSize):
    devmode.PelsWidth = UseScreenSize[0]
    devmode.PelsHeight = UseScreenSize[1]
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
    win32api.ChangeDisplaySettings(devmode, 0)


def firstDayOfMonth():
    """判断今天是不是这个月第一天"""
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 1)).day
    # print(now.day)
    # return 1
    return now_day == now.day


def firstDayOfMonth2():
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 2)).day
    return now_day == now.day


def firstDayOfMonth3():
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 3)).day
    return now_day == now.day


def firstDayOfMonth5():
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 5)).day
    return now_day == now.day


def firstDayOfMonth7():
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 7)).day
    return now_day == now.day


def firstDayOfMonth8():
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 8)).day
    return now_day == now.day


def firstDayOfMonth15():
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 15)).day
    return now_day == now.day


def firstDayOfMonth25():
    now = datetime.date.today()
    now_day = (now + datetime.timedelta(days=-now.day + 25)).day
    return now_day == now.day


def firstDayOfWeek():
    """判断今天是不是这个周第1天"""
    now = datetime.datetime.now()
    dataflag = now.weekday()
    return dataflag == 0


def firstDayOfWeek2():
    """判断今天是不是这个周第2天"""
    now = datetime.datetime.now()
    dataflag = now.weekday()
    return dataflag == 1


def firstDayOfWeek3():
    """判断今天是不是这个周第3天"""
    now = datetime.datetime.now()
    dataflag = now.weekday()
    return dataflag == 2


def firstDayOfWeek4():
    """判断今天是不是这个周第4天"""
    now = datetime.datetime.now()
    dataflag = now.weekday()
    return dataflag == 3


def firstDayOfWeek5():
    """判断今天是不是这个周第5天"""
    now = datetime.datetime.now()
    dataflag = now.weekday()
    return dataflag == 4


def firstDayOfWeek6():
    """判断今天是不是这个周第6天"""
    now = datetime.datetime.now()
    dataflag = now.weekday()
    return dataflag == 5


def firstDayOfWeek7():
    """判断今天是不是这个周第7天"""
    now = datetime.datetime.now()
    dataflag = now.weekday()
    return dataflag == 6


def settimeGflag0_tem():
    global gl_timeflagtemporary
    gl_timeflagtemporary = 0


def settimeGflag1_tem():
    global gl_timeflagtemporary
    gl_timeflagtemporary = 1


def settimeGflag0():
    global gl_timeflag
    gl_timeflag = 0


def settimeGflag1():
    global gl_timeflag
    gl_timeflag = 1


def settimeGflag0_1():
    global gl_timeflag1
    gl_timeflag1 = 0


def settimeGflag1_1():
    global gl_timeflag1
    gl_timeflag1 = 1


def settimeGflag0_2():
    global gl_timeflag2
    gl_timeflag2 = 0


def settimeGflag1_2():
    global gl_timeflag2
    gl_timeflag2 = 1


def MUMUmain():
    time.sleep(1)
    moveclick_3s(90, 22)


def MUMUclose():
    movemouse(1898, 19)
    click_02s()


def MUMUclose1():
    time.sleep(1)
    movemouse(417, 21)
    click_02s()


def MUMUclose2():
    time.sleep(1)
    movemouse(632, 22)
    click_02s()


def MUMUdrag2():
    for i in range(2):
        dragmouse(1770, 600, 200, 600)
    time.sleep(1)


def startupMUMU(sleeptime):
    time.sleep(1)
    # generalact.moveclick_1s(1895, 8)
    start_exe(MUMUpath)
    time.sleep(sleeptime)
    imgcorrdinatefun3('MUMU\\close.bmp', 0.8, 1300, 100, 1920, 1080)
    for i in range(2):
        dragmouse(1770, 600, 200, 600)
    rangeclick01(4, 1845, 65)


def start_exe(filepath):
    # 定义exe文件路径和名称
    exe_path = filepath

    # 执行exe文件
    subprocess.Popen(exe_path)


def startup_time(path, sleeptime):
    time.sleep(1)
    # generalact.moveclick_1s(1895, 8)
    start_exe(path)
    time.sleep(sleeptime)


def escpyautoguifun():
    class escprogram(threading.Thread):
        def __init__(self):
            super().__init__()
            self.running = True

        def stop(self):
            self.running = False

        def run(self):
            keyboard.on_press(on_key)  # 监听键盘事件

    def on_key(event):
        # print('按键：', event.name)
        if event.name == 'f12':
            keyboard.unhook_all()
            # escprogramthread.stop()
            movemouse(0, 0)

    escprogramthread = escprogram()
    escprogramthread.daemon = True
    escprogramthread.start()


def AMorPM():
    now_time = time.strftime("%H:%M:%S", time.localtime())  # 现在的时间
    print("现在是北京时间：{}".format(now_time))
    # 判断时间
    if "07:40:00" < now_time < "18:00:00":
        return 0
    if "18:00:00" < now_time < "24:00:00":
        return 1
    if "00:00:00" < now_time < "07:00:00":
        return 1


def regularshutdown(minute):
    shutdowntime = minute*60
    os.system(f'shutdown -s -f -t {shutdowntime}')


def cancelregularshutdown():
    os.system('shutdown -a')


def killprocess(target_process_name):
    processes = psutil.process_iter()
    for process in processes:
        print(process.name())
        if process.name() == target_process_name:
            target_process = process
            target_process.terminate()
            break

