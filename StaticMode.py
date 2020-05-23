# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\\FaceRecognition\\venv\\src\\StaticForm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import face_recognition
import cv2
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os
os.chdir("E:\\FaceRecognition\\venv\\sample")
import win32api,win32con

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

class Ui_StaticForm(object):

    def setupUi(self, StaticForm):
        #窗体
        StaticForm.setObjectName(_fromUtf8("StaticForm"))
        StaticForm.resize(1311, 799)
        self.form = StaticForm

        #应到人员输入框
        self.TextYingdao = QtGui.QTextEdit(StaticForm)
        self.TextYingdao.setEnabled(True)
        self.TextYingdao.setGeometry(QtCore.QRect(40, 100, 721, 261))
        self.TextYingdao.setAcceptDrops(True)
        self.TextYingdao.setAutoFillBackground(True)
        self.TextYingdao.setStyleSheet(_fromUtf8("background-image: url(:/text/白色背景.jpg);"))
        self.TextYingdao.setTabChangesFocus(False)
        self.TextYingdao.setOverwriteMode(False)
        self.TextYingdao.setObjectName(_fromUtf8("TextYingdao"))

        #文本框
        self.label_2 = QtGui.QLabel(StaticForm)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 561, 51))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        #信息录入按钮
        self.BtnLuru = QtGui.QPushButton(StaticForm)
        self.BtnLuru.setGeometry(QtCore.QRect(610, 40, 150, 46))
        self.BtnLuru.setStyleSheet(_fromUtf8("background-image: url(:/button/按钮背景.jpg);\n"
"border-image: url(:/button/按钮背景.jpg);"))
        self.BtnLuru.setObjectName(_fromUtf8("BtnLuru"))

        #照片识别按钮
        self.BtnPhoto = QtGui.QPushButton(StaticForm)
        self.BtnPhoto.setGeometry(QtCore.QRect(620, 380, 150, 46))
        self.BtnPhoto.setStyleSheet(_fromUtf8("background-image: url(:/button/按钮背景.jpg);\n"
"border-image: url(:/button/按钮背景.jpg);"))
        self.BtnPhoto.setObjectName(_fromUtf8("BtnPhoto"))

        #文本框
        self.label_3 = QtGui.QLabel(StaticForm)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 161, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        #缺席名单输出框
        self.TextQuexi = QtGui.QTextEdit(StaticForm)
        self.TextQuexi.setGeometry(QtCore.QRect(40, 480, 731, 231))
        self.TextQuexi.setStyleSheet(_fromUtf8("background-image: url(:/text/白色背景.jpg);"))
        self.TextQuexi.setObjectName(_fromUtf8("TextQuexi"))

        #返回主界面按钮
        self.BtnReturn = QtGui.QPushButton(StaticForm)
        self.BtnReturn.setGeometry(QtCore.QRect(1040, 650, 150, 46))
        self.BtnReturn.setStyleSheet(_fromUtf8("background-image: url(:/button/按钮背景.jpg);\n"
"border-image: url(:/button/按钮背景.jpg);"))
        self.BtnReturn.setObjectName(_fromUtf8("BtnReturn"))

        #文本框
        self.label = QtGui.QLabel(StaticForm)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(0, 0, 1311, 801))
        self.label.setObjectName(_fromUtf8("label"))

        #文本框
        self.label_4 = QtGui.QLabel(StaticForm)
        self.label_4.setGeometry(QtCore.QRect(40, 380, 241, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        #目标文件名输入框
        self.TextTargetimagepath = QtGui.QLineEdit(StaticForm)
        self.TextTargetimagepath.setGeometry(QtCore.QRect(280, 380, 321, 41))
        self.TextTargetimagepath.setObjectName(_fromUtf8("TextTargetimagepath"))

        self.label.raise_()
        self.TextYingdao.raise_()
        self.label_2.raise_()
        self.BtnLuru.raise_()
        self.BtnPhoto.raise_()
        self.label_3.raise_()
        self.TextQuexi.raise_()
        self.BtnReturn.raise_()
        self.label_4.raise_()
        self.TextTargetimagepath.raise_()

        self.retranslateUi(StaticForm)
        QtCore.QMetaObject.connectSlotsByName(StaticForm)

        #信号连接指定槽
        self.BtnLuru.clicked.connect(self.on_BtnLuru_clicked)
        self.BtnPhoto.clicked.connect(self.on_BtnPhoto_clicked)
        self.BtnReturn.clicked.connect(self.on_BtnReturn_clicked)

    def retranslateUi(self, StaticForm):
        StaticForm.setWindowTitle(_translate("StaticForm", "静态识别模式", None))
        self.TextYingdao.setHtml(_translate("StaticForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(_translate("StaticForm", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">请录入应到人员名单：（人名之间用空格隔开）</span></p></body></html>", None))
        self.BtnLuru.setText(_translate("StaticForm", "信息录入", None))
        self.BtnPhoto.setText(_translate("StaticForm", "照片识别", None))
        self.label_3.setText(_translate("StaticForm", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">缺席名单：</span></p></body></html>", None))
        self.BtnReturn.setText(_translate("StaticForm", "返回主界面", None))
        self.label.setText(_translate("StaticForm", "<html><head/><body><p><img src=\":/staticform/静态识别模式窗口背景.jpg\"/></p></body></html>", None))
        self.label_4.setText(_translate("StaticForm", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">请输入目标文件名：</span></p></body></html>", None))

    def close_application(self):
        sys.exit()

    def on_BtnLuru_clicked(self):       #信息录入按钮
        counter = 0     #用来统计输入不规范的情况
        textYingdao = self.TextYingdao.toPlainText()        #获取应到人员输入框内容
        if(textYingdao == ""):
            win32api.MessageBox(0,"请输入应到人员名单！","提醒",win32con.MB_OK)
        else:
            if(textYingdao == "default"):
                textYingdao = "LiHuachao LiYu LiuHaoran WuKaiyan"
            names = textYingdao.split(" ")
            for name in names:
                pname = name + ".jpg"
                if os.path.exists(pname):
                    continue
                else:
                    counter += 1
                    m = name + "信息不存在！"
                    win32api.MessageBox(0,m,"提醒",win32con.MB_OK)
        if(counter == 0):
            self.TextQuexi.clear()
            print("信息录入完毕")
            if (textYingdao == "default"):
                textYingdao = "LiHuachao LiYu LiuHaoran WuKaiya"
            print("应到人员名单为：",textYingdao)
            return textYingdao

    def faces_pictures(self):
        strYingdao = self.TextYingdao.toPlainText()
        names = strYingdao.split(" ")

        # 读取库中单人图片及测试图片
        counter = 0     #用来统计输入不规范的情况
        images = []
        textTargetimagename = self.TextTargetimagepath.text()
        image_target_name = "E:\\FaceRecognition\\venv\\test\\" + textTargetimagename
        if(textTargetimagename == ""):
            counter += 1
            win32api.MessageBox(0,"请输入目标文件名！","提醒",win32con.MB_OK)
        else:
            if os.path.exists(image_target_name):
                counter += 0
            else:
                counter += 1
                win32api.MessageBox(0, "目标文件不存在！", "提醒", win32con.MB_OK)

        if (counter == 0):
            for name in names:
                pname = name + ".jpg"
                image = face_recognition.load_image_file(pname)
                images.append(image)
                image_target = face_recognition.load_image_file(image_target_name)  # "E:\\FaceRecognition\\venv\\test\\three.jpg")

            # 将人脸的图像数据转换成128位向量
            face_encodings = []
            for image in images:
                encoding = face_recognition.face_encodings(image)[0]
                face_encodings.append(encoding)
                target_face_encodings = face_recognition.face_encodings(image_target)

            # 储存人脸位置信息并框出
            face_locations = face_recognition.face_locations((image_target))
            attendee_names = []
            absentee_names = []
            for i in range(len(target_face_encodings)):
                target_encoding = target_face_encodings[i]
                face_location = face_locations[i]
                top, right, bottom, left = face_location
                cv2.rectangle(image_target, (left, top), (right, bottom), (0, 255, 255), 2)
                results_recognition = face_recognition.compare_faces(face_encodings, target_encoding, tolerance=0.4)
                for j in range(len(results_recognition)):
                    if results_recognition[j]:
                        name = names[j]
                        attendee_names.append(name)
                        cv2.putText(image_target, name, (left - 10, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                (255, 255, 255, 255), 2)

            # 打印缺席名单
            for item in names:
                if item not in attendee_names:
                    absentee_names.append(item)
            cv2.putText(image_target, "absentee_names:", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 180), 2)
            cv2.putText(image_target, "、".join(absentee_names), (0, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 180), 2)

            # 显示窗口
            image_target_rgb = cv2.cvtColor(image_target, cv2.COLOR_BGR2RGB)
            cv2.namedWindow("results_recognition", 0);
            cv2.resizeWindow("results_recognition", 1280, 720)
            cv2.imshow("results_recognition", image_target_rgb)
            print("缺席名单：", absentee_names)
            return (absentee_names)
            # 等待按键
            cv2.waitKey(0)

    def on_BtnReturn_clicked(self):         #返回主界面按钮
        self.form.close()

    def on_BtnPhoto_clicked(self):          #照片识别按钮

        i = Ui_StaticForm.faces_pictures(self)
        if i:
            self.TextQuexi.setText(','.join(i))


import background_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    StaticForm = QtGui.QWidget()
    ui = Ui_StaticForm()
    ui.setupUi(StaticForm)
    StaticForm.show()
    sys.exit(app.exec_())
