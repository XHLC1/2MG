import threading
import time
import general_actions

import keyboard

from CounterSide import CounterSideFun


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
        if event.name == 'esc':
            # keyboard.unhook_all()
            escprogramthread.stop()
            general_actions.movemouse(0, 0)

    escprogramthread = escprogram()
    escprogramthread.start()


general_actions.escpyautoguifun()
CounterSideFun.completeup()

# while 1:
#     general_actions.moveclick_02s(800, 500)
