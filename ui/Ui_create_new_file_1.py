# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\PYTHON\PySeer\ui\create_new_file_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateNewFile(object):
    def setupUi(self, CreateNewFile):
        CreateNewFile.setObjectName("CreateNewFile")
        CreateNewFile.resize(320, 240)
        CreateNewFile.setMinimumSize(QtCore.QSize(320, 240))
        CreateNewFile.setMaximumSize(QtCore.QSize(320, 240))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        CreateNewFile.setFont(font)
        self.pushButton = QtWidgets.QPushButton(CreateNewFile)
        self.pushButton.setGeometry(QtCore.QRect(120, 120, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(CreateNewFile)
        self.widget.setGeometry(QtCore.QRect(20, 40, 291, 58))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CreateNewFile)
        self.lineEdit.textChanged['QString'].connect(CreateNewFile.update_text)
        self.pushButton.clicked.connect(CreateNewFile.btn_clicked)
        QtCore.QMetaObject.connectSlotsByName(CreateNewFile)

    def retranslateUi(self, CreateNewFile):
        _translate = QtCore.QCoreApplication.translate
        CreateNewFile.setWindowTitle(_translate("CreateNewFile", "Form"))
        self.pushButton.setText(_translate("CreateNewFile", "开始"))
        self.label.setText(_translate("CreateNewFile", "脚本名："))