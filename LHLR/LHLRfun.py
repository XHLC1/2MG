import time
import general_actions as generalact
import pyautogui as CSauto

CSauto.FAILSAFE = True
CSauto.FAILSAFE_POINTS = [(0, 0)]

LHLRpath = 'C:\\Software\\MuMuPlayer-12.0\\shell\\MuMuPlayer.exe'

def dailytaskst(AFTD, huodongflag, resourceflag):
    entergamefun()


def entergamefun():
    generalact.logger.info('LHLRfun.entergamefun')
    generalact.start_exe(LHLRpath)



def backtomainui():
    generalact.logger.info('YXHSFun.backtomainui')
    n = 0
    while 1:
        if generalact.ImgReturn1For5('YXHS\\picture\\XHL.bmp', 0.8, 320, 145, 1371, 868):
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
        generalact.ImgFor3Cdelay1('YXHS\\picture\\close.bmp', 0.7, 990, 0, 1920, 1080)
        generalact.ImgFor3Cdelay1('YXHS\\picture\\update.bmp', 0.7, 990, 0, 1920, 1080)
        if generalact.ImgFor3Cdelay1('YXHS\\picture\\enter_tap.bmp', 0.8, 0, 0, 1920, 1080):
            time.sleep(5)
            generalact.rangeclick02(10, 1193, 540)
            time.sleep(5)
            generalact.rangeclick02(10, 880, 805)
