# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\\FaceRecognition\\venv\\src\\MainForm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from StaticMode import Ui_StaticForm
from DynamicMode import Ui_DynamicForm

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainForm(object):

    def setupUi(self, MainForm):
        #窗体设置
        MainForm.setObjectName(_fromUtf8("MainForm"))       #窗体名称
        MainForm.setWindowModality(QtCore.Qt.NonModal)
        MainForm.setEnabled(True)       #窗体可交互
        MainForm.resize(1311, 799)
        MainForm.setAutoFillBackground(False)
        MainForm.setStyleSheet(_fromUtf8("background-image: url(:/mainform/主窗口背景.jpg);"))       #样式表
        MainForm.setInputMethodHints(QtCore.Qt.ImhNone)
        self.form = MainForm

        self.widget = QtGui.QWidget(MainForm)
        self.widget.setEnabled(True)
        self.widget.setObjectName(_fromUtf8("widget"))

        #静态识别模式按钮
        self.BtnStatic = QtGui.QPushButton(self.widget)
        self.BtnStatic.setEnabled(True)
        self.BtnStatic.setGeometry(QtCore.QRect(840, 220, 311, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文行楷"))
        font.setPointSize(14)
        self.BtnStatic.setFont(font)
        self.BtnStatic.setStyleSheet(_fromUtf8("background-color:rgb(50, 56, 61)"))
        self.BtnStatic.setObjectName(_fromUtf8("BtnStatic"))

        #动态识别模式按钮
        self.BtnDynamic = QtGui.QPushButton(self.widget)
        self.BtnDynamic.setEnabled(True)
        self.BtnDynamic.setGeometry(QtCore.QRect(840, 330, 311, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文行楷"))
        font.setPointSize(14)
        self.BtnDynamic.setFont(font)
        self.BtnDynamic.setStyleSheet(_fromUtf8("background-color: rgb(50, 56, 61);"))
        self.BtnDynamic.setObjectName(_fromUtf8("BtnDynamic"))

        #退出按钮
        self.BtnExit = QtGui.QPushButton(self.widget)
        self.BtnExit.setGeometry(QtCore.QRect(840, 440, 311, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("华文行楷"))
        font.setPointSize(14)
        self.BtnExit.setFont(font)
        self.BtnExit.setStyleSheet(_fromUtf8("background-color: rgb(50, 56, 61);"))
        self.BtnExit.setObjectName(_fromUtf8("BtnExit"))

        #文本框
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1311, 801))
        self.label.setObjectName(_fromUtf8("label"))
        self.label.raise_()
        self.BtnStatic.raise_()
        self.BtnDynamic.raise_()
        self.BtnExit.raise_()
        MainForm.setCentralWidget(self.widget)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

        #信号连接到指定槽
        self.BtnStatic.clicked.connect(self.on_BtnStatic_clicked)
        self.BtnDynamic.clicked.connect(self.on_BtnDynamic_clicked)
        self.BtnExit.clicked.connect(self.on_BtnExit_clicked)

    def retranslateUi(self, MainForm):
        MainForm.setWindowTitle(_translate("MainForm", "人脸识别系统", None))
        self.BtnStatic.setText(_translate("MainForm", "静态识别模式", None))
        self.BtnDynamic.setText(_translate("MainForm", "动态识别模式", None))
        self.BtnExit.setText(_translate("MainForm", "退出", None))
        self.label.setText(_translate("MainForm", "<html><head/><body><p><img src=\":/mainform/主窗口背景.jpg\"/></p></body></html>", None))

    def on_BtnStatic_clicked(self):         #静态识别模式按钮
        self.form.hide()
        SForm = QtGui.QDialog()
        ui = Ui_StaticForm()
        ui.setupUi(SForm)
        SForm.show()
        SForm.exec_()
        self.form.show()

    def on_BtnDynamic_clicked(self):        #动态识别模式按钮
        self.form.hide()
        DForm = QtGui.QDialog()
        ui = Ui_DynamicForm()
        ui.setupUi(DForm)
        DForm.show()
        DForm.exec_()
        self.form.show()

    def on_BtnExit_clicked(self):       #退出按钮
        self.form.close()


import background_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainForm = QtGui.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())

