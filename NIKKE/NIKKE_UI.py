# -*- coding: utf-8 -*-
from PySide6 import QtWidgets
################################################################################
## Form generated from reading UI file 'NIKKE_mainui.ui'
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

from NIKKE import nikkefun


class Ui_NIKKE(QWidget):
    def setupUi(self, NIKKE):
        if not NIKKE.objectName():
            NIKKE.setObjectName(u"NIKKE")
        NIKKE.resize(400, 300)
        self.buttonBox = QDialogButtonBox(NIKKE)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(NIKKE)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        QMetaObject.connectSlotsByName(NIKKE)
    # setupUi

    def retranslateUi(self, NIKKE):
        NIKKE.setWindowTitle(QCoreApplication.translate("NIKKE", u"Dialog", None))
    # retranslateUi

    def accept(self):
        print(1)
        nikkefun.dailytaskst()

    def reject(self):
        nikkefun.scrapshop_xia3()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_form = QtWidgets.QWidget()
    ui = Ui_NIKKE()
    ui.setupUi(login_form)
    login_form.show()
    sys.exit(app.exec())
