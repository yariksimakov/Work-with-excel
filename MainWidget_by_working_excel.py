# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidget_by_working_excel.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(864, 585)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(14)
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
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


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.pushButton_save_default_settings = QPushButton(self.groupBox)
        self.pushButton_save_default_settings.setObjectName(u"pushButton_save_default_settings")

        self.verticalLayout_8.addWidget(self.pushButton_save_default_settings)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget_CC = QTableWidget(self.groupBox_2)
        if (self.tableWidget_CC.columnCount() < 6):
            self.tableWidget_CC.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_CC.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_CC.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_CC.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_CC.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_CC.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_CC.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget_CC.rowCount() < 5):
            self.tableWidget_CC.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_CC.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_CC.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_CC.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_CC.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_CC.setVerticalHeaderItem(4, __qtablewidgetitem10)
        self.tableWidget_CC.setObjectName(u"tableWidget_CC")

        self.horizontalLayout_2.addWidget(self.tableWidget_CC)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.verticalSpacer = QSpacerItem(20, 98, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_number_CC = QLabel(self.groupBox_2)
        self.label_number_CC.setObjectName(u"label_number_CC")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_number_CC.sizePolicy().hasHeightForWidth())
        self.label_number_CC.setSizePolicy(sizePolicy1)
        self.label_number_CC.setMaximumSize(QSize(200, 16777215))
        self.label_number_CC.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_number_CC)

        self.lineEdit_number_CC = QLineEdit(self.groupBox_2)
        self.lineEdit_number_CC.setObjectName(u"lineEdit_number_CC")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_number_CC.sizePolicy().hasHeightForWidth())
        self.lineEdit_number_CC.setSizePolicy(sizePolicy2)
        self.lineEdit_number_CC.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_number_CC.setMaxLength(200)
        self.lineEdit_number_CC.setFrame(True)
        self.lineEdit_number_CC.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_number_CC)

        self.pushButton_create_CC = QPushButton(self.groupBox_2)
        self.pushButton_create_CC.setObjectName(u"pushButton_create_CC")
        sizePolicy2.setHeightForWidth(self.pushButton_create_CC.sizePolicy().hasHeightForWidth())
        self.pushButton_create_CC.setSizePolicy(sizePolicy2)
        self.pushButton_create_CC.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_3.addWidget(self.pushButton_create_CC)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox_2)

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


        self.verticalLayout_4.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 864, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton_create_CC.setDefault(False)


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
        ___qtablewidgetitem = self.tableWidget_CC.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0421ell", None));
        ___qtablewidgetitem1 = self.tableWidget_CC.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem2 = self.tableWidget_CC.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem3 = self.tableWidget_CC.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem4 = self.tableWidget_CC.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem5 = self.tableWidget_CC.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_number_CC.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u041a\u041f", None))
        self.pushButton_create_CC.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u043e\u0432 \u043f\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0443", None))
        self.label_from.setText(QCoreApplication.translate("MainWindow", u"\u0421", None))
        self.label_to.setText(QCoreApplication.translate("MainWindow", u"\u041f\u041e", None))
        self.pushButton_create_file.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
    # retranslateUi

