# -*- coding: utf-8 -*- 

import face_recognition
import cv2 
from PyQt4 import QtCore, QtGui 
import os
#print(os.getcwd()) # 打印当前工作目录
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
   
class Dialog2(object): 
	def setupUi(self, Dialog): 
		Dialog.setObjectName(_fromUtf8("Dialog")) 
		Dialog.resize(800, 600) 
		self.form = Dialog 
		self.label = QtGui.QLabel(Dialog) 
		self.label.setGeometry(QtCore.QRect(150, 0, 521, 171)) 
		self.label.setObjectName(_fromUtf8("label")) 
		
		self.label_2 = QtGui.QLabel(Dialog) 
		self.label_2.setGeometry(QtCore.QRect(90, 110, 271, 141)) 
		self.label_2.setObjectName(_fromUtf8("label_2"))
		
		self.label_3 = QtGui.QLabel(Dialog)
		self.label_3.setGeometry(QtCore.QRect(470, 120, 161, 71))
		self.label_3.setObjectName(_fromUtf8("label_3"))
		
		self.pushButton = QtGui.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(90, 460, 121, 51))
		self.pushButton.setObjectName(_fromUtf8("pushButton")) 
		
		self.pushButton_2 = QtGui.QPushButton(Dialog)
		self.pushButton_2.setGeometry(QtCore.QRect(230, 460, 121, 51)) 
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		
		self.pushButton_3 = QtGui.QPushButton(Dialog)
		self.pushButton_3.setGeometry(QtCore.QRect(580, 460, 121, 51)) 
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
			
		self.textEdit = QtGui.QTextEdit(Dialog)
		self.textEdit.setGeometry(QtCore.QRect(90, 230, 261, 201))
		self.textEdit.setObjectName(_fromUtf8("textEdit"))	
		
		self.textEdit_2 = QtGui.QTextEdit(Dialog)
		self.textEdit_2.setGeometry(QtCore.QRect(470, 190, 231, 241))
		self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))	
		self.retranslateUi(Dialog) 
		QtCore.QMetaObject.connectSlotsByName(Dialog) 
		
		#信号连接到指定槽 
		self.pushButton.clicked.connect(self.on_pushButton_clicked) 
		self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
		self.pushButton_3.clicked.connect(self.on_pushButton_3_clicked)
		
	def retranslateUi(self, Dialog): 
		Dialog.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
		Dialog.setWindowTitle(_translate("Dialog", "摄像头实时识别", None)) 
		self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">基于摄像头实时识别的考勤系统</span></p></body></html>", None))
		self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">录入应到名单：</span></p></body></html>", None)) 
		self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">缺勤名单：</span></p></body></html>", None))
		self.pushButton.setText(_translate("Dialog","确认录入" , None))
		self.pushButton_2.setText(_translate("Dialog","运行识别" , None)) 
		self.pushButton_3.setText(_translate("Dialog", "离开", None)) 

	def on_pushButton_clicked(self): 
		textt = self.textEdit.toPlainText()   #获取文本框内容
		print("已录入信息")
		return textt
		
	def video_face_recognition(self):
		video_capture = cv2.VideoCapture(0)
		video_capture.set(3,640) # 设置宽度
		video_capture.set(4,480) # 设置高度
		
		str2 = self.on_pushButton_clicked()
		if(str2 == "default"):
			str2 = "ZhangJiale HuangWeikang NiuLifei JinMing ChangHao LiXiaoqiang LiuZhihui ZhaiTianren"
			
		ids = str2.split(" ")	# 人名信息
		print("录入信息为：", ids)
		attend_ids = []
		# 读取图片
		images = []
		for id in ids:
			picname = id + ".jpg"
			image = face_recognition.load_image_file(picname)
			images.append(image)
		
		# 将images里的图片依次转化为128位向量
		face_encodings = []
		attend_ids = []
		not_attend_ids = []
		for image in images:
			encoding = face_recognition.face_encodings(image)[0]
			face_encodings.append(encoding)
	
	
		while True:
			# 读取摄像头画面
			ret, frame = video_capture.read()
		
			# 改变摄像头图像的大小
			small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
		
			# opencv的图像是BGR格式的，转为我们需要的RGB
			rgb_small_frame = small_frame[:, :, ::-1]
		
			#存人脸位置
			face_locations = face_recognition.face_locations(rgb_small_frame)
		
			#存人脸向量
			test_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
		
	
			for i in range(len(test_encodings)):
				# 显示人脸位置
				face_location = face_locations[i]
				top, right, bottom, left = face_location
				top *= 4
				right *= 4
				bottom *= 4
				left *= 4
				# 画框
				cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 255), 1)
				font = cv2.FONT_HERSHEY_DUPLEX
				# 识别
				test_encoding = test_encodings[i]
				face_location = face_locations[i] 
				results = face_recognition.compare_faces(face_encodings, test_encoding, tolerance=0.36)
				name = "unknown"
				for j in range(len(results)):
					if results[j]:
						id = ids[j]
						name = id
						m = 0
						if len(attend_ids):
							for i in range(len(attend_ids)):
								if id != attend_ids[i]:
									m += 1
								if m == len(attend_ids):
									attend_ids.append(id)
						else:
							attend_ids.append(id)
	
				print(attend_ids)
				cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 255), 1)
			
			# 窗口
			cv2.namedWindow("Video",0);
			#cv2.resizeWindow("Video", 1800, 1500)
			cv2.imshow('Video', frame)
		
			# 按ESC退出
			k = cv2.waitKey(30) & 0xff
			if k == 27: # press 'ESC' to quit
				break
			
		video_capture.release()
		cv2.destroyAllWindows() 
		for item in ids:
			if item not in attend_ids:
				not_attend_ids.append(item)
		print("缺勤名单：", not_attend_ids)
		return(not_attend_ids)

	def on_pushButton_2_clicked(self): 
		items = Dialog2.video_face_recognition(self)
		self.textEdit_2.setText('/'.join(items))


	def on_pushButton_3_clicked(self):   
		self.form .close()  
	
if __name__ == "__main__": 

		import sys 
		app = QtGui.QApplication(sys.argv) 
		Dialog = QtGui.QDialog() 
		ui = Dialog2() 
		ui.setupUi(Dialog) 
		Dialog.show() 
		sys.exit(app.exec_()) 