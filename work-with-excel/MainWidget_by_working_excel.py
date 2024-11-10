# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidget_by_working_excel.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(739, 585)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_excel_template = QLineEdit(self.groupBox)
        self.lineEdit_excel_template.setObjectName(u"lineEdit_excel_template")

        self.verticalLayout_2.addWidget(self.lineEdit_excel_template)

        self.lineEdit_path_creating_file = QLineEdit(self.groupBox)
        self.lineEdit_path_creating_file.setObjectName(u"lineEdit_path_creating_file")

        self.verticalLayout_2.addWidget(self.lineEdit_path_creating_file)

        self.lineEdit_plate_info = QLineEdit(self.groupBox)
        self.lineEdit_plate_info.setObjectName(u"lineEdit_plate_info")

        self.verticalLayout_2.addWidget(self.lineEdit_plate_info)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_excel_template = QPushButton(self.groupBox)
        self.pushButton_excel_template.setObjectName(u"pushButton_excel_template")

        self.verticalLayout.addWidget(self.pushButton_excel_template)

        self.pushButton_path_creating_file = QPushButton(self.groupBox)
        self.pushButton_path_creating_file.setObjectName(u"pushButton_path_creating_file")

        self.verticalLayout.addWidget(self.pushButton_path_creating_file)

        self.pushButton_plate_info = QPushButton(self.groupBox)
        self.pushButton_plate_info.setObjectName(u"pushButton_plate_info")

        self.verticalLayout.addWidget(self.pushButton_plate_info)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.pushButton_save_default_settings = QPushButton(self.groupBox)
        self.pushButton_save_default_settings.setObjectName(u"pushButton_save_default_settings")

        self.verticalLayout_7.addWidget(self.pushButton_save_default_settings)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_CHEUS = QLabel(self.groupBox_2)
        self.label_CHEUS.setObjectName(u"label_CHEUS")
        self.label_CHEUS.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_CHEUS)

        self.lineEdit_CHEUS = QLineEdit(self.groupBox_2)
        self.lineEdit_CHEUS.setObjectName(u"lineEdit_CHEUS")

        self.verticalLayout_3.addWidget(self.lineEdit_CHEUS)

        self.label_CHELU = QLabel(self.groupBox_2)
        self.label_CHELU.setObjectName(u"label_CHELU")
        self.label_CHELU.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_CHELU)

        self.lineEdit_CHELU = QLineEdit(self.groupBox_2)
        self.lineEdit_CHELU.setObjectName(u"lineEdit_CHELU")

        self.verticalLayout_3.addWidget(self.lineEdit_CHELU)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.pushButton_find_data_sensitive_elements = QPushButton(self.groupBox_2)
        self.pushButton_find_data_sensitive_elements.setObjectName(u"pushButton_find_data_sensitive_elements")

        self.horizontalLayout_2.addWidget(self.pushButton_find_data_sensitive_elements)

        self.tableView_sensitive_elements = QTableView(self.groupBox_2)
        self.tableView_sensitive_elements.setObjectName(u"tableView_sensitive_elements")

        self.horizontalLayout_2.addWidget(self.tableView_sensitive_elements)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_file_number = QLabel(self.groupBox_2)
        self.label_file_number.setObjectName(u"label_file_number")
        self.label_file_number.setFrameShadow(QFrame.Shadow.Raised)
        self.label_file_number.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_file_number)

        self.lineEdit_file_number = QLineEdit(self.groupBox_2)
        self.lineEdit_file_number.setObjectName(u"lineEdit_file_number")

        self.verticalLayout_4.addWidget(self.lineEdit_file_number)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.pushButton_file_number = QPushButton(self.groupBox_2)
        self.pushButton_file_number.setObjectName(u"pushButton_file_number")

        self.horizontalLayout_3.addWidget(self.pushButton_file_number)

        self.textBrowser_file_number = QTextBrowser(self.groupBox_2)
        self.textBrowser_file_number.setObjectName(u"textBrowser_file_number")

        self.horizontalLayout_3.addWidget(self.textBrowser_file_number)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_from = QLabel(self.groupBox_3)
        self.label_from.setObjectName(u"label_from")

        self.horizontalLayout_4.addWidget(self.label_from)

        self.lineEdit_from = QLineEdit(self.groupBox_3)
        self.lineEdit_from.setObjectName(u"lineEdit_from")

        self.horizontalLayout_4.addWidget(self.lineEdit_from)

        self.label_to = QLabel(self.groupBox_3)
        self.label_to.setObjectName(u"label_to")

        self.horizontalLayout_4.addWidget(self.label_to)

        self.lineEdit_to = QLineEdit(self.groupBox_3)
        self.lineEdit_to.setObjectName(u"lineEdit_to")

        self.horizontalLayout_4.addWidget(self.lineEdit_to)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.pushButton_create_file = QPushButton(self.groupBox_3)
        self.pushButton_create_file.setObjectName(u"pushButton_create_file")

        self.horizontalLayout_5.addWidget(self.pushButton_create_file)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 28))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u044d\u043a\u0441\u0435\u043b\u044c \u0444\u0430\u0439\u043b\u043e\u0432 \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u0435\u043b\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.pushButton_excel_template.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0431\u043b\u043e\u043d \u044d\u043a\u0441\u0435\u043b\u044c \u0444\u0430\u0439\u043b\u0430", None))
        self.pushButton_path_creating_file.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0434\u0435 \u0441\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.pushButton_plate_info.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u043b\u0430\u0441\u0442\u0438\u043d\u0430\u0445", None))
        self.pushButton_save_default_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u043e \u0427\u0443\u0432\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u043c \u044d\u043b\u043b\u0435\u043c\u0435\u043d\u0442\u0430\u043c", None))
        self.label_CHEUS.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0427\u042d\u0423\u0421", None))
        self.label_CHELU.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0427\u042d\u041b\u0423", None))
        self.pushButton_find_data_sensitive_elements.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0439\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0439 \u0427\u042d", None))
        self.label_file_number.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u044d\u0441\u043a\u0435\u043b\u044c \u0444\u0430\u0439\u043b\u0430", None))
        self.pushButton_file_number.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u043e\u0432 \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443", None))
        self.label_from.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.label_to.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e", None))
        self.pushButton_create_file.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
    # retranslateUi

