# -*- coding: utf-8 -*-

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

class Ui_NIKKE(object):
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
        self.buttonBox.accepted.connect(NIKKE.accept)
        self.buttonBox.rejected.connect(NIKKE.reject)

        QMetaObject.connectSlotsByName(NIKKE)
    # setupUi

    def retranslateUi(self, NIKKE):
        NIKKE.setWindowTitle(QCoreApplication.translate("NIKKE", u"Dialog", None))
    # retranslateUi

