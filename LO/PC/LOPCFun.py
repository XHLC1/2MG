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


def expedition():
    while 1:
        if generalact.imgcorrdinatefunshiftclickcount3('LO\\PC\\picture\\expedition_com1.bmp', 0.8, 0, 0, 1920, 1080, 0, -50):
            if generalact.imgcorrdinatefunclickcount3('LO\\PC\\picture\\expedition_com2.bmp', 0.8, 0, 0, 1920, 1080):
                generalact.imgcorrdinatefunclickcount3('LO\\PC\\picture\\expedition_com3.bmp', 0.8, 0, 0, 1920, 1080)
            else:
                generalact.imgcorrdinatefunshiftclickcount3('LO\\PC\\picture\\expedition_com1.bmp', 0.8, 0, 0, 1920, 1080, 0, -50)
                generalact.imgcorrdinatefunclickcount3('LO\\PC\\picture\\expedition_com2.bmp', 0.8, 0, 0, 1920, 1080)
                generalact.imgcorrdinatefunclickcount3('LO\\PC\\picture\\expedition_com3.bmp', 0.8, 0, 0, 1920, 1080)
        else:
            break


def back1():
    generalact.moveclick_1s(45, 55)


def back2():
    generalact.moveclick_2s(45, 55)


def back3():
    generalact.moveclick_3s(45, 55)


def backdown1():
    generalact.moveclick_1s(64, 1050)


def backdown2():
    generalact.moveclick_2s(64, 1050)


def backdown3():
    generalact.moveclick_3s(64, 1050)


def test():
    pass
    # pydirectinput.keyDown('enter')
