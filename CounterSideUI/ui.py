# import general_actions as generalact
# from Galactic_realm import GalacticRealmFun
# from NIKKE import nikkefun
# from RE1999 import RE1999Fun
import threading
import time

from CounterSide import CounterSideFun
# from wuqimitu import wuqimituFun
import general_actions as generalact
import yaml
import sys
# import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from win_CounterSide import Ui_MainWindow
# from win_CounterSideSetup import Ui_CSSetUp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.CSS = None

    def FilePath(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self.ui.ChoiceButtonMain,  # 父窗口对象
            "选择程序",  # 标题

            r"E:",  # 起始目录
            "程序类型 (*.exe)"  # 选择类型过滤项，过滤内容在括号中
        )
        self.ui.lineEdit.setText(filePath)
        print(filePath)

    def CSstart(self):
        Cur_Res = generalact.get_real_resolution()
        generalact.set_used_resolution()
        with open('CounterSide.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        monizuozhanflag = result['monizuozhan']
        bugeizuozhanflag = result['bugeizuozhan']
        collectflag = result['collect']
        shopflash = 0
        shengkaiflag = 0
        # subprocess.Popen(result['filepath'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # 使用管道
        if result['explore']:
            self.ui.checkBox.setChecked(False)
            time.sleep(1)
            CounterSideFun.completeup()
        else:
            if result['guild']:
                CounterSideFun.guild()
            if result['fire']:
                CounterSideFun.reclaim()
            if bugeizuozhanflag[1]:
                bugeizuozhanflag1_5 = 1
            else:
                bugeizuozhanflag1_5 = 0
            if bugeizuozhanflag[2]:
                bugeizuozhanflag1_6 = 1
            else:
                bugeizuozhanflag1_6 = 0
            if bugeizuozhanflag[3]:
                bugeizuozhanflag1_7 = 1
            else:
                bugeizuozhanflag1_7 = 0
            if bugeizuozhanflag[4]:
                bugeizuozhanflag1_8 = 1
            else:
                bugeizuozhanflag1_8 = 0
            if bugeizuozhanflag1_5 == 0 and bugeizuozhanflag1_6 == 0 \
                    and bugeizuozhanflag1_7 == 0 and bugeizuozhanflag1_8 == 0:
                bugeizuozhanflag = 0
            else:
                bugeizuozhanflag = 1

            if monizuozhanflag[1]:
                monizhanflaggongji = 1
            else:
                monizhanflaggongji = 0
            if monizuozhanflag[2]:
                monizhanflagfangyu = 1
            else:
                monizhanflagfangyu = 0
            if monizuozhanflag[3]:
                monizhanflagfangkong = 1
            else:
                monizhanflagfangkong = 0
            if monizhanflaggongji == 0 and monizhanflagfangyu == 0 and monizhanflagfangkong == 0:
                monizhanflag = 0
            else:
                monizhanflag = 1

            if collectflag[1]:
                shoucangflag1 = 1
            else:
                shoucangflag1 = 0
            if collectflag[2]:
                shoucangflag2 = 1
            else:
                shoucangflag2 = 0
            if collectflag[3]:
                shoucangflag3 = 1
            else:
                shoucangflag3 = 0
            if collectflag[4]:
                shoucangflag4 = 1
            else:
                shoucangflag4 = 0
            if collectflag[5]:
                shoucangflag5 = 1
            else:
                shoucangflag5 = 0
            if collectflag[6]:
                shoucangflag6 = 1
            else:
                shoucangflag6 = 0
            if shoucangflag1 == 0 and shoucangflag2 == 0 and shoucangflag3 == 0 \
                    and shoucangflag4 == 0 and shoucangflag5 == 0 and shoucangflag6 == 0:
                shoucangflag = 0
            else:
                shoucangflag = 1
            if result['anyingdiantang']:
                anyingdiantang = 1
            else:
                anyingdiantang = 0
            CounterSideFun.fight(bugeizuozhanflag, bugeizuozhanflag1_8, bugeizuozhanflag1_7,
                                 bugeizuozhanflag1_6, bugeizuozhanflag1_5,
                                 monizhanflag, monizhanflaggongji, monizhanflagfangyu, monizhanflagfangkong,
                                 anyingdiantang,
                                 shoucangflag, shoucangflag1, shoucangflag2, shoucangflag3, shoucangflag4,
                                 shoucangflag5,
                                 shoucangflag6)
            if result['shopflash'] == 0:
                shopflash = 0
            if result['shopflash'] == 5:
                shopflash = 5
            CounterSideFun.shop(shopflash)
            if result['shopMW']:
                CounterSideFun.shopMW()
            if result['company']:
                CounterSideFun.firm()
            if result['shengkai'] == 0:
                shengkaiflag = 0

            if result['shengkai'] == 3:
                shengkaiflag = 3
            if result['shengkai'] == 6:
                shengkaiflag = 6
            if result['shengkai'] == 9:
                shengkaiflag = 9
            CounterSideFun.shengkai(shengkaiflag)
            if result['employee']:
                CounterSideFun.employee()
        f.close()
        generalact.set_aft_resolution(Cur_Res)

    def Startup(self):
        CSstartThreat = threading.Thread(target=self.CSstart, )
        CSstartThreat.Daemon = True
        CSstartThreat.start()

    def SaveDate(self):
        shopflashflag = 0
        shengkaiflag = 0
        filePath = self.ui.lineEdit.text()

        exploreflag = self.ui.checkBox.isChecked()
        guildflag = self.ui.checkBoxguild.isChecked()
        fireflag = self.ui.checkBoxfire.isChecked()

        bugeizuozhanflag1_5 = self.ui.checkBoxbugeizuozhan15.isChecked()
        bugeizuozhanflag1_6 = self.ui.checkBoxbugeizuozhan16.isChecked()
        bugeizuozhanflag1_7 = self.ui.checkBoxbugeizuozhan17.isChecked()
        bugeizuozhanflag1_8 = self.ui.checkBoxbugeizuozhan18.isChecked()
        if bugeizuozhanflag1_5 is False and bugeizuozhanflag1_6 is False \
                and bugeizuozhanflag1_7 is False and bugeizuozhanflag1_8 is False:
            bugeizuozhanflag = False
        else:
            bugeizuozhanflag = True
        monizhanflaggongji = self.ui.checkBoxmonizhangongji.isChecked()
        monizhanflagfangyu = self.ui.checkBoxmonizhanfangyu.isChecked()
        monizhanflagfangkong = self.ui.checkBoxmonizhanfangkong.isChecked()
        if monizhanflaggongji is False and monizhanflagfangyu is False and monizhanflagfangkong is False:
            monizhanflag = False
        else:
            monizhanflag = True
        shoucangflag1 = self.ui.checkBoxcollect1.isChecked()
        shoucangflag2 = self.ui.checkBoxcollect2.isChecked()
        shoucangflag3 = self.ui.checkBoxcollect3.isChecked()
        shoucangflag4 = self.ui.checkBoxcollect4.isChecked()
        shoucangflag5 = self.ui.checkBoxcollect5.isChecked()
        shoucangflag6 = self.ui.checkBoxcollect6.isChecked()
        if shoucangflag1 is False and shoucangflag2 is False and shoucangflag3 is False \
                and shoucangflag4 is False and shoucangflag5 is False and shoucangflag6 is False:
            shoucangflag = False
        else:
            shoucangflag = True
        anyingdiantangflag = self.ui.checkBoxanyingdiantang.isChecked()

        if self.ui.radioButtonshopflash0.isChecked():
            shopflashflag = 0
        if self.ui.radioButtonshopflash5.isChecked():
            shopflashflag = 5
        shopMWflag = self.ui.checkBoxMW.isChecked()
        companyflag = self.ui.checkBoxcompany.isChecked()
        if self.ui.radioButtonshengkai0.isChecked():
            shengkaiflag = 0
        if self.ui.radioButtonshengkai3.isChecked():
            shengkaiflag = 3
        if self.ui.radioButtonshengkai6.isChecked():
            shengkaiflag = 6
        if self.ui.radioButtonshengkai9.isChecked():
            shengkaiflag = 9
        employeeflag = self.ui.checkBoxemploy.isChecked()

        apiData = {
            "guild": guildflag,
            "fire": fireflag,
            "company": companyflag,
            "employee": employeeflag,
            "anyingdiantang": anyingdiantangflag,
            "explore": exploreflag,
            "shengkai": shengkaiflag,
            "shopflash": shopflashflag,
            "shopMW": shopMWflag,
            "monizuozhan": [monizhanflag, monizhanflaggongji, monizhanflagfangyu, monizhanflagfangkong],
            "bugeizuozhan": [bugeizuozhanflag, bugeizuozhanflag1_5, bugeizuozhanflag1_6,
                             bugeizuozhanflag1_7, bugeizuozhanflag1_8],
            "collect": [shoucangflag, shoucangflag1, shoucangflag2, shoucangflag3, shoucangflag4,
                        shoucangflag5, shoucangflag6],
            "filepath": filePath,

        }

        with open('CounterSide.yaml', 'w', encoding='utf-8') as f:
            data = yaml.dump(apiData, f)
        f.close()

    def rbtnClicked(self, state):
        # print("选中项的id为：", self.checkBoxcollect1.)  # 选中选在 选项组中的id。
        # print(state == Qt.CheckState.Checked.value)
        print(state)
        self.SaveDate()

    def win_init(self):
        with open('CounterSide.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
        self.ui.checkBox.setChecked(result['explore'])
        self.ui.checkBoxguild.setChecked(result['guild'])
        self.ui.checkBoxcompany.setChecked(result['company'])
        self.ui.checkBoxfire.setChecked(result['fire'])
        self.ui.checkBoxemploy.setChecked(result['employee'])
        self.ui.checkBoxanyingdiantang.setChecked(result['anyingdiantang'])
        self.ui.radioButtonshengkai0.setChecked(result['shengkai'])
        match (result['shengkai']):
            case (0):
                self.ui.radioButtonshengkai0.setChecked(True)
            case (3):
                self.ui.radioButtonshengkai3.setChecked(True)
            case (6):
                self.ui.radioButtonshengkai6.setChecked(True)
            case (9):
                self.ui.radioButtonshengkai9.setChecked(True)
            case _:
                print('Case 4, I match anything!')
        match (result['shopflash']):
            case (0):
                self.ui.radioButtonshopflash0.setChecked(True)
            case (5):
                self.ui.radioButtonshopflash5.setChecked(True)
            case _:
                print('Case 4, I match anything!')
        self.ui.checkBoxMW.setChecked(result['shopMW'])
        monizuozhanflag = result['monizuozhan']
        self.ui.checkBoxmonizhangongji.setChecked(monizuozhanflag[1])
        self.ui.checkBoxmonizhanfangyu.setChecked(monizuozhanflag[2])
        self.ui.checkBoxmonizhanfangkong.setChecked(monizuozhanflag[3])
        bugeizuozhanflag = result['bugeizuozhan']
        self.ui.checkBoxbugeizuozhan15.setChecked(bugeizuozhanflag[1])
        self.ui.checkBoxbugeizuozhan16.setChecked(bugeizuozhanflag[2])
        self.ui.checkBoxbugeizuozhan17.setChecked(bugeizuozhanflag[3])
        self.ui.checkBoxbugeizuozhan18.setChecked(bugeizuozhanflag[4])
        collectflag = result['collect']
        self.ui.checkBoxcollect1.setChecked(collectflag[1])
        self.ui.checkBoxcollect2.setChecked(collectflag[2])
        self.ui.checkBoxcollect3.setChecked(collectflag[3])
        self.ui.checkBoxcollect4.setChecked(collectflag[4])
        self.ui.checkBoxcollect5.setChecked(collectflag[5])
        self.ui.checkBoxcollect6.setChecked(collectflag[6])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.setWindowTitle("CounterSide")
    window.show()
    window.win_init()
    generalact.escpyautoguifun()
    sys.exit(app.exec())

