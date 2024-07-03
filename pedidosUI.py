# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pedidos.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form_Pedidos(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(801, 518)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 151, 16))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 50, 781, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 761, 121))
        self.layoutAguardo = QVBoxLayout(self.verticalLayoutWidget_2)
        self.layoutAguardo.setObjectName(u"verticalLayout_2")
        self.layoutAguardo.setContentsMargins(0, 0, 0, 0)
        self.layoutAguardo.setAlignment(Qt.AlignTop)
        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 761, 121))
        self.layoutPreparo = QVBoxLayout(self.verticalLayoutWidget_3)
        self.layoutPreparo.setObjectName(u"verticalLayout_3")
        self.layoutPreparo.setContentsMargins(0, 0, 0, 0)
        self.layoutPreparo.setAlignment(Qt.AlignTop)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 20, 761, 121))
        self.layoutFinalizado = QVBoxLayout(self.verticalLayoutWidget_4)
        self.layoutFinalizado.setObjectName(u"verticalLayout_4")
        self.layoutFinalizado.setContentsMargins(0, 0, 0, 0)
        self.layoutFinalizado.setAlignment(Qt.AlignTop)
        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Pedidos", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Em Aguardo", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Em Preparo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Finalizado", None))
    # retranslateUi

