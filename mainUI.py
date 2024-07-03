# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(929, 706)
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setBaseSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 280, 820, 341))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cardapioButton = QPushButton(self.horizontalLayoutWidget)
        self.cardapioButton.setObjectName(u"cardapioButton")
        self.cardapioButton.setMinimumSize(QSize(200, 200))
        palette = QPalette()
        brush = QBrush(QColor(170, 170, 127, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.cardapioButton.setPalette(palette)

        self.horizontalLayout.addWidget(self.cardapioButton)

        self.atendenteButton = QPushButton(self.horizontalLayoutWidget)
        self.atendenteButton.setObjectName(u"atendenteButton")
        self.atendenteButton.setMinimumSize(QSize(200, 200))
        palette1 = QPalette()
        brush1 = QBrush(QColor(0, 85, 127, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        self.atendenteButton.setPalette(palette1)

        self.horizontalLayout.addWidget(self.atendenteButton)

        self.pedidosButton = QPushButton(self.horizontalLayoutWidget)
        self.pedidosButton.setObjectName(u"pedidosButton")
        self.pedidosButton.setMinimumSize(QSize(200, 200))
        palette2 = QPalette()
        brush2 = QBrush(QColor(85, 85, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        self.pedidosButton.setPalette(palette2)

        self.horizontalLayout.addWidget(self.pedidosButton)

        self.vendasButton = QPushButton(self.horizontalLayoutWidget)
        self.vendasButton.setObjectName(u"vendasButton")
        self.vendasButton.setMinimumSize(QSize(200, 200))
        palette3 = QPalette()
        brush3 = QBrush(QColor(170, 85, 127, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        self.vendasButton.setPalette(palette3)

        self.horizontalLayout.addWidget(self.vendasButton)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 40, 341, 91))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 180, 341, 91))
        font1 = QFont()
        font1.setPointSize(18)
        self.label_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cardapioButton.setText(QCoreApplication.translate("MainWindow", u"CARD\u00c1PIO", None))
        self.atendenteButton.setText(QCoreApplication.translate("MainWindow", u"ATENDENTE", None))
        self.pedidosButton.setText(QCoreApplication.translate("MainWindow", u"PEDIDOS", None))
        self.vendasButton.setText(QCoreApplication.translate("MainWindow", u"VENDAS DO DIA", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RESTAURANTE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SELECIONE O TIPO DE MENU", None))
    # retranslateUi

