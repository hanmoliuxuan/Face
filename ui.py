# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTableView,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 693)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(20, 450, 640, 221))
        self.tabWidget.setStyleSheet(u"QTabBar::tab{width:100}\n"
"QTabBar::tab{height:30}")
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setIconSize(QSize(16, 16))
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.check = QPushButton(self.tab)
        self.check.setObjectName(u"check")
        self.check.setGeometry(QRect(0, 40, 341, 91))
        self.showface = QLabel(self.tab)
        self.showface.setObjectName(u"showface")
        self.showface.setGeometry(QRect(350, 10, 271, 151))
        self.showface.setStyleSheet(u"")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.add = QPushButton(self.tab_2)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(10, 110, 630, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.name = QLineEdit(self.tab_2)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(120, 30, 113, 20))
        self.id = QLineEdit(self.tab_2)
        self.id.setObjectName(u"id")
        self.id.setGeometry(QRect(370, 30, 113, 20))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 50, 15))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(290, 30, 50, 15))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.check_list = QTableView(self.tab_3)
        self.check_list.setObjectName(u"check_list")
        self.check_list.setGeometry(QRect(0, 0, 630, 181))
        self.tabWidget.addTab(self.tab_3, "")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 640, 380))
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.check.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b", None))
        self.showface.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u4eba\u8138\u8bc6\u522b", None))
        self.add.setText(QCoreApplication.translate("Form", u"\u5f55\u5165", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u59d3\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u4eba\u8138\u5f55\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u8bc6\u522b\u8bb0\u5f55", None))
        self.label.setText("")
    # retranslateUi

