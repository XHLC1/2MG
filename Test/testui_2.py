# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testui_2.ui'
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

class Ui_testui_2(object):
    def setupUi(self, testui_2):
        if not testui_2.objectName():
            testui_2.setObjectName(u"testui_2")
        testui_2.resize(400, 300)
        self.buttonBox = QDialogButtonBox(testui_2)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(testui_2)
        # self.buttonBox.accepted.connect(testui_2.accept)
        # self.buttonBox.rejected.connect(testui_2.reject)

        QMetaObject.connectSlotsByName(testui_2)
    # setupUi

    def retranslateUi(self, testui_2):
        testui_2.setWindowTitle(QCoreApplication.translate("testui_2", u"Dialog", None))
    # retranslateUi

