# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\PYTHON\PySeer\ui\load_file_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadFile(object):
    def setupUi(self, LoadFile):
        LoadFile.setObjectName("LoadFile")
        LoadFile.resize(320, 240)
        LoadFile.setMinimumSize(QtCore.QSize(320, 240))
        LoadFile.setMaximumSize(QtCore.QSize(320, 240))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        LoadFile.setFont(font)
        self.centralwidget = QtWidgets.QWidget(LoadFile)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 58))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 70, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 110, 97, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.layoutWidget1.setFont(font)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_1 = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout_2.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 181, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        LoadFile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoadFile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 23))
        self.menubar.setObjectName("menubar")
        LoadFile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoadFile)
        self.statusbar.setObjectName("statusbar")
        LoadFile.setStatusBar(self.statusbar)

        self.retranslateUi(LoadFile)
        self.lineEdit.textChanged['QString'].connect(LoadFile.update_dbpath)
        self.lineEdit_2.textChanged['QString'].connect(LoadFile.update_windowname)
        self.pushButton.clicked.connect(LoadFile.btn_clicked_1)
        self.checkBox_2.clicked.connect(LoadFile.checkbox_2_clicked)
        self.checkBox_1.clicked.connect(LoadFile.checkbox_1_clicked)
        QtCore.QMetaObject.connectSlotsByName(LoadFile)

    def retranslateUi(self, LoadFile):
        _translate = QtCore.QCoreApplication.translate
        LoadFile.setWindowTitle(_translate("LoadFile", "MainWindow"))
        self.label.setText(_translate("LoadFile", "文件路径："))
        self.label_2.setText(_translate("LoadFile", "窗口标题："))
        self.pushButton.setText(_translate("LoadFile", "加载"))
        self.checkBox_1.setText(_translate("LoadFile", "开启防止休眠"))
        self.checkBox_2.setText(_translate("LoadFile", "开启随机点击"))
        self.label_3.setText(_translate("LoadFile", "！！！运行中按\'1\'停止运行！！！"))
