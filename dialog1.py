# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import face_recognition
import cv2
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

# print(os.getcwd()) # 打印当前工作目录
os.chdir("C:\\Users\\Administrator\\Desktop\\iface\\faces_samples")

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


class Dialog1(QtGui.QWidget):  # 定义Dialog1为一个类 继承QtGui.QWidget

    def setupUi(self, Dialog):

        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 600)  # 设置窗口大小
        self.form = Dialog

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, -40, 501, 231))
        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 271, 171))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 210, 261, 261))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))

        self.dialog1_pushButton = QtGui.QPushButton(Dialog)
        self.dialog1_pushButton.setGeometry(QtCore.QRect(100, 480, 121, 41))
        self.dialog1_pushButton.setObjectName(_fromUtf8("pushButton"))

        self.dialog1_pushButton_2 = QtGui.QPushButton(Dialog)
        self.dialog1_pushButton_2.setGeometry(QtCore.QRect(240, 480, 121, 41))
        self.dialog1_pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(460, 160, 101, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(450, 210, 251, 261))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.dialog1_pushButton_3 = QtGui.QPushButton(Dialog)
        self.dialog1_pushButton_3.setGeometry(QtCore.QRect(580, 480, 121, 41))
        self.dialog1_pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.textEdit_2 = QtGui.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(100, 210, 261, 261))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # 信号连接到指定槽
        self.dialog1_pushButton_3.clicked.connect(self.on_dialog1_pushButton_3_clicked)
        self.dialog1_pushButton_2.clicked.connect(self.on_dialog1_pushButton_2_clicked)
        self.dialog1_pushButton.clicked.connect(self.on_dialog1_pushButton_clicked)

    def retranslateUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        Dialog.setWindowTitle(_translate("Form", "多目标静态人脸识别", None))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">静态人脸识别（考勤系统）</span></p></body></html>",
                                      None))
        self.dialog1_pushButton.setText(_translate("MainWindow", "加载信息", None))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:11pt;\">请录入应到人：</span></p><p><span style=\" font-size:11pt;\">（格式：名字加空格）</span></p></body></html>",
                                        None))
        self.dialog1_pushButton_2.setText(_translate("MainWindow", "运行", None))
        self.dialog1_pushButton_3.setText(_translate("MainWindow", "返回主界面", None))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#000000;\">缺勤人：</span></p></body></html>",
                                        None))

    def close_application(self):
        sys.exit()

    def on_dialog1_pushButton_clicked(self):
        textt = self.textEdit_2.toPlainText()  # 获取文本框内容
        # print(textt)
        print("已录入信息")
        return textt

    def faces_pictures(self):
        str1 = self.on_dialog1_pushButton_clicked()
        if (str1 == "default"):
            str1 = "ZhangJiale HuangWeikang NiuLifei JinMing ChangHao LiXiaoqiang LiuZhihui ZhaiTianren"
        ids = str1.split(" ")
        print("信息为：", ids)

        # 读取库中单人图片及测试图片
        images = []
        for id in ids:
            picname = id + ".jpg"
            image = face_recognition.load_image_file(picname)
            images.append(image)
            test_image = face_recognition.load_image_file(
                "C:\\Users\\Administrator\\Desktop\\iface\\faces_test\\test.jpg")

        # 将人脸的图像数据转换成128位向量
        face_encodings = []
        for image in images:
            encoding = face_recognition.face_encodings(image)[0]
            face_encodings.append(encoding)
            test_face_encodings = face_recognition.face_encodings(test_image)

        # 储存人脸位置信息并框出
        face_locations = face_recognition.face_locations(test_image)
        attend_ids = []
        not_attend_ids = []
        for i in range(len(test_face_encodings)):
            test_encoding = test_face_encodings[i]
            face_location = face_locations[i]
            top, right, bottom, left = face_location
            cv2.rectangle(test_image, (left, top), (right, bottom), (0, 255, 255), 2)
            results = face_recognition.compare_faces(face_encodings, test_encoding, tolerance=0.4)
            for j in range(len(results)):
                if results[j]:
                    id = ids[j]
                    attend_ids.append(id)
                    cv2.putText(test_image, id, (left - 10, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),
                                2)

        # 打印缺席名单
        for item in ids:
            if item not in attend_ids:
                not_attend_ids.append(item)
        cv2.putText(test_image, "not_attend_ids:", (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 180), 2)
        cv2.putText(test_image, "/".join(not_attend_ids), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 180), 2)

        # 显示窗口
        test_image_rgb = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB)
        cv2.namedWindow("results", 0);
        cv2.resizeWindow("results", 1280, 720)
        cv2.imshow("results", test_image_rgb)
        print("缺勤名单：", not_attend_ids)
        return (not_attend_ids)
        # 等待按键
        cv2.waitKey(0)

    def on_dialog1_pushButton_3_clicked(self):
        self.form.close()

    def on_dialog1_pushButton_2_clicked(self):

        i = Dialog1.faces_pictures(self)
        self.textEdit.setText('/'.join(i))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


