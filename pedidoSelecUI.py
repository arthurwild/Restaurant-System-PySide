# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedidoSelec.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form_PedidoSelec(object):
    def setupUi(self, Form_PedidoSelec):
        if not Form_PedidoSelec.objectName():
            Form_PedidoSelec.setObjectName(u"Form_PedidoSelec")
        Form_PedidoSelec.resize(587, 392)
        self.horizontalLayoutWidget = QWidget(Form_PedidoSelec)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(300, 0, 290, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(False)

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.verticalLayoutWidget = QWidget(Form_PedidoSelec)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 110, 561, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.retranslateUi(Form_PedidoSelec)

        QMetaObject.connectSlotsByName(Form_PedidoSelec)
    # setupUi

    def retranslateUi(self, Form_PedidoSelec):
        Form_PedidoSelec.setWindowTitle(QCoreApplication.translate("Form_PedidoSelec", u"Form", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form_PedidoSelec", u"Em Espera", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form_PedidoSelec", u"Em Preparo", None))
        self.radioButton.setText(QCoreApplication.translate("Form_PedidoSelec", u"Finalizado", None))
    # retranslateUi

