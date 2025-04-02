# -*- coding: utf-8 -*-
from PySide6 import QtWidgets
################################################################################
## Form generated from reading UI file 'testui_1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QWidget)

from Test.testui_2 import Ui_testui_2


class Ui_testui_1(QWidget):
    def setupUi(self, testui_1):
        if not testui_1.objectName():
            testui_1.setObjectName(u"testui_1")
        testui_1.resize(400, 300)
        self.buttonBox = QDialogButtonBox(testui_1)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(testui_1)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(testui_1)
    # setupUi

    def accept(self):
        print(1)
        login_info = Ui_testui_2()
        self.window = QWidget()
        login_info.setupUi(self.window)
        self.window.show()
        login_form.hide()

    def reject(self):
        pass

    def retranslateUi(self, testui_1):
        testui_1.setWindowTitle(QCoreApplication.translate("testui_1", u"Dialog", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_form = QtWidgets.QWidget()
    ui = Ui_testui_1()
    ui.setupUi(login_form)
    login_form.show()
    sys.exit(app.exec())
