# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cardapio.ui'
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
    QLineEdit, QSizePolicy, QToolBox, QWidget)

class Ui_Form_Cardapio(object):
    def setupUi(self, Form_Atendente):
        if not Form_Atendente.objectName():
            Form_Atendente.setObjectName(u"Form_Atendente")
        Form_Atendente.resize(703, 381)
        self.toolBox = QToolBox(Form_Atendente)
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

        self.fetuccineAlfredoLineEdit = QLineEdit(self.formLayoutWidget)
        self.fetuccineAlfredoLineEdit.setObjectName(u"fetuccineAlfredoLineEdit")
        self.fetuccineAlfredoLineEdit.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.fetuccineAlfredoLineEdit)

        self.spaghettiCarbonaraLabel = QLabel(self.formLayoutWidget)
        self.spaghettiCarbonaraLabel.setObjectName(u"spaghettiCarbonaraLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.spaghettiCarbonaraLabel)

        self.spaghettiCarbonaraLineEdit = QLineEdit(self.formLayoutWidget)
        self.spaghettiCarbonaraLineEdit.setObjectName(u"spaghettiCarbonaraLineEdit")
        self.spaghettiCarbonaraLineEdit.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spaghettiCarbonaraLineEdit)

        self.gnocciAlPestoLabel = QLabel(self.formLayoutWidget)
        self.gnocciAlPestoLabel.setObjectName(u"gnocciAlPestoLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.gnocciAlPestoLabel)

        self.gnocciAlPestoLineEdit = QLineEdit(self.formLayoutWidget)
        self.gnocciAlPestoLineEdit.setObjectName(u"gnocciAlPestoLineEdit")
        self.gnocciAlPestoLineEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.gnocciAlPestoLineEdit)

        self.macNCheeseKidsLabel = QLabel(self.formLayoutWidget)
        self.macNCheeseKidsLabel.setObjectName(u"macNCheeseKidsLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.macNCheeseKidsLabel)

        self.macNCheeseKidsLineEdit = QLineEdit(self.formLayoutWidget)
        self.macNCheeseKidsLineEdit.setObjectName(u"macNCheeseKidsLineEdit")
        self.macNCheeseKidsLineEdit.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.macNCheeseKidsLineEdit)

        self.fusliBolonhesaLabel = QLabel(self.formLayoutWidget)
        self.fusliBolonhesaLabel.setObjectName(u"fusliBolonhesaLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.fusliBolonhesaLabel)

        self.fusliBolonhesaLineEdit = QLineEdit(self.formLayoutWidget)
        self.fusliBolonhesaLineEdit.setObjectName(u"fusliBolonhesaLineEdit")
        self.fusliBolonhesaLineEdit.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.fusliBolonhesaLineEdit)

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

        self.refrigeranteLineEdit = QLineEdit(self.formLayoutWidget_2)
        self.refrigeranteLineEdit.setObjectName(u"refrigeranteLineEdit")
        self.refrigeranteLineEdit.setEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.refrigeranteLineEdit)

        self.sucoNaturalLabel = QLabel(self.formLayoutWidget_2)
        self.sucoNaturalLabel.setObjectName(u"sucoNaturalLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.sucoNaturalLabel)

        self.sucoNaturalLineEdit = QLineEdit(self.formLayoutWidget_2)
        self.sucoNaturalLineEdit.setObjectName(u"sucoNaturalLineEdit")
        self.sucoNaturalLineEdit.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.sucoNaturalLineEdit)

        self.guaLabel = QLabel(self.formLayoutWidget_2)
        self.guaLabel.setObjectName(u"guaLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.guaLabel)

        self.guaLineEdit = QLineEdit(self.formLayoutWidget_2)
        self.guaLineEdit.setObjectName(u"guaLineEdit")
        self.guaLineEdit.setEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.guaLineEdit)

        self.toolBox.addItem(self.page_2, u"Bebidas")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 701, 251))
        self.formLayoutWidget_3 = QWidget(self.page_3)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 0, 521, 201))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.saladaCapreseLabel = QLabel(self.formLayoutWidget_3)
        self.saladaCapreseLabel.setObjectName(u"saladaCapreseLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.saladaCapreseLabel)

        self.saladaCapreseLineEdit = QLineEdit(self.formLayoutWidget_3)
        self.saladaCapreseLineEdit.setObjectName(u"saladaCapreseLineEdit")
        self.saladaCapreseLineEdit.setEnabled(False)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.saladaCapreseLineEdit)

        self.polentaBrustoladaLabel = QLabel(self.formLayoutWidget_3)
        self.polentaBrustoladaLabel.setObjectName(u"polentaBrustoladaLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.polentaBrustoladaLabel)

        self.polentaBrustoladaLineEdit = QLineEdit(self.formLayoutWidget_3)
        self.polentaBrustoladaLineEdit.setObjectName(u"polentaBrustoladaLineEdit")
        self.polentaBrustoladaLineEdit.setEnabled(False)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.polentaBrustoladaLineEdit)

        self.sopaDeCapelettiLabel = QLabel(self.formLayoutWidget_3)
        self.sopaDeCapelettiLabel.setObjectName(u"sopaDeCapelettiLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.sopaDeCapelettiLabel)

        self.sopaDeCapelettiLineEdit = QLineEdit(self.formLayoutWidget_3)
        self.sopaDeCapelettiLineEdit.setObjectName(u"sopaDeCapelettiLineEdit")
        self.sopaDeCapelettiLineEdit.setEnabled(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.sopaDeCapelettiLineEdit)

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

        self.petitGateauLineEdit = QLineEdit(self.formLayoutWidget_4)
        self.petitGateauLineEdit.setObjectName(u"petitGateauLineEdit")
        self.petitGateauLineEdit.setEnabled(False)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.petitGateauLineEdit)

        self.sorveteLabel = QLabel(self.formLayoutWidget_4)
        self.sorveteLabel.setObjectName(u"sorveteLabel")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.sorveteLabel)

        self.sorveteLineEdit = QLineEdit(self.formLayoutWidget_4)
        self.sorveteLineEdit.setObjectName(u"sorveteLineEdit")
        self.sorveteLineEdit.setEnabled(False)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.sorveteLineEdit)

        self.toolBox.addItem(self.page_4, u"Sobremesas")

        self.retranslateUi(Form_Atendente)

        self.toolBox.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form_Atendente)
    # setupUi

    def retranslateUi(self, Form_Atendente):
        Form_Atendente.setWindowTitle(QCoreApplication.translate("Form_Atendente", u"Form", None))
        self.fetuccineAlfredoLabel.setText(QCoreApplication.translate("Form_Atendente", u"Fetuccine Alfredo", None))
        self.fetuccineAlfredoLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 20,00", None))
        self.spaghettiCarbonaraLabel.setText(QCoreApplication.translate("Form_Atendente", u"Spaghetti Carbonara", None))
        self.spaghettiCarbonaraLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 25,00", None))
        self.gnocciAlPestoLabel.setText(QCoreApplication.translate("Form_Atendente", u"Gnocci al Pesto", None))
        self.gnocciAlPestoLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 30,00", None))
        self.macNCheeseKidsLabel.setText(QCoreApplication.translate("Form_Atendente", u"Mac 'n Cheese Kids", None))
        self.macNCheeseKidsLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 15,00", None))
        self.fusliBolonhesaLabel.setText(QCoreApplication.translate("Form_Atendente", u"Fusli Bolonhesa", None))
        self.fusliBolonhesaLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 20,00", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form_Atendente", u"Lanches", None))
        self.refrigeranteLabel.setText(QCoreApplication.translate("Form_Atendente", u"Refrigerante", None))
        self.refrigeranteLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 5,00", None))
        self.sucoNaturalLabel.setText(QCoreApplication.translate("Form_Atendente", u"Suco Natural", None))
        self.sucoNaturalLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 6,00", None))
        self.guaLabel.setText(QCoreApplication.translate("Form_Atendente", u"\u00c1gua", None))
        self.guaLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 3,00", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Form_Atendente", u"Bebidas", None))
        self.saladaCapreseLabel.setText(QCoreApplication.translate("Form_Atendente", u"Salada Caprese", None))
        self.saladaCapreseLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 15,00", None))
        self.polentaBrustoladaLabel.setText(QCoreApplication.translate("Form_Atendente", u"Polenta Brustolada", None))
        self.polentaBrustoladaLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 10,00", None))
        self.sopaDeCapelettiLabel.setText(QCoreApplication.translate("Form_Atendente", u"Sopa de Capeletti", None))
        self.sopaDeCapelettiLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 18,00", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Form_Atendente", u"Acompanhamentos", None))
        self.petitGateauLabel.setText(QCoreApplication.translate("Form_Atendente", u"Petit Gateau", None))
        self.petitGateauLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 15,00", None))
        self.sorveteLabel.setText(QCoreApplication.translate("Form_Atendente", u"Sorvete", None))
        self.sorveteLineEdit.setText(QCoreApplication.translate("Form_Atendente", u"R$ 10,00", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Form_Atendente", u"Sobremesas", None))
    # retranslateUi

