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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(938, 838)
        self.maintab = QTabWidget(Form)
        self.maintab.setObjectName(u"maintab")
        self.maintab.setEnabled(True)
        self.maintab.setGeometry(QRect(30, 460, 881, 341))
        self.maintab.setStyleSheet(u"QTabBar::tab{width:100}\n"
"QTabBar::tab{height:50}")
        self.maintab.setTabPosition(QTabWidget.TabPosition.North)
        self.maintab.setIconSize(QSize(16, 16))
        self.maintab.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.check = QPushButton(self.tab)
        self.check.setObjectName(u"check")
        self.check.setGeometry(QRect(320, 60, 311, 131))
        font = QFont()
        font.setPointSize(26)
        self.check.setFont(font)
        self.maintab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.add = QPushButton(self.tab_2)
        self.add.setObjectName(u"add")
        self.add.setGeometry(QRect(160, 130, 621, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.layoutWidget = QWidget(self.tab_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(170, 50, 601, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.name = QLineEdit(self.layoutWidget)
        self.name.setObjectName(u"name")
        self.name.setMaximumSize(QSize(111111, 111111))

        self.horizontalLayout_3.addWidget(self.name)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.id = QLineEdit(self.layoutWidget)
        self.id.setObjectName(u"id")
        self.id.setMaximumSize(QSize(111111, 1111111))

        self.horizontalLayout_3.addWidget(self.id)

        self.maintab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.check_list = QTableView(self.tab_3)
        self.check_list.setObjectName(u"check_list")
        self.check_list.setGeometry(QRect(0, 0, 951, 231))
        self.maintab.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.layoutWidget1 = QWidget(self.tab_4)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 20, 471, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.find_id = QLineEdit(self.layoutWidget1)
        self.find_id.setObjectName(u"find_id")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.find_id.sizePolicy().hasHeightForWidth())
        self.find_id.setSizePolicy(sizePolicy1)
        self.find_id.setMaximumSize(QSize(1999, 1000))

        self.horizontalLayout_2.addWidget(self.find_id)

        self.find = QPushButton(self.layoutWidget1)
        self.find.setObjectName(u"find")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.find.sizePolicy().hasHeightForWidth())
        self.find.setSizePolicy(sizePolicy2)
        self.find.setMaximumSize(QSize(100, 69))

        self.horizontalLayout_2.addWidget(self.find)

        self.layoutWidget2 = QWidget(self.tab_4)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 90, 471, 41))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout.addWidget(self.label_5)

        self.u_id = QLineEdit(self.layoutWidget2)
        self.u_id.setObjectName(u"u_id")
        sizePolicy2.setHeightForWidth(self.u_id.sizePolicy().hasHeightForWidth())
        self.u_id.setSizePolicy(sizePolicy2)
        self.u_id.setMaximumSize(QSize(11111, 11111))

        self.horizontalLayout.addWidget(self.u_id)

        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout.addWidget(self.label_6)

        self.u_name = QLineEdit(self.layoutWidget2)
        self.u_name.setObjectName(u"u_name")
        self.u_name.setMaximumSize(QSize(111111, 111111))

        self.horizontalLayout.addWidget(self.u_name)

        self.user_list = QTableView(self.tab_4)
        self.user_list.setObjectName(u"user_list")
        self.user_list.setGeometry(QRect(510, 10, 441, 221))
        self.layoutWidget3 = QWidget(self.tab_4)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 150, 481, 71))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.update_name = QPushButton(self.layoutWidget3)
        self.update_name.setObjectName(u"update_name")
        self.update_name.setMaximumSize(QSize(8888, 8888))

        self.horizontalLayout_5.addWidget(self.update_name)

        self.update_id = QPushButton(self.layoutWidget3)
        self.update_id.setObjectName(u"update_id")
        self.update_id.setMaximumSize(QSize(11111, 1111))

        self.horizontalLayout_5.addWidget(self.update_id)

        self.update_ph = QPushButton(self.layoutWidget3)
        self.update_ph.setObjectName(u"update_ph")
        self.update_ph.setMaximumSize(QSize(11111, 11111))

        self.horizontalLayout_5.addWidget(self.update_ph)

        self.del_user = QPushButton(self.layoutWidget3)
        self.del_user.setObjectName(u"del_user")
        self.del_user.setMaximumSize(QSize(1111, 1111))

        self.horizontalLayout_5.addWidget(self.del_user)

        self.maintab.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.draw = QLabel(self.tab_5)
        self.draw.setObjectName(u"draw")
        self.draw.setGeometry(QRect(30, 0, 811, 281))
        self.draw.setStyleSheet(u"")
        self.maintab.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.layoutWidget4 = QWidget(self.tab_6)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(210, 80, 521, 81))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.admin_pass = QLineEdit(self.layoutWidget4)
        self.admin_pass.setObjectName(u"admin_pass")
        self.admin_pass.setMaximumSize(QSize(111111, 11111))

        self.horizontalLayout_4.addWidget(self.admin_pass)

        self.admin_login = QPushButton(self.layoutWidget4)
        self.admin_login.setObjectName(u"admin_login")
        self.admin_login.setMaximumSize(QSize(11111, 11111))

        self.horizontalLayout_4.addWidget(self.admin_login)

        self.exit = QPushButton(self.layoutWidget4)
        self.exit.setObjectName(u"exit")
        self.exit.setMaximumSize(QSize(11111, 11111))

        self.horizontalLayout_4.addWidget(self.exit)

        self.maintab.addTab(self.tab_6, "")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 901, 451))
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.retranslateUi(Form)

        self.maintab.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.check.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b", None))
        self.maintab.setTabText(self.maintab.indexOf(self.tab), QCoreApplication.translate("Form", u"\u4eba\u8138\u8bc6\u522b", None))
        self.add.setText(QCoreApplication.translate("Form", u"\u5f55\u5165", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u59d3\u540d\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u4eba\u8138\u5f55\u5165", None))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u8bc6\u522b\u8bb0\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.find.setText(QCoreApplication.translate("Form", u"\u67e5\u627e", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u59d3\u540d:", None))
        self.update_name.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u59d3\u540d", None))
        self.update_id.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u5b66\u53f7", None))
        self.update_ph.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u7167\u7247", None))
        self.del_user.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u7528\u6237", None))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u7528\u6237\u7ba1\u7406", None))
        self.draw.setText("")
        self.maintab.setTabText(self.maintab.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u6570\u636e\u7edf\u8ba1", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801\uff1a", None))
        self.admin_login.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.exit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
        self.maintab.setTabText(self.maintab.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458\u767b\u5f55", None))
        self.label.setText("")
    # retranslateUi

