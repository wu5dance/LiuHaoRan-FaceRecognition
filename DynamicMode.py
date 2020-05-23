# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\\FaceRecognition\\venv\\src\\DynamicForm.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import face_recognition
import cv2
from PyQt4 import QtCore, QtGui
import os
os.chdir("E:\\FaceRecognition\\venv\\sample")

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

class Ui_DynamicForm(object):

    def setupUi(self, DynamicForm):
        #窗体
        DynamicForm.setObjectName(_fromUtf8("DynamicForm"))
        DynamicForm.resize(1310, 800)
        self.form = DynamicForm

        #文本框
        self.label = QtGui.QLabel(DynamicForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 1311, 801))
        self.label.setObjectName(_fromUtf8("label"))

        #文本框
        self.label_2 = QtGui.QLabel(DynamicForm)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 561, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        #应到人员输入框
        self.TextYingdao = QtGui.QTextEdit(DynamicForm)
        self.TextYingdao.setGeometry(QtCore.QRect(60, 120, 761, 231))
        self.TextYingdao.setObjectName(_fromUtf8("TextYingdao"))

        #信息录入按钮
        self.BtnLuru = QtGui.QPushButton(DynamicForm)
        self.BtnLuru.setGeometry(QtCore.QRect(60, 360, 150, 46))
        self.BtnLuru.setObjectName(_fromUtf8("BtnLuru"))
        
        #摄像头识别按钮
        self.BtnCamera = QtGui.QPushButton(DynamicForm)
        self.BtnCamera.setGeometry(QtCore.QRect(670, 360, 150, 46))
        self.BtnCamera.setObjectName(_fromUtf8("BtnCamera"))

        #文本框
        self.label_3 = QtGui.QLabel(DynamicForm)
        self.label_3.setGeometry(QtCore.QRect(60, 420, 131, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        #缺席名单输出框
        self.TextQuexi = QtGui.QTextEdit(DynamicForm)
        self.TextQuexi.setGeometry(QtCore.QRect(60, 460, 761, 231))
        self.TextQuexi.setObjectName(_fromUtf8("TextQuexi"))
        
        #返回主界面按钮
        self.BtnReruen = QtGui.QPushButton(DynamicForm)
        self.BtnReruen.setGeometry(QtCore.QRect(1039, 635, 141, 51))
        self.BtnReruen.setObjectName(_fromUtf8("BtnReruen"))

        self.retranslateUi(DynamicForm)
        QtCore.QMetaObject.connectSlotsByName(DynamicForm)
        
        #信号连接到指定槽
        self.BtnLuru.clicked.connect(self.on_BtnLuru_clicked)
        self.BtnCamera.clicked.connect(self.on_BtnCamera_clicked)
        self.BtnReruen.clicked.connect(self.on_BtnReturn_clicked)

    def retranslateUi(self, DynamicForm):
        DynamicForm.setWindowTitle(_translate("DynamicForm", "动态识别模式", None))
        self.label.setText(_translate("DynamicForm", "<html><head/><body><p><img src=\":/dynamicform/动态识别模式窗口背景.jpg\"/></p></body></html>", None))
        self.label_2.setText(_translate("DynamicForm", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">请录入应到人员名单：（人名之间用空格隔开）</span></p></body></html>", None))
        self.BtnLuru.setText(_translate("DynamicForm", "信息录入", None))
        self.BtnCamera.setText(_translate("DynamicForm", "摄像头识别", None))
        self.label_3.setText(_translate("DynamicForm", "<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">缺席名单：</span></p></body></html>", None))
        self.BtnReruen.setText(_translate("DynamicForm", "返回主界面", None))
        
    def on_BtnLuru_clicked(self):
        counter = 0  # 用来统计输入不规范的情况
        textYingdao = self.TextYingdao.toPlainText()  # 获取应到人员输入框内容
        if (textYingdao == ""):
            win32api.MessageBox(0, "请输入应到人员名单！", "提醒", win32con.MB_OK)
        else:
            if (textYingdao == "default"):
                textYingdao = "LiHuachao LiYu LiuHaoran WuKaiyan"
            names = textYingdao.split(" ")
            for name in names:
                pname = name + ".jpg"
                if os.path.exists(pname):
                    continue
                else:
                    counter += 1
                    m = name + "信息不存在！"
                    win32api.MessageBox(0, m, "提醒", win32con.MB_OK)
        if (counter == 0):
            print("信息录入完毕")
            if (textYingdao == "default"):
                textYingdao = "LiHuachao LiYu LiuHaoran WuKaiyan"
            print("应到人员名单为：", textYingdao)
            return textYingdao
    
    def video_face_recognition(self):
        video_capture = cv2.VideoCapture(0)
        video_capture.set(3, 640)
        video_capture.set(4, 480)

        strYingdao = self.TextYingdao.toPlainText()
        names = strYingdao.split(" ")

        attendee_names = []
        #读取图片
        images = []
        for name in names:
            pname = name + ".jpg"
            image = face_recognition.load_image_file(pname)
            images.append(image)

        #将images里的图片依次转化为128位向量
        face_encodings = []
        attendee_names = []
        absentee_names = []
        for image in images:
            encoding = face_recognition.face_encodings(image)[0]
            face_encodings.append(encoding)

        while True:
            #读取摄像头画面
            ret, frame = video_capture.read()

            #改变摄像头图像的大小
            small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)

            #opencv的图像是BGR格式的，转为我们需要的RGB
            rgb_small_frame = small_frame[:, :, ::-1]

            #存人脸位置
            face_locations = face_recognition.face_locations(rgb_small_frame)

            #存人脸向量
            target_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for i in range(len(target_encodings)):
                #显示人脸位置
                face_location = face_locations[i]
                top, right, bottom, left = face_location
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                #画框
                cv2.rectangle(frame, (left, top), (right, bottom), (0,255,255), 1)
                font = cv2.FONT_HERSHEY_DUPLEX

                #识别
                target_encoding = target_encodings[i]
                face_location = face_locations[i]
                results_recognition = face_recognition.compare_faces(face_encodings, target_encoding, tolerance = 0.36)
                face_name = "unknown"
                for j in range(len(results_recognition)):
                    if results_recognition[j]:
                        name = names[j]
                        face_name = name
                        m = 0
                        if len(attendee_names):
                            for i in range(len(attendee_names)):
                                if name != attendee_names[i]:
                                    m += 1
                                if m == len(attendee_names):
                                    attendee_names.append(name)
                        else:
                            attendee_names.append(name)

                print(attendee_names)
                cv2.putText(frame, face_name, (left + 6, bottom - 6), font, 1.0, (0, 0, 255), 1)

            #窗口
            cv2.namedWindow("Video", 0);
            cv2.imshow('Video', frame)

            #按ESC键退出
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        video_capture.release()
        cv2.destroyAllWindows()
        for item in names:
            if item in names:
                if item not in attendee_names:
                    absentee_names.append(item)
        print("缺席名单：", absentee_names)
        return(absentee_names)

    def on_BtnCamera_clicked(self):
        items = Ui_DynamicForm.video_face_recognition(self)
        self.TextQuexi.setText(','.join(items))

    def on_BtnReturn_clicked(self):
        self.form.close()


import background_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DynamicForm = QtGui.QWidget()
    ui = Ui_DynamicForm()
    ui.setupUi(DynamicForm)
    DynamicForm.show()
    sys.exit(app.exec_())
		sys.exit(app.exec_()) 
