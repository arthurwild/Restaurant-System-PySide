# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atendente.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpinBox, QTabWidget,
    QToolBox, QVBoxLayout, QWidget)

class Ui_Form_Atendente(object):
    def setupUi(self, Form_Atendente):
        if not Form_Atendente.objectName():
            Form_Atendente.setObjectName(u"Form_Atendente")
        Form_Atendente.resize(709, 516)
        self.tabWidget = QTabWidget(Form_Atendente)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 701, 511))
        self.cardapio = QWidget()
        self.cardapio.setObjectName(u"cardapio")
        self.toolBox = QToolBox(self.cardapio)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(0, 0, 701, 371))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 701, 251))
        self.formLayoutWidget = QWidget(self.page)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 371, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.fetuccineAlfredoLabel = QLabel(self.formLayoutWidget)
        self.fetuccineAlfredoLabel.setObjectName(u"fetuccineAlfredoLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.fetuccineAlfredoLabel)

        self.spinAlfredo = QSpinBox(self.formLayoutWidget)
        self.spinAlfredo.setObjectName(u"spinAlfredo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinAlfredo)

        self.spaghettiCarbonaraLabel = QLabel(self.formLayoutWidget)
        self.spaghettiCarbonaraLabel.setObjectName(u"spaghettiCarbonaraLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.spaghettiCarbonaraLabel)

        self.spinCarbo = QSpinBox(self.formLayoutWidget)
        self.spinCarbo.setObjectName(u"spinCarbo")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinCarbo)

        self.gnocciAlPestoLabel = QLabel(self.formLayoutWidget)
        self.gnocciAlPestoLabel.setObjectName(u"gnocciAlPestoLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.gnocciAlPestoLabel)

        self.spinPesto = QSpinBox(self.formLayoutWidget)
        self.spinPesto.setObjectName(u"spinPesto")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinPesto)

        self.macNCheeseKidsLabel = QLabel(self.formLayoutWidget)
        self.macNCheeseKidsLabel.setObjectName(u"macNCheeseKidsLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.macNCheeseKidsLabel)

        self.spinMac = QSpinBox(self.formLayoutWidget)
        self.spinMac.setObjectName(u"spinMac")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinMac)

        self.fusliBolonhesaLabel = QLabel(self.formLayoutWidget)
        self.fusliBolonhesaLabel.setObjectName(u"fusliBolonhesaLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.fusliBolonhesaLabel)

        self.spinFusli = QSpinBox(self.formLayoutWidget)
        self.spinFusli.setObjectName(u"spinFusli")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.spinFusli)

        self.toolBox.addItem(self.page, u"Lanches")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 701, 251))
        self.formLayoutWidget_2 = QWidget(self.page_2)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 10, 431, 181))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.refrigeranteLabel = QLabel(self.formLayoutWidget_2)
        self.refrigeranteLabel.setObjectName(u"refrigeranteLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.refrigeranteLabel)

        self.spinRefri = QSpinBox(self.formLayoutWidget_2)
        self.spinRefri.setObjectName(u"spinRefri")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinRefri)

        self.sucoNaturalLabel = QLabel(self.formLayoutWidget_2)
        self.sucoNaturalLabel.setObjectName(u"sucoNaturalLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.sucoNaturalLabel)

        self.spinSuco = QSpinBox(self.formLayoutWidget_2)
        self.spinSuco.setObjectName(u"spinSuco")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.spinSuco)

        self.guaLabel = QLabel(self.formLayoutWidget_2)
        self.guaLabel.setObjectName(u"guaLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.guaLabel)

        self.spinAgua = QSpinBox(self.formLayoutWidget_2)
        self.spinAgua.setObjectName(u"spinAgua")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spinAgua)

        self.toolBox.addItem(self.page_2, u"Bebidas")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 701, 251))
        self.formLayoutWidget_3 = QWidget(self.page_3)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(0, 0, 521, 201))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.saladaCapreseLabel = QLabel(self.formLayoutWidget_3)
        self.saladaCapreseLabel.setObjectName(u"saladaCapreseLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.saladaCapreseLabel)

        self.spinSalada = QSpinBox(self.formLayoutWidget_3)
        self.spinSalada.setObjectName(u"spinSalada")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.spinSalada)

        self.polentaBrustoladaLabel = QLabel(self.formLayoutWidget_3)
        self.polentaBrustoladaLabel.setObjectName(u"polentaBrustoladaLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.polentaBrustoladaLabel)

        self.spinPolenta = QSpinBox(self.formLayoutWidget_3)
        self.spinPolenta.setObjectName(u"spinPolenta")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinPolenta)

        self.sopaDeCapelettiLabel = QLabel(self.formLayoutWidget_3)
        self.sopaDeCapelettiLabel.setObjectName(u"sopaDeCapelettiLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.sopaDeCapelettiLabel)

        self.spinSopa = QSpinBox(self.formLayoutWidget_3)
        self.spinSopa.setObjectName(u"spinSopa")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinSopa)

        self.toolBox.addItem(self.page_3, u"Acompanhamentos")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 701, 251))
        self.formLayoutWidget_4 = QWidget(self.page_4)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(10, 10, 531, 181))
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.petitGateauLabel = QLabel(self.formLayoutWidget_4)
        self.petitGateauLabel.setObjectName(u"petitGateauLabel")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.petitGateauLabel)

        self.spinGateau = QSpinBox(self.formLayoutWidget_4)
        self.spinGateau.setObjectName(u"spinGateau")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.spinGateau)

        self.sorveteLabel = QLabel(self.formLayoutWidget_4)
        self.sorveteLabel.setObjectName(u"sorveteLabel")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.sorveteLabel)

        self.spinSorvete = QSpinBox(self.formLayoutWidget_4)
        self.spinSorvete.setObjectName(u"spinSorvete")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.spinSorvete)

        self.toolBox.addItem(self.page_4, u"Sobremesas")
        self.checkoutButton = QPushButton(self.cardapio)
        self.checkoutButton.setObjectName(u"checkoutButton")
        self.checkoutButton.setGeometry(QRect(544, 460, 151, 24))
        self.tabWidget.addTab(self.cardapio, "")
        self.carrinho = QWidget()
        self.carrinho.setObjectName(u"carrinho")
        self.label = QLabel(self.carrinho)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 49, 16))
        self.spinMesa = QSpinBox(self.carrinho)
        self.spinMesa.setObjectName(u"spinMesa")
        self.spinMesa.setGeometry(QRect(70, 10, 88, 22))
        self.label_2 = QLabel(self.carrinho)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 340, 49, 16))
        self.labelPrecoTotal = QLabel(self.carrinho)
        self.labelPrecoTotal.setObjectName(u"labelPrecoTotal")
        self.labelPrecoTotal.setGeometry(QRect(40, 340, 49, 16))
        self.pagoButton = QPushButton(self.carrinho)
        self.pagoButton.setObjectName(u"pagoButton")
        self.pagoButton.setGeometry(QRect(600, 430, 91, 51))
        self.verticalLayoutWidget_5 = QWidget(self.carrinho)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 40, 651, 291))
        self.itemLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.itemLayout.setObjectName(u"itemLayout")
        self.itemLayout.setContentsMargins(0, 0, 0, 0)
        self.itemLayout.setAlignment(Qt.AlignTop)
        self.tabWidget.addTab(self.carrinho, "")

        self.retranslateUi(Form_Atendente)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form_Atendente)
    # setupUi

    def retranslateUi(self, Form_Atendente):
        Form_Atendente.setWindowTitle(QCoreApplication.translate("Form_Atendente", u"Form", None))
        self.fetuccineAlfredoLabel.setText(QCoreApplication.translate("Form_Atendente", u"Fetuccine Alfredo", None))
        self.spaghettiCarbonaraLabel.setText(QCoreApplication.translate("Form_Atendente", u"Spaghetti Carbonara", None))
        self.gnocciAlPestoLabel.setText(QCoreApplication.translate("Form_Atendente", u"Gnocci al Pesto", None))
        self.macNCheeseKidsLabel.setText(QCoreApplication.translate("Form_Atendente", u"Mac 'n Cheese Kids", None))
        self.fusliBolonhesaLabel.setText(QCoreApplication.translate("Form_Atendente", u"Fusli Bolonhesa", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form_Atendente", u"Lanches", None))
        self.refrigeranteLabel.setText(QCoreApplication.translate("Form_Atendente", u"Refrigerante", None))
        self.sucoNaturalLabel.setText(QCoreApplication.translate("Form_Atendente", u"Suco Natural", None))
        self.guaLabel.setText(QCoreApplication.translate("Form_Atendente", u"\u00c1gua", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Form_Atendente", u"Bebidas", None))
        self.saladaCapreseLabel.setText(QCoreApplication.translate("Form_Atendente", u"Salada Caprese", None))
        self.polentaBrustoladaLabel.setText(QCoreApplication.translate("Form_Atendente", u"Polenta Brustolada", None))
        self.sopaDeCapelettiLabel.setText(QCoreApplication.translate("Form_Atendente", u"Sopa de Capeletti", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Form_Atendente", u"Acompanhamentos", None))
        self.petitGateauLabel.setText(QCoreApplication.translate("Form_Atendente", u"Petit Gateau", None))
        self.sorveteLabel.setText(QCoreApplication.translate("Form_Atendente", u"Sorvete", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Form_Atendente", u"Sobremesas", None))
        self.checkoutButton.setText(QCoreApplication.translate("Form_Atendente", u"Prosseguir para Checkout", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cardapio), QCoreApplication.translate("Form_Atendente", u"Card\u00e1pio", None))
        self.label.setText(QCoreApplication.translate("Form_Atendente", u"Mesa", None))
        self.label_2.setText(QCoreApplication.translate("Form_Atendente", u"Total: ", None))
        self.labelPrecoTotal.setText("")
        self.pagoButton.setText(QCoreApplication.translate("Form_Atendente", u"Finalizado", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.carrinho), QCoreApplication.translate("Form_Atendente", u"Carrinho", None))
    # retranslateUi

